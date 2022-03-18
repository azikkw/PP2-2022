#Function to multiply all the numbers in a list

def multiply(sum, numbers_list):
    for numbers in numbers_list:
        sum = sum * numbers
        
    print(sum)
    

sum = 1
numbers_list = [1, 2, 3, 4, 5]

multiply(sum, numbers_list)