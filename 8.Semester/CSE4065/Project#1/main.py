#   CSE4062 - Introduction to Computational Genomics, Project#1
#
#   This programs reads an input file and finds k-mers appeared at least x times
#   and checks how many times appeared reverse complement of the k-mers founded
#   with obtaining desired 'k'-mers and 'x' itmes at least

import os  # To read input.txt

# To read input from file
def read_file(file_name):
    genome = open(os.getcwd() + "/" + file_name, 'r').read()
    return genome


# To find 'k'-mers which appear at least 'x' times in 'genome'
def search(k, x, genome):
    genome_length = len(genome)
    mers = []
    for i in range (genome_length - k):
        pattern = genome[i:i+k]
        counter = 0
        j = i
        while j < genome_length - k:
            if pattern == genome[j:j+k]:
                counter += 1
            j += 1
        if (counter >= x):
            mers.append(pattern)  # We found a k-mers, added to list
    return mers


# To find reversed complement of founded 'k'-mers which
# appeared at least 'x' times in 'genome'
def reverse_search(mers, genome, k):
    rev_comp_mers = []
    rev_comp_mers_counters = []  # To keep counting of rev.comp. k-mers
    genome_length = len(genome)
    for pattern in mers:
        rev_comp = reverse_complement(pattern)
        rev_comp_mers.append(rev_comp)
        counter = 0
        for i in range(genome_length - k):
            if rev_comp == genome[i:i+k]:
                counter += 1
        rev_comp_mers_counters.append(counter)
    result = "Reverse complement: "
    for i in range(len(rev_comp_mers) - 1):
        result += rev_comp_mers[i] + " appearing " + str(rev_comp_mers_counters[i]) + " times, "
    result += rev_comp_mers[len(rev_comp_mers) - 1] + " appearing " + str(rev_comp_mers_counters[len(rev_comp_mers) - 1]) + " times."
    print result


# To generate reverse complement of the pattern
def reverse_complement(pattern):
    reverse = pattern[::-1]
    reverse_complement = "x" * len(reverse)  # To generate a string with same length as reverse
    length = len(reverse)
    # To check whether pattern chars are uppercase or lowercase
    if(reverse[0] == 'A' or reverse[0] == 'T' or
       reverse[0] == 'C' or reverse[0] == 'G'):
        uppercase = 1;
    else:
        uppercase = 0;
    if(uppercase):  # To return reverse complement as uppercase
        for i in range(length):
            if(reverse[i] == 'A'):
                reverse_complement = reverse_complement[:i] + 'T' + reverse_complement[i+1:]
            elif(reverse[i] == 'T'):
                reverse_complement = reverse_complement[:i] + 'A' + reverse_complement[i+1:]
            elif(reverse[i] == 'G'):
                reverse_complement = reverse_complement[:i] + 'C' + reverse_complement[i+1:]
            elif(reverse[i] == 'C'):
                reverse_complement = reverse_complement[:i] + 'G' + reverse_complement[i+1:]
    else:   # To return reverse complement as lowercase
        for i in range(length):
            if(reverse[i] == 'a'):
                reverse_complement = reverse_complement[:i] + 't' + reverse_complement[i+1:]
            elif(reverse[i] == 't'):
                reverse_complement = reverse_complement[:i] + 'a' + reverse_complement[i+1:]
            elif(reverse[i] == 'g'):
                reverse_complement = reverse_complement[:i] + 'c' + reverse_complement[i+1:]
            elif(reverse[i] == 'c'):
                reverse_complement = reverse_complement[:i] + 'g' + reverse_complement[i+1:]
    return reverse_complement


# Main program
def main():
    input = raw_input("Enter k, x, and file name, respectively: ")
    input = input.split()
    k = int(input[0], 10) # Convert obtained string to integer in base 10
    x = int(input[1], 10)
    file_name = input[2]
    genome = read_file(file_name)
    mers = search(k, x, genome)
    print_mers = str(k) + "-mer: "  # 9-mers for example if k = 9
    if (len(mers) > 0):
        for i in range(len(mers) - 1):
            print_mers += mers[i] + ", "
        print_mers += mers[len(mers) - 1]
        print print_mers  # Print k-mers appeared at least x times
        reverse_search(mers, genome, k) # To print rev. comp. result
    else:
        print print_mers + "-"
        print "Reverse complement: -"


if __name__ == '__main__':
    main()
