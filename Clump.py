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
     Output: The integer PatternToIndex(Pattern)
     ex: 11
"""
