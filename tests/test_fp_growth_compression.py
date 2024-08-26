# tests/test_fp_growth_compression.py
import pandas as pd

import unittest
from src.fp_growth_compression import (
    load_dataset,
    run_fp_growth,
    create_mapping,
    compress_dataset,
    decompress_dataset
)


class TestFPGrowthCompression(unittest.TestCase):

    def test_load_dataset(self):
        dataset = load_dataset('data/D_small.dat')
        self.assertGreater(len(dataset), 0)

    def test_run_fp_growth(self):
        dataset = [['A', 'B', 'C'], ['A', 'B'], ['B', 'C']]
        frequent_itemsets = run_fp_growth(dataset, min_support=0.5)
        self.assertGreater(len(frequent_itemsets), 0)

    def test_create_mapping(self):
        frequent_itemsets = pd.DataFrame({
            'itemsets': [['A', 'B'], ['A', 'B', 'C'], ['B', 'C']]
        })
        mapping = create_mapping(frequent_itemsets)
        self.assertTrue(len(mapping) > 0)

    def test_compress_dataset(self):
        dataset = [['A', 'B', 'C'], ['A', 'B'], ['B', 'C']]
        mapping = {'X1': frozenset(['A', 'B'])}
        compressed_dataset = compress_dataset(dataset, mapping)
        self.assertEqual(len(compressed_dataset), 3)

    def test_decompress_dataset(self):
        compressed_dataset = [['X1', 'C'], ['X1']]
        mapping = {'X1': {'A', 'B'}}
        decompressed_dataset = decompress_dataset(compressed_dataset, mapping)
        # Sort transactions before comparison
        self.assertEqual([sorted(t) for t in decompressed_dataset], [['A', 'B', 'C'], ['A', 'B']])

if __name__ == "__main__":
    unittest.main()
