import FindingHiddenMessagesInDNA.Week2.Neighbors as neighbors
import FindingHiddenMessagesInDNA.Week2.ApproximatePatternCount as apc


def motif_enumeration(dna, k, d):
    patterns = []
    neighborhood = []

    for string in dna:
        for i in range(0, len(string) - (k - 1)):
            pattern = string[i: i+k]
            neighborhood += neighbors.neighbors(pattern, d)

    neighborhood = list(set(neighborhood))

    for i in neighborhood:
        count = 0
        for j in dna:
            if apc.approximate_pattern_count(i, j, d) > 0:
                count += 1

        if count >= len(dna):
            patterns.append(i)

    return patterns


if __name__ == '__main__':
    file = open('../Files/MotifEnumeration.txt', 'r')
    lines = file.read().splitlines()
    K, D = lines[0].split(' ', 1)

    result = motif_enumeration(lines[1:], int(K), int(D))
    print(' '.join(sorted(result)))

    file.close()
