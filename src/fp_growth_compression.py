# src/fp_growth_compression.py

import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder

def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        for line in file:
            dataset.append(line.strip().split())
    return dataset

def run_fp_growth(transactions, min_support=0.5):
    df = pd.DataFrame(transactions)
    frequent_itemsets = fpgrowth(df, min_support=0.3, use_colnames=True)
    return frequent_itemsets

def create_mapping(frequent_itemsets):
    mapping = {}
    itemset_id = 1
    for _, row in frequent_itemsets.iterrows():
        itemset = frozenset(row['itemsets'])
        if len(itemset) > 1:  # Ensure that only meaningful itemsets are mapped
            mapping[f'X{itemset_id}'] = itemset
            itemset_id += 1
    return mapping


def compress_dataset(dataset, mapping):
    compressed_dataset = []
    for transaction in dataset:
        compressed_transaction = []
        for key, itemset in mapping.items():
            if itemset.issubset(transaction):
                compressed_transaction.append(key)
                transaction = [item for item in transaction if item not in itemset]
        compressed_transaction.extend(transaction)
        compressed_dataset.append(compressed_transaction)
    return compressed_dataset

def decompress_dataset(compressed_dataset, mapping):
    decompressed_dataset = []
    for transaction in compressed_dataset:
        decompressed_transaction = []
        for item in transaction:
            if item in mapping:
                decompressed_transaction.extend(mapping[item])
            else:
                decompressed_transaction.append(item)
        decompressed_dataset.append(decompressed_transaction)
    return decompressed_dataset
