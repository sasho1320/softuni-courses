from itertools import permutations


def possible_permutations(elements: list):
    for perm in permutations(elements):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]
