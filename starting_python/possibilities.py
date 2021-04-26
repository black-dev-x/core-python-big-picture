from math import factorial as f


def possibilities(n, k):
    return f(n) // f(k) * f(n-k)


number_of_items = 20
number_of_draws = 4

number_of_possibilities = possibilities(number_of_items, number_of_draws)
print(number_of_possibilities)
