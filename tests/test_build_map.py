import unittest

from build_map import load, mermaid, series_md, validate


class MapTest(unittest.TestCase):
    def test_registry_valid(self):
        self.assertEqual(validate(load()), [])

    def test_detects_forward_dependency(self):
        reg = load()
        reg["episodes"][0]["builds_on"] = [5]
        self.assertTrue(any("later episode" in p for p in validate(reg)))

    def test_outputs(self):
        reg = load()
        self.assertIn("E3 --> E16", mermaid(reg))
        self.assertEqual(series_md(reg).count("](https://github.com/sghatge/safe-to-send-"), 28)


if __name__ == "__main__":
    unittest.main()
