import math
import string

def decipher(N, L, cipher):
    factorizations = []
    all_primes = set()
    mapping = {}
    for number in cipher:
        factorization = prime_factorization(number)
        # if len(factorization) == 2:
        factorizations.append(factorization)

        for n in factorization:
            all_primes.add(n)
    all_primes = sorted(list(all_primes))

    for i, c in enumerate(string.ascii_uppercase):
        mapping[all_primes[i]] = c
    
    if len(all_primes) != len(mapping):
        return "abc"

    # Add first letter
    deciphered_text = [mapping[factorizations[0][0]]]

    for i in range(1, len(factorizations)):
        current_fact = factorizations[i]

        if current_fact[0] in factorizations[i - 1]:
            letter = mapping[current_fact[0]]
        else:
            letter = mapping[current_fact[1]]
        deciphered_text.append(letter)

    # Add last letter
    last_letter = ""
    last_factorization = factorizations[-1]
    second_last_fact = factorizations[-2]

    if last_factorization[0] not in second_last_fact:
        last_letter = mapping[last_factorization[0]]
        pass
    else:
        last_letter = mapping[last_factorization[1]]
        pass
    deciphered_text.append(last_letter)

    res = ''.join(deciphered_text)
    return res


def prime_factorization(n):
    # Print the number of two's that divide n 
    prime_factors = []
    while n % 2 == 0: 
        prime_factors.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prime_factors.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prime_factors.append(n)
    return sorted(prime_factors)

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N, L = input().split()
    N = int(N)
    L = int(L)
    cipher = input().split()
    cipher = list(map(int, cipher))

    res = decipher(N, L, cipher)
    print("Case #{}: {}".format(i, res))

# def main():
#     N, L = 103, 31
#     cipher = "217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053"

#     # N, L = 10000, 25
#     # cipher = "3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543"

#     cipher = cipher.split()
#     cipher = list(map(int, cipher))
#     print(decipher(N, L, cipher))

# if __name__ == "__main__":
#     main()
    
    