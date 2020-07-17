"""By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def main():
    soma, a, b = 0, 0, 1

    controle = 4000000

    while a <= controle:
        if a % 2:
            soma = soma + a
        print(a, end=",\n")  # Evita a nova linha após a saída
        a, b = b, a + b
    print("")
    print(f"Soma dos pares da sequência: {soma}")


main()
