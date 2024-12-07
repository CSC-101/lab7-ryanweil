import sys
import convert


#Main takes in inputs from the command_line parameters and creates a sum of all numbers input.
#Main takes in any value and returns a float
#def main():
#print(numbers)
#if script parameters = (hello 1 2 3 done)
# 6.0
def main():
    numbers = 0.0
    for arg in sys.argv[1:]:
        if arg == 'done':
            break
        if convert.string_to_float(arg) is not None:
            numbers += convert.string_to_float(arg)
    print(numbers)



if __name__ == '__main__':
    main()