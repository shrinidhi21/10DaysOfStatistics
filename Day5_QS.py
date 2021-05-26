  
# Question: A random variable, X, follows Poisson distribution with mean of 2.5
# Find the probability with which the random variable X is equal to 5.

# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

# Set data
mean = float(input())
k = float(input())
e = 2.71828

# Gets the result and show on the screen
result = ((mean ** k) * (e ** -mean)) /  factorial(k)
print(round(result, 3))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question: The manager of a industrial plant is planning to buy a machine of
# either type A or type B. For each day’s operation:
# The number of repairs, X, that machine A needs is a Poisson random variable
# with mean 0.88. The daily cost of operating A is C = 160 + 40X².
# The number of repairs, Y, that machine B needs is a Poisson random variable
# with mean 1.55. The daily cost of operating B is C = 128 + 40Y².

# Set data
lambdas = list(map(float, input().split()))
lambda_a = lambdas[0]
lambda_b = lambdas[1]

# Gets the result and show on the screen
print (round(160 + 40 * (lambda_a + lambda_a ** 2), 3))
print (round(128 + 40 * (lambda_b + lambda_b ** 2), 3))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question: In a certain plant, the time taken to assemble a car is a random
# variable, X, having a normal distribution with a mean of 20 hours and a
# standard deviation of 2 hours. What is the probability that a car can be
# assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(cumulative(mean, std, less_period),3))
print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question: The final grades for a Physics exam taken by a large group of
# students have a mean of mi = 70 and a standard deviation of sigma = 10.
# If we can approximate the distribution of these grades by a normal
# distribution, what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade < 60)?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
val_first_question = float(input())
val_sec_third_question = float(input())

# Gets the result and show on the screen
print (round(100 - (cumulative(mean, std, val_first_question) * 100), 2))
print (round(100 - (cumulative(mean, std, val_sec_third_question) * 100), 2))
print (round(cumulative(mean, std, val_sec_third_question) * 100, 2))
