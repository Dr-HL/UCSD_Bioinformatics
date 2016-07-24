"""
We start sliding the window at position 0 of Text, but where should we stop?
In general, the final k-mer of a string of length n begins at position n-k;
for example, the final 3-mer of "GACCATACTG", which has length 10, begins at
position 10 - 3 = 7. This observation implies that the window should slide
between position 0 and position len(Text)-len(Pattern). We now have the desired
for loop, shown at bottom. Note that in Python, the statement

for i in range(n):

iterates over all values of i between 0 and n-1. Thus, in the code below,
i ranges up to len(Text)-len(Pattern)+1 in order to include position len(Text)-len(Pattern).

count = 0
 for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
"""

"""
input:    pattern - sequence of base pattern we are searching for
          ex: "GCGATCGCG"
          text- the full base sequence string
          ex: "GCG"
output:   the number of times Pattern appears in Text
          ex: 2
"""
def PatternCount(Pattern, Text):
    count = 0
    # determine index value we can stop checking for pattern (see explaination above)
    for i in range(len(Text)-len(Pattern)+1):
        # can access characters in text string Text[start index: up to but not including end index]
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


#Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
#Pattern = "AAA"
#print(PatternCount(Pattern, Text))
"""
input:    text- full base sequence string
          ex: "CGATATATCCATAG"
          k or k-mer is the length of pattern we are searching for (ex: 3-mer "ATA")
          ex: 3
output:   Count is a dictionary that stores results of PatternCount
          ex: {0: 1, 1: 1, 2: 3, 3: 2, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1, 10: 3, 11: 1}
"""
def CountDict(Text, k):
    Count = {}
    # same range as range(len(Text)-len(Pattern)+1) above because k == len(Pattern)
    for i in range(len(Text)-k+1):
        # flexible creation of pattern so we don't have to hardcode it directly into PatternCount
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

"""
input:    list- list returned from FrequentWords
output:   list with no duplicate FrequentWords
"""
def RemoveDuplicates(Items):
    ItemsNoDuplicates = []
    for i in Items:
        # append to new list if input item not in new list
        if i not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

"""
input:text- full base sequence string
      ex: "ACGTTGCATGTCGCATGATGCATGAGAGCT"
      k or k-mer is the length of pattern we are searching for (ex: 3-mer "ATA")
      ex: 4
output: list of frequent patterns
        ex: GCAT CATG GCAT CATG GCAT CATG

complexity of this algorithm as O(|Text|2 · k)
"""
def FrequentWords(Text, k):
    # initialize empty list
    FrequentPatterns = []
    # store Count dictionary that stores result of PatternCount (the number of a times a pattern appears in the text)
    Count = CountDict(Text, k)
    # Count.values() returns a list of all the values in the in Count dictionary
    # max(Count.values()) returns the maximum value in the Count dictionary
    m = max(Count.values())
    # loop through Count dictionary
    for i in Count:
        # if the number of times the pattern appears in text == max value
        if Count[i] == m:
            # push the text pattern string into the FrequentPatterns list
            FrequentPatterns.append(Text[i:i+k])
    # avoid duplicate frequent words
    FrequentPatternsNoDuplicates = RemoveDuplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

#Text="ACTTCCTAGCCTACCCAGCACTTCCTAGCCTACCCAGCTACGCGGTCACTTCCTAGCCACTGCTCCACTGCTCCACTGCTCAATGTCCACTACCCAGCAATGTCCACACTGCTCCTACCCAGCAATGTCCACTACCCAGCTACGCGGTCAATGTCCAACTTCCTAGCTACGCGGTCTACGCGGTCTACGCGGTCAATGTCCATACGCGGTCCTACCCAGCCACTGCTCCACTGCTCTACGCGGTCCTACCCAGCTACGCGGTCACTTCCTAGCCTACCCAGCTACGCGGTCCTACCCAGCACTTCCTAGCTACGCGGTCCTACCCAGCTACGCGGTCAATGTCCACTACCCAGCTACGCGGTCTACGCGGTCCTACCCAGCCACTGCTCCTACCCAGCCTACCCAGCACTTCCTAGCACTTCCTAGCACTTCCTAGCCACTGCTCCTACCCAGCACTTCCTAGCTACGCGGTCAATGTCCACACTGCTCTACGCGGTCTACGCGGTCCTACCCAGCTACGCGGTCACTTCCTAGCCTACCCAGCACTTCCTAGCCACTGCTCCACTGCTCTACGCGGTCTACGCGGTCAATGTCCAACTTCCTAGCACTTCCTAGCCTACCCAGCACTTCCTAGCTACGCGGTCTACGCGGTCAATGTCCAACTTCCTAGCCACTGCTCTACGCGGTCACTTCCTAGCACTTCCTAGCAATGTCCACTACCCAGCTACGCGGTCCTACCCAGCCACTGCTCCACTGCTCCTACCCAGCAATGTCCAAATGTCCAACTTCCTAGCAATGTCCATACGCGGTCCACTGCTCAATGTCCATACGCGGTCAATGTCCATACGCGGTCAATGTCCACACTGCTCCTACCCAGCAATGTCCAAATGTCCACACTGCTCTACGCGGTCAATGTCCA"
#k=13
#Text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
#k = 3
#print(FrequentWords(Text,k))

