def return_complement(source_string):
    complement_list = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    complementary_string = ''
    for i in range(0, len(source_string)):
        complementary_string += complement_list[source_string[i]]

    complementary_string = complementary_string[::-1]

    return complementary_string

if __name__ == "__main__":
    file = open('files/ReverseComplement.txt', 'r')

    dnaString = file.readline()

    print(return_complement(dnaString))
    file.close()