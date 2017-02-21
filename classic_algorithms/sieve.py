###############################################################################################
# Sieve of Eratosthenes - The sieve of Eratosthenes is one of the most efficient ways to find #
# all of the smaller primes (below 10 million or so).                                         #
###############################################################################################

input = int(raw_input("type an integer:  "))
list = range(2, input + 1)
for i in list:
    for j in list:
        if j != i and j % i == 0:
            list.remove(j)
print list
