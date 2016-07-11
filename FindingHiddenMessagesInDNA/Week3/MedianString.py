import sys
import FindingHiddenMessagesInDNA.Week2.FrequencyArray as FreqArr
import FindingHiddenMessagesInDNA.Week3.DistanceBetweenPatternAndStrings as DisPat


def median_string(dna, k):
    distance = sys.maxsize
    median = None

    for i in range(0, (4 ** k) - 1):
        pattern = FreqArr.number_to_pattern(i, k)
        calculated_distance = DisPat.distance_between_pattern_and_strings(pattern, dna)
        if distance > calculated_distance:
            distance = calculated_distance
            median = pattern

    return median

if __name__ == '__main__':
    file = open('..\Files\MedianString.txt', 'r')
    kSize = int(file.readline())
    strings = []

    for line in file:
        strings.append(line.strip())

    print(median_string(strings, kSize))
    file.close()
