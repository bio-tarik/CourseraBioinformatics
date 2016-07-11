import FindingHiddenMessagesInDNA.Week2.FrequencyArray as freqArray


def profile(motifs):
    motifs_profile = [[0 for x in range(len(motifs[0]))] for y in range(0, 4)]

    for col in range(0, len(motifs[0])):
        n_sum = float(0)
        for li in motifs:
            nucleotide = freqArray.pattern_to_number(li[col])
            n_sum += 1
            motifs_profile[nucleotide][col] += float(1)

        for n in range(0,4):
            motifs_profile[n][col] = motifs_profile[n][col]/n_sum

    return motifs_profile


if __name__ == '__main__':
    file = open('..\Files\MotifProfile.txt', 'r')
    strings = []

    for line in file:
        strings.append(line.strip())

    print(profile(strings))
    file.close()