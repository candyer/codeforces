# https://codeforces.com/contest/1343/problem/A

def solve(n):
	'''
	1 <= t <= 10^4
	3 <= n <= 10^9
	'''
	i = count = 1
	while count < n:
		count += pow(2, i)
		if n % count == 0:
			return n // count
		i += 1

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		print(solve(n))
		

assert(solve(3) == 1)
assert(solve(6) == 2)
assert(solve(7) == 1)
assert(solve(21) == 7)
assert(solve(28) == 4)
assert(solve(999999999) == 333333333)
assert(solve(999999984) == 333333328)
