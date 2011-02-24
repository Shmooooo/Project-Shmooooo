def factorial(n):
	n_ = n
	n = int(abs(n))
	f = 1
	for k in range(n):
		f *= k + 1
	if n_ != int(abs(n)):
		print n_, "is not a natural number! Using", int(abs(n)),"instead."
	return f
print factorial(-5.57)
