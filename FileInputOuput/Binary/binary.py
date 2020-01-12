# How to create a binary file and write data in it.

with open("binary", 'bw') as bin_file:
    for i in range(1, 17):
        bin_file.write(bytes([i]))  # This is done to convert the data into binary type

"""We are using the built-in function bytes() to convert the data into the bytes object which can be written to the 
binary file. bytes([i]) is an immutable version of bytes version which cannot be changed."""

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)

# Writing hexadecimal numbers into a binary file and reading it
a = 65534
b = 65535
c = 65536
x = 2998302

with open("binary2", 'bw') as bin_file1:
    bin_file1.write(a.to_bytes(2, 'big'))
    bin_file1.write(b.to_bytes(2, 'big'))
    bin_file1.write(c.to_bytes(4, 'big'))
    bin_file1.write(x.to_bytes(4, 'big'))
    bin_file1.write(x.to_bytes(4, 'little'))

"""Syntax of writing a decimal integer to bytes is 
'file_name_variable.write(integer_variable.to_bytes(byte_length, 'type'))"""

with open("binary2", 'br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)
