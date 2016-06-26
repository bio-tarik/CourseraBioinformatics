import HammingDistance as HammingDistance


def approximate_pattern_matching(pattern, genome, d):
    indices = []
    stretch = ''
    for i in range(0, len(genome) - (len(pattern) - 1)):
        stretch = genome[i: i+len(pattern)]
        if HammingDistance.hamming_distance(pattern, stretch) <= d:
            indices.append(str(i))

    return indices

if __name__ == "__main__":
    file = open('Files\ApproximatePatternMatching.txt', 'r')
    print(approximate_pattern_matching(file.readline().strip(), file.readline().strip(), int(file.readline().strip())))
    file.close()
