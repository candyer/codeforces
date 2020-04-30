# https://codeforces.com/contest/1343/problem/B

def solve(n):
	'''
	1 <= t <= 10^4
	2 <= n <= 2 * 10^5, n % 2 == 0
	'''
	if n // 2 % 2:
		return 'NO'
	res = [0] * n
	for i in range(n // 2):
		res[i] = 2 * (i + 1)
		res[i + n // 2] = 2 * i + 1
	res[-1] += n // 2
	print('YES')
	return ' '.join(map(str, res))

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		print(solve(n))
