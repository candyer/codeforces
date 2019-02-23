# https://codeforces.com/contest/1102/problem/C


def solve(n, x, y, array):
	count = 0
	for num in array:
		if num <= x:
			count += 1
	if x > y:
		return n
	else:
		return (count + 1) / 2

if __name__ == '__main__':
	n, x, y = map(int, raw_input().split())
	array = map(int, raw_input().split())
	print solve(n, x, y, array)

assert solve(6, 3, 2, [2, 3, 1, 3, 4, 2]) == 6
assert solve(5, 3, 3, [1, 2, 4, 2, 3]) == 2
assert solve(6, 3, 3, [1, 2, 4, 2, 3, 1]) == 3
assert solve(5, 5, 6, [1, 2, 6, 10, 3]) == 2
assert solve(5, 1, 1, [1, 2, 3, 4, 5]) == 1