# https://codeforces.com/contest/1108/problem/B

# 2 <= n <= 128
# 1 <= di <= 10^4


from collections import Counter
def solve(n, array):
	d = Counter(array)
	y = max(d)
	for num in range(1, int(y ** 0.5) + 1):
		if y % num == 0:
			if d[num] > 1:
				d[num] -= 1
			else:
				d.pop(num)
			if num != y/num:
				if d[y/num] > 1:
					d[y/num] -= 1
				else:
					d.pop(y/num)

	x = max(d)
	return '{} {}'.format(x, y)


if __name__ == '__main__':
	n = int(raw_input())
	array = map(int, raw_input().split())
	print solve(n, array)


assert solve(10, [10, 2, 8, 1, 2, 4, 1, 20, 4, 5]) == '8 20'
assert solve(2, [1, 1]) == '1 1'
