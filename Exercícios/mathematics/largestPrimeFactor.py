# The prime factor of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
"""
def primo(numero):
    totaldivisores = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            totaldivisores += 1

    if totaldivisores == 2:
        return True
    else:
        return False


def main():
    number = 600851475143
    maiorfator = 0

    for contador in range(1, number + 1):
        verificar = primo(contador)
        if verificar:
            if number % contador == 0:
                maiorfator = contador

    print(f'The largest prime factor of the number {number} is {maiorfator}')


main()
"""


def max_prime_factor(n):
    """find the largest prime factor of integer n"""

    largest_factor = 1
    i = 2

    # i is a possible *smallest* factor of the (remaining) number n.
    # If i * i > n then n is either 1 or a prime number.
    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            # Divide by the highest possible power of the found factor:
            while n % i == 0:
                n //= i
        i = 3 if i == 2 else i + 2

    if n > 1:
        # n is a prime number and therefore the largest prime factor of the
        # original number.
        largest_factor = n

    return largest_factor


def main():
    factor = max_prime_factor(600851475143)
    print(factor)


main()
