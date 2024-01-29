#------------Even or Odd------------
#Description:
#create a function that takes on integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


#write function that takes in an integer

#evaluate whether that int is even or odd
#---using an if statement combined with % to check remainder of division by 2 

#returns string of even or  odd depending on the num


def even_or_odd(num):

    if num % 2 == 0:
        return "Even"
    
    else:
        return "Odd"
    
print(even_or_odd(11))

