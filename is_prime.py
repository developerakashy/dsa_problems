def isPrime(A):
	upperLimit = int(A**0.5)
	print(upperLimit)
	for i in range(2, upperLimit + 1):
		if A % i == 0:
			return 0
	return 1

A = 2

print(isPrime(A))
