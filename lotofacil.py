import random


def generate_sequences_lotofacil(quantity_of_sequences):
    sequencies = []
    for _ in range(quantity_of_sequences):
        sequence = sorted(random.sample(range(1, 26), 15))
        sequencies.append(sequence)
    print(sequencies)
