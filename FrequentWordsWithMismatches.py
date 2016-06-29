import ApproximatePatternCount as apc
import Neighbors
import FrequencyArray


def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = []
    close = {}
    frequency_array = {}
    for i in range(0, ((k ** 4) - 1)):
        close[i] = 0
        frequency_array[i] = 0

    for i in range(0, (len(text) - k)):
        neighborhood = Neighbors.neighbors(text[i:i+k], d)
        for string in neighborhood:
            index = FrequencyArray.pattern_to_number(string)
            close[index] = 1

    for i in range(0, len(close)):
        if close[i] == 1:
            pattern = FrequencyArray.number_to_pattern(i, k)
            frequency_array[i] = apc.approximate_pattern_count(pattern, text, d)

    max_count = max(frequency_array.values())

    for i in range(0, len(close)):
        if frequency_array[i] == max_count:
            pattern = FrequencyArray.number_to_pattern(i, k)
            frequent_patterns.append(pattern)

    return frequent_patterns

if __name__ == "__main__":
    file = open('Files/FrequentWordsWithMismatches.txt', 'r')
    print(frequent_words_with_mismatches(file.readline().strip(), int(file.readline().strip()), int(file.readline().strip())))
    file.close()
