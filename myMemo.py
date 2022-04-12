import time

start = time.time()

a, b = map(int,input().split())



memo = { 1: 1, 2: 2}
def get_length(n):
    if n in memo:
        # print('Used memo[', n, '] = ', memo[n])
        return memo[n]
    if n == 1:
        return n
    if n % 2 != 0:
        m = 3*n+1
        count = get_length(m)+1
        memo[m] = count - 1
        # print('memo[',m,'] = ', memo[m])
        return count
    else:
        m = int(n/2)
        count = get_length(m)+1
        memo[m] = count-1
        # print('memo[',m,'] = ', memo[m])
        return count

highest = 1
longest = 1
for i in range(a,b+1):
    if longest < get_length(i):
        highest = i
        longest = get_length(i)
    # print("longest={},highest={}".format(highest,longest))
print(highest,longest)
