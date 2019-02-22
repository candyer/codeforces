# https://codeforces.com/contest/1102/problem/A

# 1 <= n <= 2*10^9


def solve(n):
	if n % 2 == 0:
		if (n - 2) % 4 == 0:
			return 1
		else:
			return 0
	else:
		if (n - 1) % 4 == 0:
			return 1
		return 0

if __name__ == '__main__':
	n = int(raw_input())
	print solve(n)


assert solve(1) == 1
assert solve(2) == 1
assert solve(3) == 0
assert solve(4) == 0
assert solve(5) == 1
assert solve(6) == 1
assert solve(7) == 0
assert solve(8) == 0

