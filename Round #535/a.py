# https://codeforces.com/contest/1108/problem/A

# 1 <= q <= 500
# 1 <= l1, r1, l2, r2 <= 10^9, l1 < r1, l2 < r2

def solve(l1, r1, l2, r2):
	a = b = 0
	if l1 <= l2:
		a, b = l1, r2
	else:
		a, b = r1, l2
	return '{} {}'.format(a, b)

if __name__ == '__main__':
	q = int(raw_input())
	for _ in range(q):
		l1, r1, l2, r2 = map(int, raw_input().split())
		print solve(l1, r1, l2, r2)


assert solve(1, 2, 1, 2) == '1 2'
assert solve(2, 6, 3, 4) == '2 4'
assert solve(1, 2, 1, 3) == '1 3'
assert solve(1, 4, 5, 8) == '1 8'
assert solve(4, 10, 3, 6) == '10 3'
assert solve(2, 4, 1, 3) == '4 1'
assert solve(100, 101, 1, 3) == '101 1'