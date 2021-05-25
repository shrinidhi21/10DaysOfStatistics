# Question: The ratio of boys to girls for babies born in Russia is 1.09 : 1.
# If there is 1 child born per birth, what proportion of Russian families with
# exactly 6 children will have at least 3 boys?

# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

def binomial(x, n, p):
    f = factorial(n) / (factorial(n - x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))

# Set data
values = list(map(float, input().split()))
p = values[0] / (values[0] + values[1])
n = 6

# Get binomial result
result = binomial(3,n,p) + binomial(4,n,p) + binomial(5,n,p) + binomial(6,n,p)
print(round(result, 3))

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question: A manufacturer of metal pistons finds that, on average, 12% of the
# pistons they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:

# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

def binomial(x, n, p):
    f = factorial(n) / (factorial(n - x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))

# Set data
values = list(map(float, input().split()))
p = (values[0] / 100)
n = int(values[1])

# First rule: No more than 2 rejects
no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects = no_more_than_2_rejects + binomial(i, n, p)
print(round(no_more_than_2_rejects, 3))

# Second rule: At least 2 rejects
at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects = at_least_2_rejects + binomial(i, n, p)
print(round(at_least_2_rejects, 3))
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question: The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the
# 5th inspection?

# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = q ** (n - 1) * p
print(round(result, 3))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question: The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the
# first 5 inspections?

# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

# Show the final result
print(round(result, 3))
