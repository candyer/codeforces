# http://codeforces.com/contest/1141/problem/0


from fractions import gcd
def solve(n, m):
	g = gcd(n, m)
	res = 0
	n, m = n / g, m / g
	while m % 6 == 0 and m / 6 >= n:
		res += 2
		m /= 6
	while  m % 3 == 0 and m / 3 >= n:
		res += 1
		m /= 3	
	while  m % 2 == 0 and m / 2 >= n:
		res += 1
		m /= 2
	if m != n:
		return -1		
	return res

# if __name__ == '__main__':
# 	n, m = map(int, raw_input().split())
# 	print solve(n, m)

assert solve(2, 324) == 5
assert solve(6, 72) == 3
assert solve(10, 40) == 2
assert solve(120, 51840) == 7
assert solve(42, 42) == 0
assert solve(48, 72) == -1
assert solve(2, 24) == 3
assert solve(10, 100) == -1

