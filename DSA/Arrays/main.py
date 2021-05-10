import array

my_array = array.array('i')  # array is the module and array.array() is a class. Here we have initialized a constructor
# of class array with data object type as int

for i in range(1, 11):
    my_array.insert(i, i * 2)

list_from_array = my_array.tolist()

print(my_array)
print(list_from_array)

list1 = [1, 2, 3, 4, 5]
array2 = array.array('i')
array2.fromlist(list1)
print(array2)


def traverse_array(array):
    for i in array:
        print(i, end="\t")


traverse_array(array2)
