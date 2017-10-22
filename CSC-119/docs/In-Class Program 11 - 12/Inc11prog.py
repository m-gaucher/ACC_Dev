#Inc11prog.py

'''
value-return function with 3 parameters n1, n2 ,n3 passed in
'''
def average(n1,n2,n3):
    print("Entering: ", average.__name__ + '()')
    return (n1+n2+n3) / 3.0

'''
main: main function of program
'''
def main():
    avg = 0.0
    print("average before function call:", avg)
    avg = average(1,2,3)
    print("average after function call:", avg)

if __name__ == "__main__":
    main()
