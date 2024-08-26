# src/main.py

from fp_growth_compression import (
    load_dataset,
    run_fp_growth,
    create_mapping,
    compress_dataset,
    decompress_dataset
)
from compression_evaluation import evaluate_compression

def main():
    # Load the dataset
    dataset = load_dataset('data/D_small.dat')
    
    # Run FP-Growth algorithm to find frequent itemsets
    frequent_itemsets = run_fp_growth(dataset, min_support=0.5)
    
    # Create mapping based on frequent itemsets
    mapping = create_mapping(frequent_itemsets)
    
    # Compress the dataset
    compressed_dataset = compress_dataset(dataset, mapping)
    
    # Evaluate the compression
    original_size, compressed_size, mapping_size, compression_ratio = evaluate_compression(dataset, compressed_dataset, mapping)
    
    # Output results
    print(f"Original Dataset Size: {original_size}")
    print(f"Compressed Dataset Size: {compressed_size}")
    print(f"Mapping Size: {mapping_size}")
    print(f"Compression Ratio: {compression_ratio}%")
    
    # Decompress the dataset to verify lossless compression
    decompressed_dataset = decompress_dataset(compressed_dataset, mapping)
    assert dataset == decompressed_dataset, "Decompression failed: Original and decompressed datasets do not match."

if __name__ == "__main__":
    main()
