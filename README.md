# Transaction Data Compression using Apriori Algorithm

This project implements a data compression method for transactional datasets using the Apriori algorithm.

## Project Structure

- `data/`: Contains dataset files.
- `src/`: Main code for loading data, applying Apriori, creating mappings, and evaluating compression.
- `tests/`: Unit tests for various modules.
- `results/`: Stores output from compression and decompression.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python src/main.py
   ```

## How to Run Tests

1. Run all tests:
   ```bash
   python -m unittest discover -s tests
   ```

## Dependencies

- Python 3.7+
- mlxtend
- pandas
