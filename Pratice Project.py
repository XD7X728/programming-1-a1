# PracticeProject.pv

# Code to practice using Git

def main():
    """Calculate the nth Fibonacci number"""
    # 1, 1, 2, 3, 5, 8, 13, 21, 34

    # Ask the user for which fib number they want
    num = int(input("Which fib number do you want?"))

    # start at num = 1 -> 1
    #          num = 2 -> 2
    #          num = 3 -> 2
    if num == 1 or num == 2:
        print(f"The {num}st/nd fibonacci number is 1.")
    else:
        for i in range(num):


if __name__ == "__main__":
    main()