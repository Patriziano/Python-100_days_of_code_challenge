#!/usr/bin/python3
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
last_name = int(len(names) - 1)
random_name = random.randint(0, last_name)
bill_payer = names[random_name]
print('{} is going to pay for the meal'.format(bill_payer))
