# http://codeforces.com/contest/1141/problem/B


# def solve(n, array):
# 	res = 0
# 	tmp = 0
# 	x = []
# 	for i in range(n):
# 		print '-----------------------------------------i:', i, array[i]
# 		# print array[i % n]
# 		if array[i % n] == 1:
# 			tmp += 1
# 		else:
# 			res = max(res, tmp)
# 			# if tmp > 0:
# 			x.append(tmp)
# 			tmp = 0
# 		print tmp
# 	# if array[0] ==  array[-1] == 1:
# 	# 	return x[0] + x[0-1]
# 	return res, x



def solve(n, array):
	res = 0
	tmp = 0
	count = []
	for num in array+[0]:
		if num == 1:
			tmp += 1
		else:
			res = max(res, tmp)
			count.append(tmp)
			tmp = 0
	if array[0] ==  array[-1] == 1 and len(count) > 1:
		return max(count[0] + count[0-1], res)
	return res

if __name__ == '__main__':
	n = int(raw_input())
	array = map(int, raw_input().split())
	print solve(n, array)


print solve(5, [1,0,1,0,1])
print solve(6, [0,1,0,1,1,0])
print solve(7, [1,0,1,1,1,0,1])
print solve(3, [0,0,0])
print solve(5, [1, 0, 1, 1, 1])
print solve(1, [0, 1, 1])

