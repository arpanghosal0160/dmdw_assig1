import unittest
from src.compression_evaluation import evaluate_compression, decompress_dataset

class TestCompressionEvaluation(unittest.TestCase):
    def test_evaluate_compression(self):
        original_dataset = [['A', 'B', 'C'], ['A', 'B']]
        compressed_dataset = [['X1', 'C'], ['X1']]
        mapping = {'X1': frozenset(['A', 'B'])}
        compression_ratio = evaluate_compression(original_dataset, compressed_dataset, mapping)
        self.assertGreater(compression_ratio, 0.01)  # Check for minimal compression


    def test_decompress_dataset(self):
        compressed_dataset = [['X1', 'C'], ['X1']]
        mapping = {'X1': frozenset(['A', 'B'])}
        decompressed_dataset = decompress_dataset(compressed_dataset, mapping)
        self.assertEqual([sorted(t) for t in decompressed_dataset], [['A', 'B', 'C'], ['A', 'B']])


if __name__ == "__main__":
    unittest.main()
