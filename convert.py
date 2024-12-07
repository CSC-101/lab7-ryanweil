#The puprose of this function is to take in any input and return the float value.
#This function takes in a string and returns either None or a float
#def string_to_float(string:str:
    #return none
    #return string
#string_to_float('23')
#23
def string_to_float(string:str):
    try:
        string = float(string)
    except:
        return None
    return string

#The purpose of this function is to take user inputs and make it into a list of floats.
#This function takes in unser inputs of any value and returns a list of floats
#def gather_numbers() -> list[float]:
    #return numbers
#gather_numbers()
#3
#2
#1
#output: [3,0, 2,0, 1.0]
def gather_numbers() -> list[float]:
    numbers = []
    while True:
        inputs = input("Enter a number or type 'Done' when done: ")
        if inputs.lower() == 'done':
            break
        if string_to_float(inputs) is not None:
            numbers.append(string_to_float(inputs))

    return numbers


if __name__ == '__main__':
    numbers = gather_numbers()
    print(numbers)