'''
Problem Introduction
This is an example of a problem where a subproblem of the corresponding greedy algorithm is slightly distinct
from the initial problem.
Problem Description
Task: The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum k such that n can be written as
a1 + a2 + · · · + ak where a1, . . . , ak are positive integers and ai != aj for all 1 ≤ i < j ≤ k.
Input Format: The input consists of a single integer n.
Constraints. 1 ≤ n ≤ 10^9
.
Output Format: In the first line, output the maximum number k such that n can be represented as a sum
of k pairwise distinct positive integers. In the second line, output k pairwise distinct positive integers
that sum up to n (if there are many such representations, output any of them).
'''
# def Pairwise_Distinct_Summand(fnum):
#     summmand_list = []
#     summand = 1
#     num = fnum
#     while num > 2*summand:
#         summmand_list.append(summand)
#         summand +=1
#         num = num - summand
#     if sum(summmand_list) != fnum:
#         summmand_list.append(fnum-sum(summmand_list))
#     return summmand_list    

def Pairwise_Distinct_Summand(fnum):
    summmand_list = []
    summand_num_pair = [1,fnum]
    while True:
        if 2*summand_num_pair[0] >= summand_num_pair[1]:
            summmand_list.append(summand_num_pair[1])
            break
        else:
            summmand_list.append(summand_num_pair[0])
            summand_num_pair[1] -= summand_num_pair[0]
            summand_num_pair[0] +=1
    return summmand_list    

entry_num = int(input('Please enter a number: '))
print(len(Pairwise_Distinct_Summand(entry_num)))
print(*Pairwise_Distinct_Summand(entry_num))         