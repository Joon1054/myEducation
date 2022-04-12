
a, b = map(int,input().split())
memo = {1: 1, 2:2}

def get_length(n):
    if n in memo:
        print("used memo" ,memo.get(n))
        return memo.get(n)
    if n == 1:
        print("1")
        return 1
    if n%2 != 0:
        print(n,"->",end=" ")
        n = int(3*n+1)
        return get_length(n)+1
    else:
        print(n,"->",end=" ")
        n = int (n / 2)
        return get_length(n)+1
count = 0
longestNum = 1
longest = 0
for i in range (a,b+1):
    count = get_length(i)
    memo[i] = count
    if longest < count:
        longest = count
        longestNum = i
print(longestNum, longest)
print(memo)
