import numpy as np
from keras.utils import to_categorical

DNA_2_digit = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
digit_2_DNA = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def dna_to_number(base):
    return DNA_2_digit[base]


def number_2_dna(digit):
    return digit_2_DNA[digit]


def dna_to_onehot(sequence):
    data = map(dna_to_number, sequence)
    data = np.array(data)
    # one hot encode
    encoded = to_categorical(data, num_classes=4)
    return encoded


def onehot_to_dna(encoded):
    decoded = ''
    for onehot in encoded:
        inverted = np.argmax(onehot)
        decoded += number_2_dna(inverted)
    return decoded
