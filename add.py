import sys

def add(a,b):
    return a+b

if __name__ == "__main__":
    num1 = int(input(sys.argv[1]))
    num2 = int(input(sys.argv[2]))
    result = add(num1,num2)
    print("Result = ", result)