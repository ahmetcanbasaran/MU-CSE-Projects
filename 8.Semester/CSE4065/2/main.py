import os
import random
from array import *


# To read input file
def read_file(file_name):
    genome = open(os.getcwd() + "/" + file_name, 'r').read()
    return genome


# To generate a random 10-mer
def random_10mer_generate():
    rand_10_mer = ""
    for i in range(10):
        rand = random.randint(0,3)
        if(rand == 0):      rand_10_mer = rand_10_mer + "A"
        elif(rand == 1):    rand_10_mer = rand_10_mer + "T"
        elif(rand == 2):    rand_10_mer = rand_10_mer + "G"
        else:               rand_10_mer = rand_10_mer + "C"
    return rand_10_mer


# To produce 10 different 10-mers with 4 mutation
def mutate(random_10mer):
    mutated_10mers = []
    for i in range(10):
        new_10_mer = random_10mer
        r_pos = random.sample(range(0, 10), 4)  # To generate random positions
        for i in range(4):
            letter = new_10_mer[r_pos[i]]  # To get base letter and change it to another base letter
            rand = random.randint(0,3)
            if(letter == "A"):  # If base letter is "A", change it to "T" or "G" or "C" randomly
                if(rand == 0):      new_10_mer = new_10_mer[:r_pos[i]] + "T" + new_10_mer[r_pos[i]+1:]
                elif(rand == 1):    new_10_mer = new_10_mer[:r_pos[i]] + "G" + new_10_mer[r_pos[i]+1:]
                else:               new_10_mer = new_10_mer[:r_pos[i]] + "C" + new_10_mer[r_pos[i]+1:]
            elif (letter == "T"):
                if(rand == 0):      new_10_mer = new_10_mer[:r_pos[i]] + "A" + new_10_mer[r_pos[i]+1:]
                elif(rand == 1):    new_10_mer = new_10_mer[:r_pos[i]] + "G" + new_10_mer[r_pos[i]+1:]
                else:               new_10_mer = new_10_mer[:r_pos[i]] + "C" + new_10_mer[r_pos[i]+1:]
            elif (letter == "G"):
                if(rand == 0):      new_10_mer = new_10_mer[:r_pos[i]] + "A" + new_10_mer[r_pos[i]+1:]
                elif(rand == 1):    new_10_mer = new_10_mer[:r_pos[i]] + "T" + new_10_mer[r_pos[i]+1:]
                else:               new_10_mer = new_10_mer[:r_pos[i]] + "C" + new_10_mer[r_pos[i]+1:]
            else:
                if(rand == 0):      new_10_mer = new_10_mer[:r_pos[i]] + "A" + new_10_mer[r_pos[i]+1:]
                elif(rand == 1):    new_10_mer = new_10_mer[:r_pos[i]] + "T" + new_10_mer[r_pos[i]+1:]
                else:               new_10_mer = new_10_mer[:r_pos[i]] + "G" + new_10_mer[r_pos[i]+1:]
        mutated_10mers.append(new_10_mer)
    return mutated_10mers


# To insert 10 different 10-mers with mutation 4 into DNA strings
def insert(dna_strings, mutated_10mers):
    for i in range(10):
        rand = random.randint(0,490)
        dna_strings[i] = dna_strings[i][:rand] + mutated_10mers[i] + dna_strings[i][rand+10:]


# To get 10 randomly choosen k-mers from DNA strings
def randomly_choose(dna_strings, k):
    rand_choosen_kmers = []
    for i in range(10):
        rand = random.randint(0,490)
        rand_choosen_kmers.append(dna_strings[i][rand:rand+k])
    return rand_choosen_kmers


# To produce profile matrix of motifs
def construct_profile(motifs, k):
    width, height = k, 4
    profile = [[0 for x in range(width)] for y in range(height)]  # Empty profile matrix
    for i in range(k):
        counter_A, counter_T, counter_G, counter_C = 0, 0, 0, 0
        for j in range(10):
            if   (motifs[j][i] == "A"):     counter_A = counter_A + 1
            elif (motifs[j][i] == "T"):     counter_T = counter_T + 1
            elif (motifs[j][i] == "G"):     counter_G = counter_G + 1
            else:                           counter_C = counter_C + 1
        profile[0][i] = counter_A / 10.0
        profile[1][i] = counter_T / 10.0
        profile[2][i] = counter_G / 10.0
        profile[3][i] = counter_C / 10.0
    return profile


# To compute occurence probability of each different k-mers in DNA strings and produce probability matrix
def compute_prob(dna_strings, k, profile):
    width, height = 500-k+1, 10
    probability = [[0 for x in range(width)] for y in range(height)]  # Empty probability matrix
    for i in range(10):
        for j in range(width):
            k_mer = dna_strings[i][j:j+k]
            prob = 1.0
            for m in range(k):
                if   (k_mer[m] == "A"):     prob = prob * profile[0][m]
                elif (k_mer[m] == "T"):     prob = prob * profile[1][m]
                elif (k_mer[m] == "G"):     prob = prob * profile[2][m]
                else:                       prob = prob * profile[3][m]
            probability[i][j] = prob
    return probability


