# Q1: Given two n-element data sets, X and Y, calculate the value of
# the Pearson correlation coefficient.

# import libraries
import statistics as st

# define function to Pearson correlation coefficient
def correlation_coefficient(n, dt_x, dt_y):
    mean_x = st.mean(dt_x)
    mean_y = st.mean(dt_y)
    std_x = st.pstdev(dt_x)
    std_y = st.pstdev(dt_y)
    c = 0
    for i in range(n):
        c = c + (dt_x[i] - mean_x) * (dt_y[i] - mean_y)
    return c / (n * std_x * std_y)

# Set data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(correlation_coefficient(n, data_set_x, data_set_y), 3))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q2: Given two n-element data sets, X and Y, calculate the value of
# Spearman's rank correlation coefficient.

# Define functions
def rank(dt):
    rank = {}
    sort = sorted(dt)
    for i in range(len(dt)):
        for j in range(len(sort)):
            if dt[i] == sort[j]:
                rank[dt[i]] = j + 1
    return rank

def spearman(x, y, rx, ry, n):
    diff_rank = 0
    for i in range(n):
        if rx[x[i]] != ry[y[i]]:
            diff_rank = diff_rank + ((rx[x[i]] - ry[y[i]]) ** 2)
    return (6 * diff_rank) / (n ** 3 - n)

# Set data
n = int(float(input()))
data_set_x = list(map(float, input().split()))
data_set_y = list(map(float, input().split()))

# Get rank
rank_x = rank(data_set_x)
rank_y = rank(data_set_y)

# Gets the result and show on the screen
s = spearman(data_set_x, data_set_y, rank_x, rank_y, n)
print(round(1 - s, 3))
