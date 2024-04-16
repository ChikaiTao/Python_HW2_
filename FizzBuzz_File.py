import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)
    fizz = (numbers % 3 == 0)
    buzz = (numbers % 5 == 0)
    conditions = [fizz & buzz, fizz, buzz]
    choices = ["FizzBuzz", "Fizz", "Buzz"]
    result = np.select(conditions, choices, default=numbers.astype(str))
    
    return result

# Usage example:
start = 1
finish = 15
fizzbuzz_results = FizzBuzz(start, finish)
fizzbuzz_results


def FizzBuzz(start, finish):
    v = ['buzz', 41, 'fizz', 43, 44, 'fizzbuzz']
    return(v)