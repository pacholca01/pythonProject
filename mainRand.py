import numpy as np
import matplotlib.pyplot as plt

# Pseudo random numbers
rand = np.random.rand()
print(rand)

# Starting from a seed.
np.random.seed(123)

# Notice how the number produced doesnt change when called to print again. This ensures reproducibility
rand = np.random.seed(123)
print(rand)

coin = np.random.randint(0, 2)  # Generate a number between 0 and 1
print(coin)
coin = np.random.randint(0, 2)
print(coin)

# Generate and print random float
print(np.random.rand())

# Print randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))

# Finish the control construct
step = 50
dice = np.random.randint(1, 7)
if dice <= 2:
    step -= 1
elif dice <= 5:
    step += 1
else:
    step += np.random.randint(1, 7)

# Print out dice and step
print("\n")
print(dice)
print(step)

# Record Random Steps in an Outcome Array
outcomes = []
for i in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print("\n")
print(outcomes)

# Record Random Walk in an Array
tailsWalk = [0]  # tailsWalk needs to be initialized with a 0 so that the array becomes an int array
for i in range(10):
    coin = np.random.randint(0, 2)
    tailsWalk.append(tailsWalk[i] + coin)
    # append to array tailsWalk the coin value for the iteration of the loop in our range
    # since coin is either 0 or 1, the walk will increment each time a tails is generated
print(tailsWalk)

# Dice Game Exercise
# Initialize random_walk
random_walk = [0]

# Complete the for loop
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Plot random_walk
plt.plot(random_walk)

# Show the plot
# plt.show()
plt.clf()

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10):

    # Code from before
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print("\n")
print(all_walks)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
print("\n")
print(np_aw)

# Plot np_aw and show
plt.clf()
plt.plot(np_aw)
# plt.show()

# Clear the figure
plt.clf()

# Visualize all walks
# all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a NumPy array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.
#
# The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.
#
# Instructions
# 100 XP
# Use np.array() to convert all_walks to a NumPy array, np_aw.
# Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
# Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
# Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?


# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
print("\n")
print(np_aw_t)

# Plot np_aw_t and show
plt.plot(np_aw_t)
# plt.show()
plt.clf()

# Recreate the Game so that there is a chance of freefall in the dice roll schema.
# Implement clumsiness
# With this neatly written code of yours, changing the number of times the random walk should be simulated is super-easy. You simply update the range() function in the top-level for loop.
#
# There's still something we forgot! You're a bit clumsy and you have a 0.1% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0.
#
# Instructions
# 100 XP
# Change the range() function so that the simulation is performed 250 times.
# Finish the if condition so that step is set to 0 if a random float is less or equal to 0.001. Use np.random.rand().


# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
# plt.show()
plt.clf()

# Plot the distribution
# All these fancy visualizations have put us on a sidetrack. We still have to solve the million-dollar problem: What are the odds that you'll reach 60 steps high on the Empire State Building?
#
# Basically, you want to know about the end points of all the random walks you've simulated. These end points have a certain distribution that you can visualize with a histogram.
#
# Note that if your code is taking too long to run, you might be plotting a histogram of the wrong data!
#
# Instructions
# 100 XP
# To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
# From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. Store this NumPy array as ends.
# Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
# plt.show()
plt.clf()

endsBool = ends >= 60
count = 0
for x in endsBool:
    if x == True:
        count += 1
likelihood = count/500
print("\n")
print(likelihood)

mean = np.mean(ends>=30)
print(mean)
