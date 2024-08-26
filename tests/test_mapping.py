import unittest
import pandas as pd

from src.mapping import create_mapping, compress_transaction

class TestMapping(unittest.TestCase):
    def test_create_mapping(self):
        frequent_itemsets = pd.DataFrame({
            'itemsets': [frozenset(['A', 'B']), frozenset(['C', 'D'])]
        })
        mapping = create_mapping(frequent_itemsets)
        self.assertGreater(len(mapping), 0)

    def test_compress_transaction(self):
        mapping = {'X1': frozenset(['A', 'B'])}
        transaction = ['A', 'B', 'C']
        compressed_transaction = compress_transaction(transaction, mapping)
        self.assertIn('X1', compressed_transaction)

if __name__ == "__main__":
    unittest.main()
