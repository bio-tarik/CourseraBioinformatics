def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1

    return count

if __name__ == "__main__":
    dnaSequence = open('../Files/PatternCount.txt', 'r')

    result = pattern_count(dnaSequence.readline(), dnaSequence.readline())
    print(result)

    dnaSequence.close()
