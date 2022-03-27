fib = 15
m = 3
fib_list=[]
fib_remain_list = []
num = 0
while True:
    if num < 2 :
        fib_list.append(num)
        fib_remain_list.append(num)
    else:
        element1 = fib_list[num-1]%m 
        element2 =  fib_list[num-2]%m
        element =  (element1 + element2)%m   
        fib_remain_list.append(element) 
        if fib_remain_list[-2:] == [0,1] and len(fib_remain_list) > 3:  
            break        
    num += 1
    print(fib_remain_list)
me_list = fib_remain_list[:-2]
print(me_list)
ind = fib%len(me_list)
print(ind)