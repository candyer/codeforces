# https://codeforces.com/contest/1102/problem/D

def solve(n, s):
	zero, one, two = s.count('0'), s.count('1'), s.count('2')
	avg = n / 3
	if zero == one == two:
		return s
	res = list(s)
	if zero < avg:
		if two > avg:
			for i in range(n):
				if res[i] == '2':
					res[i] = '0'
					zero += 1
					two -= 1
					if zero == avg or two == avg:
						break

		if one > avg:
			for i in range(n):
				if res[i] == '1':
					res[i] = '0'
					zero += 1
					one -= 1
					if zero == avg or one == avg:
						break	
	if two < avg:
		if zero > avg:
			for i in range(n-1, -1, -1):
				if res[i] == '0':
					res[i] = '2'
					two += 1
					zero -= 1
					if zero == avg or two == avg:
						break	
		if one > avg:
			for i in range(n-1, -1, -1):
				if res[i] == '1':
					res[i] = '2'
					two += 1
					one -= 1
					if one == avg or two == avg:
						break	
	if one < avg:
		if zero > avg:
			count = 0
			for i in range(n):
				if res[i] == '0':
					if count < avg:
						count += 1
					else:
						res[i] = '1'
						one += 1
						zero -= 1
		j = 0
		while two > avg:
			if res[j] == '2':
				res[j] = '1'
				two -= 1
				one += 1
			j += 1
		
	return ''.join(res)

if __name__ == '__main__':
	n = int(raw_input())
	s = raw_input()
	print solve(n, s)

assert solve(6, '221211') == '020211'
assert solve(3, '122') == '102'
assert solve(3, '121') == '021'
assert solve(12, '222222222222') == '000011112222'
assert solve(12, '111111111111') == '000011112222'
assert solve(12, '000000000000') == '000011112222'
assert solve(6, '000000') == '001122'
assert solve(6, '120110') == '120120'
assert solve(6, '211200') == '211200'
