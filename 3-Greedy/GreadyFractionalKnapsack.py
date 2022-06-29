'''
Problem Introduction
Given a set of items and total capacity of a knapsack, find the maximal value of fractions of items that fit
into the knapsack.

Input Format: The first line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines define the values and weights of the items. The i-th line contain integers vi and wi —
the value and the weight of i-th item, respectively.

Constraints. 1 ≤ n ≤ 10^3, 0 ≤ W ≤ 2 · 10^6; 0 ≤ vi ≤ 2 · 10^6, 0 < wi ≤ 2 · 10^6 for all 1 ≤ i ≤ n. All the numbers are integers.

Output Format: Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10^-3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of robunding issues).
'''
def knapsack_value_cal (numi,cap):
    item_counter = 0
    item_spec = []
    while item_counter<numi:
        v,w = map(float, input('Enter the value and weight of the item respectively, separated by space: ').split())
        item_spec.append((v,w))
        item_counter+=1
    item_spec.sort(key = lambda elem: elem[0]/elem[1] , reverse=True) # define a sorting key by lamda: it sorts the list by key per value(value per weight) 
    Total_value = 0
    for item in range(len(item_spec)):
        if cap >= 0:
            a = min(cap,item_spec[item][1])
            Total_value += (item_spec[item][0]*(a/item_spec[item][1]))
            cap -= a 
    return Total_value        

num_items, capacity = map(float,input('Enter number of items and the capacity of the knapsack respectively, separated by space: ').split())
print (knapsack_value_cal(num_items,capacity))

    

