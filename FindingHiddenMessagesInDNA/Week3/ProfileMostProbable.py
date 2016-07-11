def profile_most_probable(dna, k, matrix):
    p = 1
    pattern_dict = {}
    for i in range(len(dna) - k + 1):
        pattern = dna[i:i+k]
        for n in range(0, len(pattern)):
            if pattern[n] == 'A':
                p *= float(matrix[0][n])
            elif pattern[n] == 'C':
                p *= float(matrix[1][n])
            elif pattern[n] == 'G':
                p *= float(matrix[2][n])
            else:
                p *= float(matrix[3][n])
        pattern_dict[pattern] = p
        p = 1

    return max(pattern_dict, key=pattern_dict.get)

if __name__ == '__main__':
    file = open('..\Files\ProfileMostProbable.txt', 'r')
    string = file.readline()
    kSize = int(file.readline())
    MatrixProfile = []

    for line in file:
        MatrixProfile.append(line.strip().split('\t'))

    print(profile_most_probable(string, kSize, MatrixProfile))
    file.close()
