import random


def generate_sequences_mega_sena(quantity_of_sequences):
    sequencies = []
    for _ in range(quantity_of_sequences):
        sequence = sorted(random.sample(range(1, 61), 6))
        sequencies.append(sequence)
    print(sequencies)
