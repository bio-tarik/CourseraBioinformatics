import HammingDistance


def approximate_pattern_count(pattern, text, d):
    count = 0
    for i in range(0, len(text) - (len(pattern) - 1)):
        stretch = text[i: i + len(pattern)]
        if HammingDistance.hamming_distance(stretch, pattern) <= d:
            count += 1

    return count

if __name__ == "__main__":
    file = open("Files/ApproximatePatternCount.txt", "r")
    print(approximate_pattern_count(file.readline().strip(), file.readline().strip(), int(file.readline().strip())))
    file.close()
