import HammingDistance as HamDis


def suffix(pattern):
    return pattern[1:]


def first_symbol(pattern):
    return pattern[0:1]


def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return nucleotides

    neighborhood = []
    suffix_neighbors = neighbors(suffix(pattern), d)

    for text in suffix_neighbors:
        if HamDis.hamming_distance(suffix(pattern), text) < d:
            for n in nucleotides:
                neighborhood.append(n + text)
        else:
            neighborhood.append(first_symbol(pattern) + text)
    return neighborhood

if __name__ == '__main__':
    file = open('Files/Neighbors.txt', 'r')
    response = neighbors(file.readline().strip(), int(file.readline()))
    print(' '.join(response))
    file.close()
