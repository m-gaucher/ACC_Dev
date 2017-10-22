#pass by reference (note the types are mutable)

'''
pass_by_ref: Append 88,99 to our mutable list
'''
def pass_by_ref(num_list):
    print("Entering pass_by_ref:")
    print(num_list)
    print("Inside pass_by_ref() : Appending 88 to num_list; num_list is now:")
    num_list.append(88)
    print(num_list)
    print("Inside pass_by_ref() : Appending 99 to num_list; num_list is now:")
    num_list.append(99)
    print(num_list)

'''
main: Entry point of Program
'''
def main():
    num_list = [1,2,3,4,5,6]
    print("Before calling pass_by_ref(): num_list is:")
    print(num_list)
    print("Calling pass_by_ref()...")
    pass_by_ref(num_list)
    print("After claling pass_by_ref(); num_list is:")
    print(num_list)

if __name__ == "__main__":
    main()
