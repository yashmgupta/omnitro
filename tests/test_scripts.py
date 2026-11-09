import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "specialized-skills"


def load(relative):
    path = SKILLS / relative
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


power = load("statistical-power/scripts/power.py")
mt = load("statistical-analysis/scripts/multiple_testing.py")
snap = load("reproducible-workflows/scripts/snapshot_env.py")
vcf = load("genomics-variants/scripts/vcf_summary.py")
counts = load("rna-seq-analysis/scripts/check_counts_metadata.py")
safe = load("research-tables/scripts/safe_csv.py")
doi = load("citation-verification/scripts/doi_tools.py")


class PowerTests(unittest.TestCase):
    def test_known_means_sample_size(self):
        # Textbook value for d=0.5, alpha=0.05 two-sided, 80% power is about 64 per group.
        self.assertEqual(power.n_per_group_means(0.5), 64)
        self.assertEqual(power.n_per_group_means(0.8), 26)

    def test_known_proportions_sample_size(self):
        self.assertEqual(power.n_per_group_proportions(0.5, 0.3), 93)

    def test_power_round_trip(self):
        self.assertAlmostEqual(power.power_means(64, 0.5), 0.8, delta=0.02)
        self.assertGreater(power.power_means(100, 0.5), power.power_means(50, 0.5))

    def test_one_sided_needs_fewer(self):
        self.assertLess(power.n_per_group_means(0.5, two_sided=False), power.n_per_group_means(0.5))

    def test_dropout_and_validation(self):
        self.assertEqual(power.inflate_for_dropout(64, 0.2), 80)
        for bad in (lambda: power.n_per_group_means(0), lambda: power.n_per_group_means(0.5, alpha=1.5),
                    lambda: power.n_per_group_proportions(0.4, 0.4), lambda: power.inflate_for_dropout(10, 1)):
            with self.assertRaises(ValueError):
                bad()

    def test_cli(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            power.main(["means", "--d", "0.5", "--dropout", "0.2"])
        self.assertIn("n per group: 64; with dropout: 80", out.getvalue())


class MultipleTestingTests(unittest.TestCase):
    P = [0.01, 0.04, 0.03, 0.005]

    def test_benjamini_hochberg(self):
        self.assertEqual([round(x, 10) for x in mt.benjamini_hochberg(self.P)], [0.02, 0.04, 0.04, 0.02])

    def test_holm_and_bonferroni(self):
        self.assertEqual([round(x, 10) for x in mt.holm(self.P)], [0.03, 0.06, 0.06, 0.02])
        self.assertEqual([round(x, 10) for x in mt.bonferroni(self.P)], [0.04, 0.16, 0.12, 0.02])

    def test_adjusted_never_below_raw_and_capped(self):
        for method in (mt.benjamini_hochberg, mt.holm, mt.bonferroni):
            adjusted = method([0.9, 0.5, 0.001])
            self.assertTrue(all(0 <= a <= 1 for a in adjusted))
            self.assertTrue(all(a >= p for a, p in zip(adjusted, [0.9, 0.5, 0.001])))

    def test_invalid_values(self):
        for bad in ([float("nan")], [-0.1], [1.2]):
            with self.assertRaises(ValueError):
                mt.benjamini_hochberg(bad)


class SnapshotTests(unittest.TestCase):
    def test_checksum_and_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "data.txt"
            path.write_bytes(b"abc")
            result = snap.snapshot([str(path)], cwd=tmp)
        self.assertEqual(
            result["inputs"][str(path)], "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        )
        self.assertIsNone(result["git_commit"])
        self.assertIn("python", result)
        self.assertIsInstance(result["packages"], dict)


VCF = """##fileformat=VCFv4.2
##reference=GRCh38
##contig=<ID=chr1,length=248956422>
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\ts1\ts2
chr1\t100\t.\tA\tG\t50\tPASS\t.\tGT:DP\t0/1:10\t./.:0
chr1\t200\t.\tC\tT\t50\tPASS\t.\tGT:DP\t1|1:12\t0/0:9
chr1\t300\t.\tA\tC\t50\tLowQual\t.\tGT\t0/1\t./.
chr1\t400\t.\tAT\tA\t50\tPASS\t.\tGT\t0/1\t0/0
chr2\t500\t.\tG\tA,T\t50\tPASS\t.\tGT\t1/2\t0/0
"""


class VcfTests(unittest.TestCase):
    def test_summary(self):
        result = vcf.summarize(VCF.splitlines(keepends=True))
        self.assertEqual(result["records"], 5)
        self.assertEqual(result["multiallelic_records"], 1)
        self.assertEqual(result["alt_allele_types"], {"snv": 5, "indel_or_mnv": 1})
        # transitions: A>G, C>T, G>A (3); transversions: A>C, G>T (2)
        self.assertEqual(result["titv_ratio"], 1.5)
        self.assertEqual(result["filters"], {"PASS": 4, "LowQual": 1})
        self.assertEqual(result["reference_header"], "GRCh38")
        self.assertEqual(result["contig_style"], "chr-prefixed")
        self.assertEqual(result["contigs_missing_from_header"], ["chr2"])
        self.assertEqual(result["missing_genotype_fraction"], {"s1": 0.0, "s2": 0.4})

    def test_malformed_record(self):
        with self.assertRaises(ValueError):
            vcf.summarize(["chr1\t1\t.\tA\n"])


class CountMetadataTests(unittest.TestCase):
    META = [{"sample": "a"}, {"sample": "b"}]

    def test_ok(self):
        rows = [["gene", "a", "b"], ["g1", "5", "6"], ["g2", "0", "0"]]
        result = counts.check(rows, self.META)
        self.assertTrue(result["ok"])
        self.assertEqual(result["zero_count_features"], 1)
        self.assertEqual(result["library_sizes"], {"a": 5.0, "b": 6.0})

    def test_problems(self):
        rows = [["gene", "a", "c", "a"], ["g1", "1.5", "-1", "2"]]
        result = counts.check(rows, self.META)
        text = " ".join(result["problems"])
        self.assertFalse(result["ok"])
        for expected in ("duplicate count-matrix", "only in counts", "only in metadata", "negative", "non-integer"):
            self.assertIn(expected, text)

    def test_shape_and_column_errors(self):
        with self.assertRaises(ValueError):
            counts.check([["gene", "a"], ["g1", "1", "2"]], [{"sample": "a"}])
        with self.assertRaises(ValueError):
            counts.check([["gene", "a"]], [{"id": "a"}])


class SafeCsvTests(unittest.TestCase):
    def test_sanitize(self):
        self.assertEqual(safe.sanitize_cell("=1+1"), "'=1+1")
        self.assertEqual(safe.sanitize_cell("@SUM(A1)"), "'@SUM(A1)")
        self.assertEqual(safe.sanitize_cell("-cmd"), "'-cmd")
        self.assertEqual(safe.sanitize_cell("-3.5"), "-3.5")
        self.assertEqual(safe.sanitize_cell("+7"), "+7")
        self.assertEqual(safe.sanitize_cell("normal"), "normal")
        self.assertEqual(safe.sanitize_cell(None), "")

    def test_cli_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp, "in.csv"), Path(tmp, "out.csv")
            src.write_text('name,value\n"=HYPERLINK(""x"")",-2\n', encoding="utf-8")
            safe.main([str(src), str(dst)])
            self.assertEqual(dst.read_text(encoding="utf-8").splitlines()[1], "\"'=HYPERLINK(\"\"x\"\")\",-2")


class DoiTests(unittest.TestCase):
    def test_extract_normalize_and_duplicates(self):
        text = "See https://doi.org/10.1038/NATURE12373. Also (doi:10.1038/nature12373), and 10.1186/s13059-014-0550-8;"
        result = doi.report(text)
        self.assertEqual(result["total_mentions"], 3)
        self.assertEqual(result["duplicates"], {"10.1038/nature12373": 2})
        self.assertIn("10.1186/s13059-014-0550-8", result["unique_dois"])

    def test_no_dois(self):
        self.assertEqual(doi.report("no identifiers here")["unique_dois"], [])
        json.dumps(doi.report("x"))


if __name__ == "__main__":
    unittest.main()
