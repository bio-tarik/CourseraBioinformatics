import PatternCount


def frequent_words(text, k):
    frequent_patterns = []
    count = []

    for i in range(0, len(text) - k):
        pattern = text[i:i+k]
        count.append(PatternCount.pattern_count(text, pattern))

    max_count = max(count)

    for i in range(0, len(text) - k):
        if count[i] == max_count:
            frequent_patterns.append(text[i:i+k])

    frequent_patterns = set(frequent_patterns)

    return frequent_patterns

if __name__ == "__main__":
    dnaSequence = open("Files/FrequentWords.txt", "r")

    result = frequent_words(dnaSequence.readline(), int(dnaSequence.readline()))

    print(result)
    dnaSequence.close()
