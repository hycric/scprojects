"""
File: largest_digit.py
Name: Richard
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function calls the helper function then returns the largest digit of the number to main.
	:param n:int, a integer ready to be speculated by function
	:return:int returns the largest digit of the integer
	"""
	k = 1
	n = abs(n)    # 避免負數%
	mx = n % 10**k
	return find_largest_digit_helper(n,mx,k)


def find_largest_digit_helper(n,mx,k):
	"""
	This helper returns the greatest digit of a number.
	:param n:int, a integer ready to be speculated by function
	:param mx: int, a temporary maximum digit of integer n
	:param k: int, a variable that follows the arithmetic sequence of k += 1
	:return: int, returns the largest digit of the integer n
	"""
	k += 1
	r = n % 10**k
	if r == n:  # means that 數值 可能為 0~99
		q_1 = n // 10**(k-1)
		if q_1 != 0 and q_1 > mx:    # 代表 n >= 10
			return q_1
		else:
			return mx
	else:
		q_2 = r // 10**(k-1)
		if q_2 > mx:
			mx = q_2
			return find_largest_digit_helper(n, mx, k)
		else:
			return find_largest_digit_helper(n, mx, k)



if __name__ == '__main__':
	main()
