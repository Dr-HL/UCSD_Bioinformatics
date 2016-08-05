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

motif1 = "AACGTA"
motif2 = "CCCGTT"
motif3 = "CACCTT"
motif4 = "GGATTA"
motif5 = "TTCCGG"
motifs = [motif1, motif2, motif3, motif4, motif5]

# print(Profile(motifs))

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

print(Consensus(motifs))

motif1 = "AACGTA"
motif2 = "CCCGTT"
motif3 = "CACCTT"
motif4 = "GGATTA"
motif5 = "TTCCGG"
motifs = [motif1, motif2, motif3, motif4, motif5]
