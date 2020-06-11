from die import Die
import matplotlib as plt

# Creates dice
die_1 = Die()
die_2 = Die()

# rolls the dice
results = [die_1.roll() + die_2.roll() for roll in range(100000)]

# analyzes results
frequencies = [results.count(side) for side in range(2, die_1.sides + die_2.sides + 1)]

print(frequencies)


