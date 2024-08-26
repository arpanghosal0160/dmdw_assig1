def load_dataset(file_path):
    """Loads the dataset from a .dat file."""
    with open(file_path, 'r') as file:
        dataset = [line.strip().split() for line in file]
    return dataset

if __name__ == "__main__":
    file_path = '../data/D_small.dat'
    dataset = load_dataset(file_path)
    print("Dataset Loaded:")
    for transaction in dataset:
        print(transaction)
