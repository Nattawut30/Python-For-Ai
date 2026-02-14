# Type Hinting

# a dynamically typed language which means we don't know what the data types is
# so we need to process it until runtime

def my_function(my_parameter: int) -> str: # expected type 'int'
    return f"{my_parameter + 10}"

def other_function(other_parameter: str) -> int:
    print(f"Get the value of {other_parameter}")
    return len(other_parameter) + 5


result_1 = my_function(10) # Got "20" (str)
result_2 = other_function(result_1) # Receive "20" (str) convert into number and +5 = 25 (int)

print(f"Final result is {result_2}")

def even_number(param: list[int]) -> list[int]:
    # I'm not only expecting a list, I'm also expecting a list of integers as well
    return [n for n in param if n % 2 == 0]
    # I need an even number and return list of int

print(f"Even number: {even_number([1, 2, 3, 4, 5])} ")