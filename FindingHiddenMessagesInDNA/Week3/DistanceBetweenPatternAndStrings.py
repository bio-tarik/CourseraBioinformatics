import FindingHiddenMessagesInDNA.Week2.HammingDistance as HamDis


def distance_between_pattern_and_strings(dna_pattern, dna_strings):
    k = len(dna_pattern)
    distance = 0

    for dna in dna_strings:
        hamming_distance = k
        for i in range(0, len(dna) - k + 1):
            k_mer_pattern = dna[i:i+k]
            calculated_hamming_distance = HamDis.hamming_distance(dna_pattern, k_mer_pattern)
            if hamming_distance > calculated_hamming_distance:
                hamming_distance = calculated_hamming_distance
        distance += hamming_distance

    return distance


if __name__ == "__main__":
    file = open('..\Files\DistanceBetweenPatternAndStrings.txt', 'r')
    pattern = file.readline().strip()
    strings = file.readline().strip().split(' ')
    print(distance_between_pattern_and_strings(pattern, strings))
    file.close()