"""
input: Pattern - DNA string pattern
       ex: Pattern = 'ATGATCAAG'
output: The reverse complement of a DNA string Pattern is the string formed by
        taking the complementary nucleotide of each nucleotide in Pattern, then
        reversing the resulting string
       ex: 'ACCGGGTTTT'
"""
def ReverseComplement(Pattern):
    # transform string into list
    input_list = list(Pattern)
    # create list to store complimentary string
    comp_list = []
    # loop through list and transform each nucleotide in DNA to its complimentary nucleotide
    for char in input_list:
        if char == 'A':
            comp_list.append('T')
        elif char == 'T':
            comp_list.append('A')
        elif char == 'C':
            comp_list.append('G')
        elif char == 'G':
            comp_list.append('C')
        else:
            print('Unable to determine nucleotide compliment')

    # reverse compliment list
    comp_list.reverse()
    # transform reversed compliment list back into a string
    revComp = ''.join(comp_list)
    # return reversed compliment string
    return revComp

#Pattern = 'GATTACA'
#print(ReverseComplement(Pattern))

"""
However, before concluding that we have found the DnaA box of Vibrio cholerae,
the careful bioinformatician should check if there are other short regions in the
Vibrio cholerae genome with multiple occurrences of "ATGATCAAG" (or "CTTGATCAT").
After all, maybe these strings occur as repeats throughout the entire Vibrio
cholerae genome, rather than just in the ori region.
"""

"""
input: Pattern-  DNA string pattern
       ex: Pattern = 'ATAT'
       Genome- entire genome string pattern
       ex: Genome = 'GATATATGCATATACTT'
output: All starting positions in Genome where Pattern appears as a substring
       ex: 1 3 9
"""
def PatternMatching(Pattern, Genome):
    # create empty list for result
    positions = []
    # determine index value we can stop checking for pattern
    for i in range(len(Genome)-len(Pattern)+1):
        # if we find the pattern within the genome, append starting position of pattern to positions list
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    result = ' '.join(str(number) for number in positions)
    return result

# Pattern = 'ATAT'
# Genome = 'GATATATGCATATACTT'
#Pattern = 'CTTGATCAT'
#input_file = open("input.txt")
#Genome = input_file.read()
#print(PatternMatching(Pattern, Genome))

"""
Although most bacteria have circular genomes, we have thus far assumed that
genomes were linear, a reasonable simplifying assumption because the length of
the window is much shorter than the length of the genome. This time, because we
are sliding a giant window, we should account for windows that “wrap around” the
end of Genome. To do so, we will define a string ExtendedGenome as Genome+Genome[0:n//2]
"""
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    print(ExtendedGenome)
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

Genome = "GATATATGCATATACTT"
# ExtendedGenome = GATATATGCATATACTTGATATATG
symbol = "C"
# print(SymbolArray(Genome, symbol))

"""
We observe that when we slide a window one symbol to the right, the number of
occurrences of symbol in the window does not change much, and so regenerating
the entire array from scratch is inefficient

We can view this sliding of the window as simply removing the first symbol from
the window (C) and adding a new symbol to the end (A). Thus, when shifting the
window right by one symbol, the number of occurrences of C in the window decreased
by 1 and increased by 0. Once we compute that array[0] is equal to 8, we automatically
know that array[1] is equal to 7 because the next symbol A does not equal C.

Input:  Strings Text and Pattern
Output: The number of times Pattern appears in Text
"""

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)                                     # n = 8
    ExtendedGenome = Genome + Genome[0:n//2]            # ExtendedGenome = AAAAGGGGAAAA
    array[0] = PatternCount(symbol, Genome[0:n//2])     # {0: 4}
    for i in range(1, n):                               # from 1 up to but not including 8
        array[i] = array[i-1]                           # array[1] = array[0] so array[1] = {0: 4}
        # if previous index matches symbol, subtract one
        if ExtendedGenome[i-1] == symbol:               # if ExtendedGenome[0] == A
            array[i] = array[i]-1                           # array[1] = 4 - 1 = 3 so array[1] = {0: 3}
        # if next index matches symbol, add one
        if ExtendedGenome[i+(n//2)-1] == symbol:        # if ExtendedGenome[4] == A
            array[i] = array[i]+1                           # array[1] = {0: 4}
    return array

Genome = "AAAAGGGG"
symbol = "A"
print(FasterSymbolArray(Genome, symbol))

"""
Every time we encounter a G, Skew[i] is equal to Skew[i-1]+1
Every time we encounter a C, Skew[i] is equal to Skew[i-1]-1
Otherwise, Skew[i] is equal to Skew[i-1]
"""

def Skew(Genome):
    skew = {}
    n = len(Genome)

# print(Skew("CATGGGCATCGGCCATACGCC"))
