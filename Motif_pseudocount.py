import random

"""
The functions in Motif.py will return 0 for an entire motif probability even if only
one of the positions has a 0 probability of existing in the consensus string.

This doesn't make sense because a motif that differs from the consensus string
at every position will also get a total probability of 0.

In order to improve this unfair scoring, bioinformaticians often substitute zeroes
with small numbers called pseudocounts.
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

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # initializing the count dictionary
    count = {}
    # for each letter
    for symbol in "ACGT":
        # each key in the dictionary ("A", "C", "G", "T") will store a list
        count[symbol] = []
        # loop through each letter within the motif string
        for j in range(k):
            # create a placeholder for count
            count[symbol].append(1)
    # for each motif
    for i in range(t):
        # for each letter in motif
        for j in range(k):
            # save the current letter into a variable
            symbol = Motifs[i][j]
            # add to total in count dictionary[current letter][char in motif]
            count[symbol][j] += 1
    return count

"""
ProfileWithPseudocounts(Motifs) that takes a list of strings Motifs as input and
returns the profile matrix of Motifs with pseudocounts as a dictionary of lists
"""

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = CountWithPseudocounts(Motifs)
    for key, motif_lists in sorted(count.items()):
        profile[key] = motif_lists
        for motif_list, number in enumerate(motif_lists):
            motif_lists[motif_list] = number/(float(t+4))
    return profile

# motif1 = "AACGTA"
# motif2 = "CCCGTT"
# motif3 = "CACCTT"
# motif4 = "GGATTA"
# motif5 = "TTCCGG"
# motifs = [motif1, motif2, motif3, motif4, motif5]
#
# print(ProfileWithPseudocounts(motifs))

"""
 Write a function GreedyMotifSearchWithPseudocounts(Dna, k, t) that takes a list
 of strings Dna followed by integers k and t and returns the result of running
 GreedyMotifSearch, where each profile matrix is generated with pseudocounts
 """
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
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
            P = ProfileWithPseudocounts(Motifs[0:j])
            # sets Motifs[i] equal to the Profile-most probable k-mer from Dna[i] based on this profile matrix
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        # GreedyMotifSearch checks whether Motifs outscores the current best scoring collection of motifs, BestMotifs
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    profile = ProfileWithPseudocounts(Motifs)
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

# k = 3
# t = 5
# Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
# print(GreedyMotifSearchWithPseudocounts(Dna, k, t))

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Profile-most probable 4-mer from each row of Dna
def Motifs(Profile, Dnas):
    t = len(Dnas)
    n = len(Dnas[0])
    k = len(Profile['A'])
    probable_kmer = []
    for Dna in Dnas:
        probable_kmer.append(ProfileMostProbablePattern(Dna, k, Profile))
    return probable_kmer

# Profile = {'A': [0.8, 0.0, 0.0, 0.2],
#            'C': [0.0, 0.6, 0.2, 0.0],
#            'G': [0.2, 0.2, 0.8, 0.0],
#            'T': [0.0, 0.2, 0.0, 0.8]}
#
# Dnas = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
#
# print(Motifs(Profile, Dnas))

# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dnas, k, t):
    n = len(Dnas[0])
    random_motifs = []
    for dna in Dnas:
        random_start = random.randint(0,n-k)
        random_motifs.append(dna[random_start:random_start+k])
    return random_motifs

Dnas = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
k = 3
t = len(Dnas)
print(RandomMotifs(Dnas, k, t))
