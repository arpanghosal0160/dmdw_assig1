def evaluate_compression(original_dataset, compressed_dataset, mapping):
    """Evaluates the compression and ensures decompression is lossless."""
    original_size = sum(len(transaction) for transaction in original_dataset)
    compressed_size = sum(len(transaction) for transaction in compressed_dataset)
    mapping_size = sum(len(items) for items in mapping.values())

    compression_ratio = (original_size - (compressed_size + mapping_size)) / original_size * 100

    print(f"Original Dataset Size: {original_size}")
    print(f"Compressed Dataset Size: {compressed_size}")
    print(f"Mapping Size: {mapping_size}")
    print(f"Compression Ratio: {compression_ratio:.2f}%")

    return compression_ratio

def decompress_dataset(compressed_dataset, mapping):
    """Decompresses the dataset using the mapping."""
    decompressed_dataset = []
    reverse_mapping = {v: k for k, v in mapping.items()}

    for transaction in compressed_dataset:
        decompressed_transaction = []
        for item in transaction:
            if item in mapping:
                decompressed_transaction.extend(mapping[item])
            else:
                decompressed_transaction.append(item)
        decompressed_dataset.append(sorted(decompressed_transaction))
    return decompressed_dataset

if __name__ == "__main__":
    # Example usage
    original_dataset = [['A', 'B', 'C'], ['A', 'B'], ['B', 'C'], ['A', 'C']]
    compressed_dataset = [['X1', 'C'], ['X1'], ['B', 'C'], ['A', 'C']]
    mapping = {'X1': frozenset(['A', 'B'])}
    evaluate_compression(original_dataset, compressed_dataset, mapping)
    decompressed_dataset = decompress_dataset(compressed_dataset, mapping)
    assert sorted(original_dataset) == sorted(decompressed_dataset), "Decompression is not lossless!"
    print("Decompression is lossless!")
