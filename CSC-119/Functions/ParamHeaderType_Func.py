#different forms of function headers

'''
param1_func: single parameter passed to non-value func
'''
def param1_func(p1):
    print("entering:", param1_func.__name__)
    print("parameter1: ", p1)

'''
param2_func: two parameters passed to non-value func
'''
def param2_func(p1,p2):
    print("entering:", param2_func.__name__)
    print("parameter1: ", p1)
    print("parameter2: ", p2)

'''
param3_func: 3 parameters passed to non-value func
'''
def param3_func(p1,p2,p3):
    print("entering:", param3_func.__name__)
    print("parameter1: ", p1)
    print("parameter2: ", p2)
    print("parameter3: ", p3)

'''
paramN_func: N parameters passed to non-value func
'''
def paramN_func(*args):
    print("entering:", param1_func.__name__)
    print("num of params passed in: ", len(args))
    for arg in args:
        print("arg: ", arg)


'''
main: Entry point of Program
'''
def main():
    n1 =4
    n2 =3
    n3 =2
    s1 ="bird"
    s2 ="hello"
    s3 ="it"

    print("calling: ", param1_func.__name__, param1_func(n1))
    print("calling: ", param1_func.__name__, param1_func(s1))

    print("calling: ", param2_func.__name__, param2_func(n1,s1))
    print("calling: ", param2_func.__name__, param2_func(n1, n2))
    print("calling: ", param2_func.__name__, param2_func(s2, s3))

    print("calling: ", param3_func.__name__, param3_func(n1, n2, n3))
    print("calling: ", param3_func.__name__, param3_func(s1, s2, s3))
    print("calling: ", param3_func.__name__, param3_func(n1, s2, n3))

    print("calling: ", paramN_func.__name__, paramN_func(n1))
    print("calling: ", paramN_func.__name__, paramN_func(n1,n2))
    print("calling: ", paramN_func.__name__, paramN_func(n1,n2,n3))
    print("calling: ", paramN_func.__name__, paramN_func(n1,n2,n3,s1))
    print("calling: ", paramN_func.__name__, paramN_func(n1,n2,n3,s1,s2))
    print("calling: ", paramN_func.__name__, paramN_func(n1,n2,n3,s1,s2,s3))

if __name__ == "__main__":
    main()
