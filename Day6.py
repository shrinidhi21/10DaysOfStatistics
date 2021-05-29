#Q1: A large elevator can transport a maximum of 9800 pounds. Suppose a
# load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean
# of u = 205 pounds and a standard deviation of a = 15 pounds. Based on this
# information, what is the probability that all 49 boxes can be safely loaded
# into the freight elevator and transported?
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Gets the result and show on the screen
print (round(cumulative(new_mean, new_std, max_weight),4))
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q2: The number of tickets purchased by each student for the
# University X vs. University Y football game follows a distribution that has
# a mean of u = 2.4 and a standard deviation of 20.
# A few hours before the game starts, 100 eager students line up to purchase
# last-minute tickets. If there are only 250 tickets left, what is the
# probability that all 100 students will be able to purchase tickets?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Gets the result and show on the screen
print (round(cumulative(new_mean, new_std, max_weight),4))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q3: You have a sample of 100 values from a population with mean u = 500
# and with standard deviation a = 80. Compute the interval that covers the
# middle 95% of the distribution of the sample mean; in other words, compute
# A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note
# that z is the z-score.

# Import library
import math

# Set data
n = float(input())
mean = float(input())
std = float(input())
percent_ci = float(input())
value_ci = float(input())

# Formula CI
ci = value_ci * (std / math.sqrt(n))

# Gets the result and show on the screen
print(round(mean - ci, 2))
print(round(mean + ci, 2))
