#!/usr/bin/python3
import random

def insertion_sort(collection):
    for i in range(1, len(collection)):
        j = i - 1
        key = collection[i]
        while j >= 0 and key < collection[j]:
            collection[j + 1] = collection[j]
            j -= 1
        collection[j + 1] = key


if __name__ == "__main__":
    ary = []
    for i in range(10):
        ary.append(random.randint(1, 100))
    print(ary)

    insertion_sort(ary)
    print(ary)
