def symbol_to_number(s):
    s.isnumeric()
    symbols = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return symbols[s.upper()]


def number_to_symbol(n):
    symbols = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return symbols[n]


def pattern_to_number(pattern):
    if pattern == '':
        return 0

    symbol = pattern[-1]
    prefix = pattern[0:len(pattern) - 1]
    return 4*pattern_to_number(prefix) + symbol_to_number(symbol)


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = int(index/4)
    r = index % 4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k-1)
    return prefix_pattern + symbol


def computing_frequencies(text, k):
    frequency = []
    for i in range(4**k):
        frequency.append(0)

    for i in range(0, len(text) - (k-1)):
        pattern = text[i: i+k]
        number = pattern_to_number(pattern)
        frequency[number] += 1

    return frequency

if __name__ == "__main__":
    file = open('Files\FrequencyArray.txt', 'r')
    print(computing_frequencies(file.readline().strip(), int(file.readline())))
    file.close()
