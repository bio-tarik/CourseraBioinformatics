import FindingHiddenMessagesInDNA.Week3.Consensus as Con
import FindingHiddenMessagesInDNA.Week2.HammingDistance as HamDis


def motif_score(motifs):
    consensus = Con.consensus(motifs)
    score = 0
    for motif in motifs:
        score += HamDis.hamming_distance(consensus, motif)
    return score

if __name__ == "__main__":
    file = open("..\Files\MotifScore.txt", "r")
    strings = []

    for line in file:
        strings.append(line.strip())

    print(motif_score(strings))
    file.close()
