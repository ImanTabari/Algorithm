def fibonacci_calc(n):
    fib_list = []
    for number in range(n):
        if number < 2:
            fib_list.append(number)
        else:
            fib_list.append(fib_list[number-2] + fib_list[number-1])
    print(fib_list)
    return fib_list[n-1]         

entry = int(input('Please enter the number:'))
fibonacci_calc(entry)
print (f'The fibonacci number for {entry} is: {fibonacci_calc(entry)}')
print(f'The last digit of this fibonacci number is = {fibonacci_calc(entry)%10}')