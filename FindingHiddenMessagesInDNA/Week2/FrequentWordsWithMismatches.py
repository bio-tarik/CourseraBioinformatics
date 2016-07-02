import FindingHiddenMessagesInDNA.Week2.Neighbors as Neighbors
import FindingHiddenMessagesInDNA.Week1.ReverseComplement as ReverseComplement
import FindingHiddenMessagesInDNA.Week2.ApproximatePatternCount as ApproximatePatternCount


def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = []
    frequency_array = {}
    neighborhood = []

    for i in range(0, (len(text) - (k - 1))):
        neighborhood += Neighbors.neighbors(text[i:i + k], d)

    neighborhood += [ReverseComplement.return_complement(p) for p in neighborhood]

    neighborhood = list(set(neighborhood))

    for i in neighborhood:
        frequency_array[i] = ApproximatePatternCount.approximate_pattern_count(i, text, d) + ApproximatePatternCount.approximate_pattern_count(i, ReverseComplement.return_complement(text), d)

    max_count = max(frequency_array.values())

    for k, v in frequency_array.items():
        if v == max_count:
            frequent_patterns.append(k)

    return frequent_patterns

if __name__ == "__main__":
    file = open('../Files/FrequentWordsWithMismatches.txt', 'r')
    print(frequent_words_with_mismatches(file.readline().strip(), int(file.readline().strip()), int(file.readline().strip())))
    file.close()

