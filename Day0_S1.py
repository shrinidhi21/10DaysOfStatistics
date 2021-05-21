# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

num = list(map(int, input().split()))

print(sum(num)/n)

mid = n//2

if n%2 :
    print(sorted(num)[mid])
else:
    print(sum(sorted(num)[mid-1:mid+1])/2)
    
from collections import Counter

c = Counter(num)

mode = [k for k,v in c.items() if v == c.most_common(1)[0][1]]

if len(mode)>1:
    print(min(mode))
else:
    print(mode)