# To compute score of the motifs
def compute_score(motifs, k):
    score = 0
    for i in range(k):
        count_A, count_T, count_G, count_C = 0, 0, 0, 0
        for j in range(10):
            if(motifs[j][i] == "A"):        count_A = count_A + 1
            if(motifs[j][i] == "T"):        count_T = count_T + 1
            if(motifs[j][i] == "G"):        count_G = count_G + 1
            if(motifs[j][i] == "C"):        count_C = count_C + 1
        if(count_A >= count_T and count_A >= count_G and count_A >= count_C):
            score = score + count_T + count_G + count_C
        elif(count_T >= count_A and count_T >= count_G and count_T >= count_C):
            score = score + count_A + count_G + count_C
        elif(count_G >= count_A and count_G >= count_T and count_G >= count_C):
            score = score + count_A + count_T + count_C
        else:
            score = score + count_A + count_T + count_G
    return score


# To produce 10 new k-mers from DNA strings with taking most probable k-mers with using probability matrix
def construct_random_motifs(dna_strings, probability, k):
    new_motifs = []
    for i in range(10):
        highest_prob = 0
        index = 0
        for j in range(500-k+1):
            if(probability[i][j] > highest_prob):
                highest_prob = probability[i][j]
                index = j
        new_motifs.append(dna_strings[i][index:index+k])
    return new_motifs


# To produce only 1 k-mers changed motifs with taking most probable k-mer from a
# randomly choosen DNA string with using probability matrix
def construct_gibbs_motifs(dna_strings, motifs, probability, k):
    new_motif = ""
    rand = random.sample(range(0, 10), 1)[0]
    highest_prob = 0
    index = 0
    for i in range(500-k+1):
        if(probability[rand][i] > highest_prob):
            highest_prob = probability[rand][i]
            index = i
    new_motif = dna_strings[rand][index:index+k]
    motifs[rand] = new_motif
    return motifs


# To produce consensus string from
def find_consensus(profile, k):
    consensus_string = ""
    for i in range(k):
        count_A = profile[0][i]
        count_T = profile[1][i]
        count_G = profile[2][i]
        count_C = profile[3][i]
        if(count_A >= count_T and count_A >= count_G and count_A >= count_C):
            consensus_string = consensus_string + "A"
        elif(count_T >= count_A and count_T >= count_G and count_T >= count_C):
            consensus_string = consensus_string + "T"
        elif(count_G >= count_A and count_G >= count_T and count_G >= count_C):
            consensus_string = consensus_string + "G"
        else:
            consensus_string = consensus_string + "C"
    return consensus_string


# To run Randomized Motif Search Algorithm
def randomized_motif_search(dna_strings, k):
    RMS_ITERATION = 100  # To iterate the algorithm 100 times
    motifs = randomly_choose(dna_strings, k)  # To get randomly produced motifs
    for i in range(RMS_ITERATION):
        profile = construct_profile(motifs, k)  # To construct profile matrix of motifs
        probability = compute_prob(dna_strings, k, profile)  # To calculate occurence probability of all k-mers in DNA strings
        motifs = construct_random_motifs(dna_strings, probability, k)  # To construct new motifs with using profile matrix
    score = compute_score(motifs, k)  # To calculate score of the motifs
    return find_consensus(profile, k), score


# To run Gibbs Sampler Algorithm
def gibbs_sampler(dna_strings, k):
    count_50 = 0
    motifs = randomly_choose(dna_strings, k)  # To get randomly produced motifs
    old_score = compute_score(motifs, k)  # To calculate score of the motifs
    while(count_50 != 50):
        profile = construct_profile(motifs, k)  # To construct profile matrix of motifs
        probability = compute_prob(dna_strings, k, profile)  # To calculate occurence probability of all k-mers in DNA strings
        motifs = construct_gibbs_motifs(dna_strings, motifs, probability, k)  # To construct new motifs with using profile matrix
        new_score = compute_score(motifs, k)  # To calculate score of the motifs
        if (old_score == new_score):    count_50 = count_50 + 1
        else:                           count_50 = 0
        old_score = new_score
    return find_consensus(profile, k), old_score


# Main function
def main():
    input = raw_input("Enter k, and file name, respectively: ")
    input = input.split()
    k = int(input[0], 10) # Convert obtained string to integer in base 10
    file_name = input[1]
    dna_strings = read_file(file_name)      # To read DNA strings from read_file
    dna_strings = dna_strings.splitlines()  # To split whole strings to 10 lines
    random_10mer = random_10mer_generate()  # To generate a 10-mer random pattern
    mutated_10mers = mutate(random_10mer)   # To generate mutated 10 10-mers
    insert(dna_strings, mutated_10mers)     # To insert mutated 10-mers into DNA strings

    print "\n\nRandomized Motif Search has began!\n"
    # To run randomized motif search algorithm
    result_randomized = randomized_motif_search(dna_strings, k)
    # To get consensus string and score of last motifs from returned list
    consensus_randomized, score_randomized = result_randomized[0], result_randomized[1]
    print "Consensus string is: ", consensus_randomized, " with score ", score_randomized
    print "\n\n------------------------------------------------\n\n"

    print "Gibbs sampler has began!\n"
    # To run Gibbs Sampler Algorithm
    result_gibbs = gibbs_sampler(dna_strings, k)
    # To get consensus string and score of last motifs from returned list
    consensus_gibbs, score_gibbs = result_gibbs[0], result_gibbs[1]
    print "Consensus string is: ", consensus_gibbs, " with score ", score_gibbs, "\n\n"


if __name__ == '__main__':
    main()
