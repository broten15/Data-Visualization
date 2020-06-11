from die import Die
import pygal

# Create dice
die_1 = Die()
die_2 = Die()

# Gets the possible results of both dice being multiplied
possible_results = [side_1 * side_2 for side_1 in range(1, die_1.sides + 1) 
    for side_2 in range(1, die_2.sides + 1)]
possible_results = list(dict.fromkeys(possible_results))
possible_results.sort()

# Rolls the dice a certain amount of times
results = [die_1.roll() * die_2.roll() for roll in  range(100000)]

# Analyzes the results
frequencies = [results.count(side) for side in possible_results]

# Vizualize the results
hist = pygal.Bar()

hist.title = "Results of rolling 2 dice 100,000 times"
hist.x_labels = possible_results
hist.x_title = 'Die side'
hist.y_title = "Times rolled"

hist.add("D6", frequencies)
hist.render_to_file('dice_visual.svg')