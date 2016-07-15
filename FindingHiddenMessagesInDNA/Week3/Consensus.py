import FindingHiddenMessagesInDNA.Week2.FrequencyArray as FreqArr


def consensus(motifs):
    consensus_string = ''
    for i in range(0, len(motifs[0])):
        count = [0, 0, 0, 0]
        for motif in motifs:
            index = FreqArr.symbol_to_number(motif[i])
            count[index] += 1

        consensus_string += FreqArr.number_to_symbol(count.index(max(count)))
    return consensus_string

if __name__ == "__main__":
    file = open("..\Files\Consensus.txt", "r")
    strings = []

    for line in file:
        strings.append(line.strip())

    print(consensus(strings))
    file.close()
