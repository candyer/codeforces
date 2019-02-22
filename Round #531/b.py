# https://codeforces.com/contest/1102/problem/B


from collections import defaultdict
def solve(n, k, array):
	tmp = defaultdict(list)
	for i in range(n):
		tmp[array[i]].append(i)
	res = [0] * n
	j = 0
	for key, val in tmp.items():
		if len(val) > k:
			return 'NO'
		i = j
		for pos in val:
			res[pos] = (i % k) + 1
			i += 1
		j = i
	return '{}{}{}'.format('YES', '\n', ' '.join(map(str, res)))

if __name__ == '__main__':
	n, k = map(int, raw_input().split())
	array = map(int, raw_input().split())
	print solve(n, k, array)


print solve(5, 2, [1, 1, 2, 2, 5])
print solve(4, 2, [1, 2, 2, 3])
print solve(5, 2, [3, 2, 1, 2, 3])
print solve(5, 2, [2, 1, 1, 2, 1])
print solve(5, 3, [1, 4, 3, 4, 4])
print solve(5, 4, [1, 1, 1, 2, 2])
print solve(5, 4, [1, 2, 1, 3, 7])
print solve(5, 5, [1, 2, 1, 3, 7])