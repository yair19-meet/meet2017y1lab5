#making a function
def add_numbers(start, end):
    c = 0
    for number in range(start, end + 1):
        print(number)
        c = c + number
    return(c)
    


#####################################################################


#using a function
    
answer = add_numbers(333,777)
print(answer)

test1 = add_numbers(1,2)
print(test1)
test2 = add_numbers(1, 100)
print(test2)
test3 = add_numbers(1000, 5000)
print(test3)
