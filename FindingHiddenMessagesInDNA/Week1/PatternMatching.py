def pattern_matching(pattern, genome):
    pattern_length = len(pattern)
    count = ''
    for i in range(0, len(genome) - pattern_length):
        if genome[i:i + pattern_length] == pattern:
            count += str(i) + ' '

    return count

file = open('../files/PatternMatching.txt', 'r')
print(pattern_matching(file.readline().strip(), file.readline().strip()))
file.close()
