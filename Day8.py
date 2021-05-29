Q1:

import statistics as st

# Set data
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = st.mean(x)
mean_y = st.mean(y)
x_squared = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

# Set the B and A
b = (n * xy - sum(x) * sum(y)) / (n * x_squared - (sum(x) ** 2))
a = mean_y - b * mean_x

# Gets the result and show on the screen
print (round(a + 80 * b, 3))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

regression X:
3x + 4y + 8 = 0
- 4y = 3x + 8
-y = 3x/4 + 8/4
-y = 3x/4 + 4 (reverse signal)
y = -3x/4 - 4
bx = -3/4
regression Y:
4x + 3y + 7 = 0
-4y = 3y + 7
-x = 3x/4 + 7/4 (reverse signal)
y =  -3x/4 - 7/4
by = -3/4
r² = bx * by
r² = -3/4 * -3/4
r² = 9/16
r +/- 3/4
if bx = by then
  r = -3/4
"""

print ("Result is: {}".format("-3/4"))
