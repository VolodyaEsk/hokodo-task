hint = [
    ['t', 'c', 'k', 's', 'x', 'f', 'b', 'r', 'a', 'v', 'h', 'i', 'g', 'p', 'o'],
    ['t', 'c', 'l', 'u', 's', 'z', 'f', 'r', 'a', 'h', 'e', 'i', 'j', 'q', 'g'],
    ['w', 't', 'l', 'u', 'k', 's', 'n', 'f', 'm', 'a', 'v', 'h', 'i', 'g', 'p'],
    ['t', 'c', 'u', 's', 'z', 'm', 'r', 'a', 'y', 'v', 'h', 'e', 'q', 'g', 'p'],
    ['w', 'c', 'l', 'u', 's', 'f', 'b', 'm', 'y', 'v', 'h', 'i', 'q', 'g', 'o'],
    ['w', 't', 'c', 'k', 'f', 'b', 'm', 'r', 'h', 'e', 'i', 'j', 'q', 'g', 'o'],
    ['w', 't', 'c', 'u', 'k', 's', 'z', 'x', 'b', 'm', 'h', 'e', 'i', 'g', 'p'],
    ['w', 't', 'c', 'k', 's', 'n', 'b', 'm', 'r', 'v', 'h', 'j', 'q', 'p', 'o'],
    ['w', 't', 'c', 'u', 's', 'z', 'f', 'b', 'm', 'a', 'y', 'e', 'q', 'g', 'o'],
    ['c', 'l', 'u', 'k', 's', 'z', 'n', 'f', 'b', 'r', 'a', 'y', 'v', 'e', 'i'],
    ['t', 'c', 'l', 'k', 's', 'z', 'f', 'b', 'm', 'r', 'a', 'e', 'i', 'g', 'p'],
    ['w', 'c', 'l', 'u', 'k', 's', 'x', 'n', 'f', 'b', 'a', 'y', 'i', 'j', 'q'],
    ['w', 't', 'u', 'z', 'x', 'n', 'f', 'a', 'y', 'e', 'i', 'q', 'g', 'p', 'o'],
    ['w', 't', 'u', 'k', 'z', 'x', 'n', 'b', 'r', 'y', 'h', 'j', 'q', 'g', 'o'],
    ['w', 't', 'c', 'l', 'u', 'k', 'n', 'a', 'y', 'h', 'e', 'j', 'q', 'p', 'o'],
]

hint2 = [['d', 'b'], ['b', 'c'], ['a', 'd']]
hint3 = [['a', 'b'], ['b', 'c'], ['c', 'd']]


def get_new_alphabet(hint):
    new_alphabet = hint.pop(0)

    for order in hint:
        for index, letter in enumerate(order):
            if letter not in new_alphabet:
                if index == 0:
                    new_alphabet.insert(index, letter)
                else:
                    previous_index = index - 1
                    previous_letter = order[previous_index]
                    index_to_insert = new_alphabet.index(previous_letter) + 1
                    new_alphabet.insert(index_to_insert, letter)

    return new_alphabet


if __name__ == "__main__":
    print(get_new_alphabet(hint))
