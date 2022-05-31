#Greatest Common Divisor & Least Common Multipple
def gcd_cal(a,b):
    while (b != 0):
        remainder = a%b  
        a = b
        b = remainder
    return a
def lcm_cal(a,b):
    lcm = a*b//gcd_cal(a,b)
    return lcm
try:
    #big_num , small_num = int(input('Please enter the bigger number: ')), int(input('Please enter the smaller number: '))
    big_num, small_num = sorted([int(x) for x in input('Enter two numbers separated by space: ').split()], reverse=True)
except:
    print('You did not follow the input instruction') 
    exit()         
if small_num == 0: print('numbers have to be more than Zero.')
else:
    print(f'The Greatest Common Deviser of "{big_num}" and "{small_num}" equals to: {gcd_cal(big_num,small_num)}','\n')
    print(f'And The Least Common Multipple of "{big_num}" and "{small_num}" equals to: {lcm_cal(big_num,small_num)}')

