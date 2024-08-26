def create_mapping(frequent_itemsets):
    """Creates a mapping from frequent itemsets to labels."""
    mapping = {}
    counter = 1
    for _, row in frequent_itemsets.iterrows():
        items = frozenset(row['itemsets'])
        mapping[f"X{counter}"] = items
        counter += 1
    return mapping

def compress_transaction(transaction, mapping):
    """Compresses a single transaction using the mapping."""
    transaction_set = frozenset(transaction)
    compressed_transaction = []
    for key, items in mapping.items():
        if items.issubset(transaction_set):
            compressed_transaction.append(key)
            transaction_set -= items
    compressed_transaction.extend(transaction_set)
    return compressed_transaction

if __name__ == "__main__":
    # Example usage
    frequent_itemsets = pd.DataFrame({
        'itemsets': [frozenset(['A', 'B']), frozenset(['C', 'D'])]
    })
    mapping = create_mapping(frequent_itemsets)
    transaction = ['A', 'B', 'C']
    compressed_transaction = compress_transaction(transaction, mapping)
    print("Compressed Transaction:", compressed_transaction)
