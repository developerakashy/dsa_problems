def sieve(A):
        prime_arr = []

        for i in range(2, A+1):
            upperLimit = int(i**0.5)
            isPrime = True
            for j in range(2, upperLimit+1):
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime:
                prime_arr.append(i)


        return prime_arr

print(sieve(19))
