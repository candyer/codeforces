# https://codeforces.com/contest/1343/problem/C

def solve(n, arr):
	'''
	1 <= t <= 10^4
	1 <= n <= 2 * 10^5
	the sum of n over all test cases does not exceed 2 * 10^5
	−10^9 <= ai <= 10^9, ai != 0
	'''
	maxi = float('-inf')
	res = 0
	arr.append(arr[-1] * -1)
	for i in range(n):
		maxi = max(maxi, arr[i])
		if arr[i] * arr[i + 1] < 0:
			res += maxi
			maxi = float('-inf')
	return res

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().split()))
		print(solve(n, arr))

assert(solve(5, [1, 2, 3, -1, -2]) == 2)
assert(solve(4, [-1, -2, -1, -3]) == -1)
assert(solve(10, [-2, 8, 3, 8, -4, -15, 5, -2, -3, 1]) == 6)
assert(solve(6, [1, -1000000000, 1, -1000000000, 1, -1000000000]) == -2999999997)
assert(solve(5, [-9, -8, -3, 8, 2]) == 5)
