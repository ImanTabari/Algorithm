
import random

def pairwise_product_1 (t1):
    tt1 = sorted(t1, reverse=True)
    return tt1[0]*tt1[1]

def pairwise_product_2 (t2):
    max1 = 0
    max2 = 0
    for num in t2:
        if num > max1: max1 = num
    for i in range(len(t2)):
        if  t2[i]>max2 and i != t2.index(max1) : max2 = t2[i]  # we have to use index as an itterator(i in range ...) because if we use element as an itterator(num in num_list) and use index method in if statement
                                                                # in case of having duplicated number in the num_list index will return the first occerance of the elemnt that can be the same as max1 index
    return max1*max2

num_of_num = int(input('Please enter number of numbers: '))
num_range = int(input('Please enter range of numbers: ')) 
while True:  
    num_list = [random.randint(0,num_range) for x in range(num_of_num)]
    if pairwise_product_1(num_list) == pairwise_product_2(num_list):
        print('ok', num_list)
    else:
        print(num_list, pairwise_product_1(num_list), pairwise_product_2(num_list))
        break

                    

   