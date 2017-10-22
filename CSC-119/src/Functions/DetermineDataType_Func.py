# Determine a given data type using function var_type

'''
var_type: determine a given item's type
'''
def var_type(item):
    print("entering function:",var_type.__name__)
    if( type(item) == int ):
        print("int item:", item, "is type:", type(item))
    if( type(item) == str ):
        print("str item:", item, "is type:", type(item))
    if( type(item) == float ):
        print("float item:", item, "is type:", type(item))
    if( type(item) == list ):
        print("list item:", item, "is type:", type(item))
    if( type(item) == tuple ):
        print("tuple item:", item, "is type:", type(item))

'''
main: Entry point of Program
'''
def main():
    val_int = 0
    val_float = 3.14
    val_string ="random"
    var_list = ['bird', 1, 3, 2.2]
    var_tuple = ('word', 5, 6, 7.9)

    print("calling function var_type() with int...")
    var_type(val_int)
    print("back from function var_type()...")

    print("now calling function var_type() with str...")
    var_type(val_string)
    print("back from function var_type()...")

    print("now calling function var_type() with list...")
    var_type(var_list)
    print("back from function var_type()...")

    print("now calling function var_type() with tuple...")
    var_type(var_tuple)
    print("back from function var_type()...")

if __name__ == "__main__":
    main()
