"""sample calc"""

def sutract(a, b):
    return a-b

def main():

    a = input("enter first number: ")
    b = input("enter second number: ")

    ans = subtract(a, b)

    print("Your calucated result is: ", ans)
    print("Sum is:", add(a, b))
    # print("you are in main")
def add(a, b):
    return a + b
    

if __name__ = "__main__":
    main()