'''
Problem Description
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer m.
Constraints. 1 ≤ m ≤ 10^3
.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m.
'''
import sys
entry_coin = int(input('Enter the amount of coin to be canged: '))

'''
num_10coin = entry_coin//10
num_5coin = (entry_coin%10)//5
num_1coin = entry_coin - (num_10coin*10 + num_5coin*5)
number_of_coins = num_10coin + num_5coin + num_1coin
print(number_of_coins) 
'''

def num_of_coins(c):
    number_of_coins = c//10 + (c%10)//5 + (c%10)%5
    return number_of_coins

print(num_of_coins(entry_coin))    
