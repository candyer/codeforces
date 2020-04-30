# https://codeforces.com/contest/1343/problem/D

########## brute force ###########
# def solve(n, k, arr):
# 	'''
# 	1 <= t <= 10^4
# 	2 <= n <= 2 * 10^5, n % 2 == 0
# 	1 <= k <= 2 * 10^5
# 	1 <= ai <= k
# 	'''
# 	res = float('inf')
# 	for x in range(2, 2 * k + 1):
# 		tmp = 0
# 		for i in range(n // 2):
# 			mini, maxi = min(arr[i], arr[n - i - 1]), max(arr[i], arr[n - i - 1])
# 			sm = mini + maxi 
# 			if sm != x:
# 				if mini + 1 <= x <= maxi + k:
# 					tmp += 1
# 				else:
# 					tmp += 2
# 		res = min(res, tmp)
# 	return res



########## prefix sum ###########
from itertools import accumulate
def solve(n, k, arr):
	'''
	1 <= t <= 10^4
	2 <= n <= 2 * 10^5, n % 2 == 0
	1 <= k <= 2 * 10^5
	1 <= ai <= k
	'''
	count = [0] * (2 * k + 2)
	for i in range(n // 2):
		a, b = arr[i], arr[n - i - 1]
		if a > b:
			a, b = b, a
		count[a + 1] += 1
		count[b + k + 1] -= 1

		count[a + b] += 1
		count[a + b + 1] -= 1
	return n - max(accumulate(count))

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n, k = map(int, input().split())
		arr = list(map(int, input().split()))
		print(solve(n, k, arr))

assert(solve(4, 2, [1, 2, 1, 2]) == 0)
assert(solve(4, 3, [1, 2, 2, 1]) == 1)
assert(solve(8, 7, [6, 1, 1, 7, 6, 3, 4, 6]) == 4)
assert(solve(6, 6, [5, 2, 6, 1, 3, 4]) == 2)



