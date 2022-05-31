'''
Problem Introduction:
The dot product of two sequences a1, a2, . . . , an and b1, b2, . . . , bn of the same length is equal to
aibi = a1b1 + a2b2 + · · · + anbn .
Problem Description:
Task: The goal is, given two sequences a1, a2, . . . , an and b1, b2, . . . , bn, find a permutation π of the second
sequence such that the dot product of a1, a2, . . . , an and bπ1, bπ2, . . . , bπn is minimum.
Input Format: The first line contains an integer n, the second one contains a sequence of integers
a1, a2, . . . , an, the third one contains a sequence of integers b1, b2, . . . , bn.
Constraints. 1 ≤ n ≤ 10^3; -10^5 ≤ ai, bi ≤ 10^5 for all 1 ≤ i ≤ n.
Output Format: Output the minimum possible dot product.
'''
def Min_DotProduct_cal(num,fs,ss):
    MinDotPro = 0
    fs.sort()
    ss.sort(reverse=True)
    for ind in range(num):
        MinDotPro += fs[ind]*ss[ind]
    return MinDotPro

num_of_num = int(input('Enter the number of your serries: '))
first_seq = [int(x) for x in input(f'Pleas enter "{num_of_num}" number as your first sequence: ').split()]
second_seq = [int(x) for x in input(f'Pleas enter "{num_of_num}" number as your second sequence: ').split()]
print (Min_DotProduct_cal(num_of_num,first_seq,second_seq))    

 