import json
import unittest
from pathlib import Path
from src.records import read_records

class RecordFormatTests(unittest.TestCase):
    def test_sample_has_declared_shape(self):
        path = Path(__file__).parents[1] / "data/sample.json"
        rows = read_records(path)
        self.assertGreaterEqual(len(rows), 2)
        self.assertTrue(all(row["record_id"] for row in rows))

    def test_invalid_shape_is_rejected(self):
        path = Path(__file__).parents[1] / "data/invalid.json"
        path.write_text(json.dumps({"records": [{}]}), encoding="utf-8")
        try:
            with self.assertRaises(ValueError):
                read_records(path)
        finally:
            path.unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
