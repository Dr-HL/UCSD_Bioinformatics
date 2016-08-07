"""
For a given choice of Motifs, we can construct a 4 x k (k-mer length) count matrix,
called Count(Motifs), counting the number of occurrences of each nucleotide in each
column of the motif matrix

element (i,j) of Count(Motifs) stores the number of times that nucleotide i (A G C or T)
appears in column j of Motifs
"""
def Count(Motifs):
    # initializing the count dictionary
    count = {}
    # all motifs will have the same string length
    k = len(Motifs[0])
    # for each letter
    for symbol in "ACGT":
        # each key in the dictionary ("A", "C", "G", "T") will store a list
        count[symbol] = []
        # loop through each letter within the motif string
        for j in range(k):
            # create a placeholder for count
            count[symbol].append(0)
    # number of motifs in input matrix
    t = len(Motifs)
    # for each motif
    for i in range(t):
        # for each letter in motif
        for j in range(k):
            # save the current letter into a variable
            symbol = Motifs[i][j]
            # add to total in count dictionary[current letter][char in motif]
            count[symbol][j] += 1
    return count

motif1 = "AACGTA"
motif2 = "CCCGTT"
motif3 = "CACCTT"
motif4 = "GGATTA"
motif5 = "TTCCGG"

# print(Count(motifs))

"""
determine the frequency of a nucleotide to occur at a certain index within a motif
in count we determined the count of each letter within a column
now we divide the count by the number of motifs that were initially inputted
"""
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for key, motif_lists in sorted(count.items()):
        profile[key] = motif_lists
        for motif_list, number in enumerate(motif_lists):
            motif_lists[motif_list] = number/t
    return profile

# motif1 = "AACGTA"
# motif2 = "CCCGTT"
# motif3 = "CACCTT"
# motif4 = "GGATTA"
# motif5 = "TTCCGG"
# motifs = [motif1, motif2, motif3, motif4, motif5]

#print(Profile(motifs))

"""
The letter that occurs most often in the matrix column will be deemed the consensus letter
The consensus letter for each column will form the consensus string
"""

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    profile = Profile(Motifs)
    consensus = ""
    for j in range(k):
        maximum = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > maximum:
                maximum = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

# profile = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#            'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#            'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#            'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}


# profile = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
#            'T': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
#            'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
#            'C': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
# text = "ACGGGGATTACC"

#print(Consensus(motifs))

"""
Loop through each letter in each motif, and if the letter does not match the
consensus string, add to score count
"""
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    count = 0
    consensus = Consensus(Motifs)
    for motif in Motifs:
        for index, letter in enumerate(motif):
            if letter != consensus[index]:
                count += 1
    return count

# motif1 = "AACGTA"
# motif2 = "CCCGTT"
# motif3 = "CACCTT"
# motif4 = "GGATTA"
# motif5 = "TTCCGG"
# motifs = [motif1, motif2, motif3, motif4, motif5]
#
# print(Score(motifs))

"""
The probability that a profile matrix will produce a given string is given by
the product of individual nucleotide probabilities.
"""
# Input:  String Text and profile matrix Profile
# Output: Probability value
def Pr(Text, Profile):
    p = 1
    # loop through each index(char) in text
    for index,char in enumerate(Text):
        for key, profile_lists in sorted(Profile.items()):
            if char == key:
                p *= profile_lists[index]
    return p

# profile = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#            'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#            'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#            'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
# text = "CAGTGA"
#
# print(Pr(text, profile))

"""
Check the probability of each k-mer in the DNA string.  Return the k-mer with the
great probability.
"""

# Input:  String Text, an integer k, and profile matrix Profile
# Output: String of most probable pattern
def ProfileMostProbablePattern(Text, k, Profile):
    n = len(Text)
    maximum = -1
    probable_pattern = ''
    for i, letter in enumerate(Text):
        for i in range(n-k+1):
            pattern = Text[i:i+k]
            probability = Pr(pattern,Profile)
            if (probability > maximum):
                maximum = probability
                probable_pattern = pattern
    if maximum == -1:
        return Text[0:0+k]
    else:
        return probable_pattern

# k = 6
# profile = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#            'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#            'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#            'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
# text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
#
# print(ProfileMostProbablePattern(text, k, profile))

"""
A greedy algorithm will make the locally optimal choice at each step with the
hopes of finding a global optimum.

Applying a greedy algorithm in chess would mean attacking the most valuable
unfriendly piece at each turn, which is not an ideal method for actually winning
the game.

GreedyMotifSearch will return the motifs with the highest scores.
"""
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    # search through DNA string
    for i in range(0, t):
        # starts by setting BestMotifs equal to the first k-mer from each string in Dna
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    # ranges over all possible k-mers in Dna[0], trying each one as Motifs[0]
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            # builds a profile matrix Profile for this lone k-mer, and sets Motifs[1] equal to the Profile-most probable k-mer in Dna[1]
            P = Profile(Motifs[0:j])
            # sets Motifs[i] equal to the Profile-most probable k-mer from Dna[i] based on this profile matrix
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        # GreedyMotifSearch checks whether Motifs outscores the current best scoring collection of motifs, BestMotifs
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# k = 3
# t = 5
# Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
# print(GreedyMotifSearch(Dna, k, t))
