#!/usr/bin/python3
if __name__ == "__main__":

    import random

    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)
    result = random.randint(0, 1)
    if result == 1:
        print("Heads")
    elif result ==0:
        print("Tails")
