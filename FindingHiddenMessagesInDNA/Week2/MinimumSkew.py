import FindingHiddenMessagesInDNA.Week1.ReverseComplement as ReverseComplement


def skew(string, positive_skew):
    negative_skew = ReverseComplement.return_complement(positive_skew)
    skew_dict = {0: 0}

    for i in range(0, len(string)):
        skew_rate = int(skew_dict[i])

        if string[i] == positive_skew:
            skew_rate += 1
        elif string[i] == negative_skew:
            skew_rate -= 1

        skew_dict.update({i + 1: skew_rate})

    return ' '.join(str(key) for min_value in (min(skew_dict.values()),) for key in skew_dict if skew_dict[key]==min_value)

if __name__ == "__main__":
    file = open('..\Files\MinimumSkew.txt', 'r')

    genome = file.readline().strip()

    # genome += genome

    print(skew(genome, file.readline()))

    file.close()
