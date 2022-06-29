# Huge Fibonacci Number modulo m


def fib_mod_cal(fib,m):
    #fib_list=[]
    fib_remain_list = []
    num = 0
    while fib_remain_list[-2:] != [0,1] or len(fib_remain_list) < 3:
        if num < 2 :
            #fib_list.append(num)
            fib_remain_list.append(num)
        else: 
            #fib_list.append(fib_list[num-1] + fib_list[num-2])
            #fib_remain_list.append((fib_list[num-1] + fib_list[num-2])%m)   
            fib_remain_list.append((fib_remain_list[num-1] + fib_remain_list[num-2] )%m)       
        num += 1
    Sequence_list = fib_remain_list[:-2]
    remainder_index = fib%len(Sequence_list)
    return Sequence_list[remainder_index]
E_fibonacci, E_mod = [int(x) for x in input('Please enter the nth fibonacci and the mod: ').split()]
print(f'The remainder of "{E_fibonacci}"th fibonacci number to "{E_mod}" equals to: {fib_mod_cal(E_fibonacci,E_mod)}')    


