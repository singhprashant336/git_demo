"""sample calc"""

def sutract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def main():

    a = input("enter first number: ")
    op = input("chose the operation (+-x/): ")
    b = input("enter second number: ")

    if op not in ["+", "-", "+","x"]:
        raise("Invalid operation or currently this type of operation is not supported")
    if op == "-":
        ans = subtract(a, b)

    if op == "x":
        ans = multiply(a, b)

    print("Your calucated result is: ", ans)
    print("Sum is:", add(a, b))
    # print("you are in main")
def add(a, b):
    return a + b
    

if __name__ = "__main__":
    main()