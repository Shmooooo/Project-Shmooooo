def factorial(n):
	from math import floor
	n = floor(abs(n))
	f = 1
	for k in range(n):
		f *= k + 1
	return f

print factorial(0), factorial(1), factorial(1.5), factorial(7)
