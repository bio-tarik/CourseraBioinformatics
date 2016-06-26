import FrequentWords as Frequent
import PatternCount as PatterCount
from collections import Counter

def clump_finder(genome, k, l, t):
    genome_split = [genome[i:i+l] for i in range(0, len(genome), l)]
    patterns = []
    counter = {}

    for i in range(0, len(genome_split)):
        patterns = patterns + list((Frequent.frequent_words(genome_split[i], k)))

    for i in patterns:
        patter_count = PatterCount.pattern_count(genome, i)
        if patter_count >= t:
            counter[i] = patter_count

    return counter


if __name__ == "__main__":
    file = open('files/ClumpFinding.txt', 'r')
    params = file.readline().strip().split(' ')
    result = clump_finder(file.readline().strip(), int(params[0]), int(params[1]), int(params[2]))

    print(result)

    file.close()
