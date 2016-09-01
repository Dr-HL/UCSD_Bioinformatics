import math
"""
Clump Finding Problem: Find patterns forming clumps in a string.

We aspire to slide a window down the entire Genome string only once. As we slide
this window, we will keep track of the number of times that each k-mer Pattern
has already appeared in Text, updating these numbers as we proceed in a
Frequency array

Our plan is to slide a window of fixed length L along the genome, looking for a region
where a k-mer appears several times in short succession. The parameter value L = 500
reflects the typical length of ori in bacterial genomes.

We defined a k-mer as a "clump" if it appears many times within a short interval of the
genome. More formally, given integers L and t, a k-mer Pattern forms an

(L, t)-clump

inside a (longer) string Genome if there is an interval of Genome of length L in
which this k-mer appears at least t times. (This definition assumes that the k-mer
completely fits within the interval.)

1. Order all 4^k k-mers lexicographically(like how they would be ordered in a dictionary)

ex with k = 2: AA AC AG AT CA CC CG CT GA GC GG GT TA TC TG TT

2. PatternToIndex(Pattern)
Treat DNA strings as numbers in base 4, where A = 0, C = 1, G = 2, T = 3
Then convert base 4 DNA pattern to base 10 in order to assign each pattern
an index in the frequency array

ex with k = 2: AA AC AG AT CA CC CG CT GA GC GG GT TA TC TG TT
base4(pattern) 00 01 02 03 10 11 12 13 20 21 22 23 30 31 32 33
base10(index)  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15

Code Challenge: Implement PatternToIndex
     Input: A DNA string Pattern
     ex: AGT
     Output: The index within the genome
     ex: 11
"""

def LetterToNumber(Letter):
    if Letter == 'A':
        return 0
    elif Letter == 'C':
        return 1
    elif Letter == 'G':
        return 2
    elif Letter == 'T':
        return 3
    else:
        return "INVALID"

def PatternToIndex(Pattern):
    Base10 = 0
    PatternInput = list(Pattern)
    PatternToBase4 = []
    for Letter in PatternInput:
        PatternToBase4.append(LetterToNumber(Letter))
    PatternToBase4.reverse()
    for index, value in enumerate(PatternToBase4):
        Base10 += value * 4**index
    return Base10

# print(PatternToIndex('CCAGA'))

"""
CODE CHALLENGE: Implement FrequencyIndexToPattern
     Input: Integers index and k.
     Output: The string NumberToPattern(index, k).
"""

def NumberToLetter(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'
    else:
        return "INVALID"

def IndexToPattern(index, k):
    numbers = []
    letters = []
    quotient = index
    while (quotient > 0):
        remainder = quotient % 4
        numbers.append(remainder)
        quotient = math.floor(quotient / 4)
    if (quotient != 0):
        numbers = numbers + [quotient]
    numbers.reverse()
    while (len(numbers) < k):
        numbers = [0] + numbers
    for number in numbers:
        letters.append(NumberToLetter(number))
    DNA = ''.join(letters)
    return DNA

# print(IndexToPattern(5437, 8))

"""
Code Challenge: Implement ComputingFrequencies to generate a frequency array.
    Input: A DNA string Text followed by an integer k.
    Output: FrequencyArray(Text).
"""
def ComputingFrequencies(Text, k):
    frequency = []
    for i in range(0, 4**k):
        frequency.append(0)
    for i in range(0, (len(Text) - (k-1))):
        currentPattern = Text[i:i+k]
        index = PatternToIndex(currentPattern)
        frequency[index] += 1
    result = ' '.join(str(number) for number in frequency)
    return result

#input_file = open("input.txt")
#Text = input_file.read()
#k = 5
#print(ComputingFrequencies('ATGGCGCCTGAATCTCACATATTAGGGTAGATGTCTGCTAGAAGCGAAATTGCATAGGGGGGTCACCCATGCTGCTGCTGTACCTCTGCTGTATACTTTGGCACGGCCCGGCACTATGACTGTACTGGCGCTAACCACGTTCAATCGCGAACCCTACTCTCGACGGTTTTCTGCATCGAATCGTGACGCTCTCCCGTGTATTGCGTTGGTTTTATCAGAGTAATAACTAGTCTAGTAATATCGTGAGCTTTCCTAGCAACTCTAGTCCTCAGCTTCCAAACTGTTTAGAACGCGATTACTCGAGCACAGCGTAATTAGGATCTGGTTAGCCAAAGATTAGCTTAAACATATTGTGCCCCTTTACTACAGGCCCATCCGTGTGACGACGTGTATGGCAATCTCTGCAGGGATTACAACCGCGCTACCTCAGACCTTGCGTGATTGTGAGTCGTCGTGAATTTCTCGTCGATGGCTCACTTCCTAGACGACCGATCTGATGGGTCGACAGATCAACAGATCAGATTGTAGAAATGGCGAGAATAACCCTGCCTGGCGGCTTCGAGTGCACTGGTTGGTCGATGAGTAATCGGCTTACACGCTGCCGCCCGAGGTCCGTAGTCTCATTAGTGCGCACTTCCCGGAGTCACAACTTTCACCTGGATATCCCTAGTTGCCACTCCCTGGTGCGGTCTGCCAAATGCCGCCTACATAATCTCTTGT', 5))

"""
Pseudocode to find clumps of k-mers w/in the entire genome
def ClumpFinding(Genome, k, t, L):
    clumps = set()
    for i ← 0 to 4k − 1
        Clump(i) ← 0
    Text ← Genome(0, L)
    FrequencyArray ← ComputingFrequencies(Text, k)
    for i ← 0 to 4k − 1
        if FrequencyArray(i) ≥ t
            Clump(i) ← 1
    for i ← 1 to |Genome| − L
        FirstPattern ← Genome(i − 1, k)
        index ← PatternToNumber(FirstPattern)
        FrequencyArray(index) ← FrequencyArray(index) − 1
        LastPattern ← Genome(i + L − k, k)
        index ← PatternToNumber(LastPattern)
        FrequencyArray(index) ← FrequencyArray(index) + 1
        if FrequencyArray(index) ≥ t
            Clump(index) ← 1
    for i ← 0 to 4k − 1
        if Clump(i) = 1
            Pattern ← NumberToPattern(i, k)
            add Pattern to the set FrequentPatterns
    return FrequentPatterns
"""
