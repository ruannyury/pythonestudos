# def - define uma função
def fib(n):  # Write Fibonacci series up to 'n'
    """
    Print a Fibonacci series up to n.

    More paragraphs for documentation
    :param n:
    :return:
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Ou
def fib2(n):  # Return Fibonacci series up to 'n'
    """
    Return a list the Fibonacci series up to 'n'

    More paragraphs for documentation
    :param n:
    :return:
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # See below
        a, b = b, a + b
    return result


fib(2000)  # Chama a função

fib2(1000)  # Chama a outra função


# Argumentos com valor padrão
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):  # Verifica se uma sequência contém ou não um determinado valor
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


ask_ok('Do you really want to quit?')


# ask_ok('Do you really want to quit?', 2)
# ask_ok('Do you really want to quit?', 2, 'Come on, only yes or no!')


# Acumula os argumentos passados, nas chamadas subsequentes:
# def f(a, lista=[]):  # Default value mutable
#     lista.append(a)
#     return lista

# Para não acumular:
def f1(a, lista=None):
    if lista is None:
        lista = []
    lista.append(a)
    return lista


# print(f(1))  # [1]
# print(f(2))  # [1][2]
# print(f(3))  # [1][2][3]
print(f1(1))  # [1]
print(f1(2))  # [2]
print(f1(3))  # [3]


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("If you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# Mas todas as formas a seguir seriam inválidas:
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead)   # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# *args permite passar um número indeterminado de parametros para uma função
# **kwdargs - número indeterminado de parâmetros nomeados
def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, '?')
    print('-- I\'m, sorry, we\'re all out off', kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ':', keywords[kw])


cheeseshop('Limburger', 'It\'s very runny, sir',
           'It\'s really very, VERY runny, sir.',
           shopkeeper='Michael Palin',
           client='John Cleese',
           sketch='Cheese Shop Sketch')


def standard_arg(arg):  # Argumentos passados por posição ou nome
    print(arg)


def pos_only_arg(arg, /):  # Apenas argumentos posicionais
    print(arg)


def kwd_only_arg(*, arg):  # Apenas números nomeados
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)  # Argumentos passados por posição ou nome
standard_arg(arg=2)
pos_only_arg(1)  # Apenas argumentos posicionais
# pos_only_arg(arg=1) Dará erro
# kwd_only_arg(3) Dará erro pois aceita apenas argumentos nomeados
kwd_only_arg(arg=3)
# combined_example(1, 2, 3) Dará erro também
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) Dará erro
"""
def foo(name, **kwds):
    return 'name' in kwds  # A chave 'name' sempre será aplicada para o primeiro parâmetro


foo(1, **{'name': 2})
"""


def foo(name, /, **kwds):
    return 'name' in kwds


print(foo(1, **{'name': 2}))


def write_multiple_items(file, separator, *arg):
    file.write(separator.join(arg))


def concat(*arg, sep="/"):
    return sep.join(arg)


list(range(3, 6))  # [3, 4, 5] - normal call with separate arguments
args = [3, 6]  # Argumentos já estão numa lista ou tupla
list(range(*args))  # [3, 4, 5] - call with arguments unpacked from a list


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)  # A variável "vira" uma função
print(f(0))
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# soma2Numeros = lambda x, y: x + y  ===  Não está de acordo com o PEP8
# soma3Numeros = lambda x, y, z: x + y + z  ===  Não está de acordo com o PEP8
def soma_dupla(y):
    return lambda x: x + y


def soma_tripla(y, z):
    return lambda x: x + y + z


soma2Numeros = soma_dupla(3)
soma3Numeros = soma_tripla(3, 5)
print(f"""
        Soma de 2 + 3 = {soma2Numeros(2)}
        Soma de 2 + 3 + 5 = {soma3Numeros(2)}
""")
