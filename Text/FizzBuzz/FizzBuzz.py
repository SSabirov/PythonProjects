# Function to print numbers from 1-100. for multiples of 3 prints Fizz, for mutiples of 5 prints Buzz
#for both prints FizzBuzz

def fizzBuzz():
    n=1

    for i in range(100):

        if n%3==0 and n%5==0:
            print('FizzBuzz')
        elif n%3==0:
            print('Fizz')
        elif n%5==0:
            print('Buzz')
        else:
            print(n)
        n+=1        


fizzBuzz()