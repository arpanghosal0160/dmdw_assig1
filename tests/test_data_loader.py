import unittest
from src.data_loader import load_dataset

class TestDataLoader(unittest.TestCase):
    def test_load_dataset(self):
        dataset = load_dataset('data/D_small.dat')

        self.assertIsInstance(dataset, list)
        self.assertGreater(len(dataset), 0)

if __name__ == "__main__":
    unittest.main()
