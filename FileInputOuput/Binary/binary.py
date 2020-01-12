# How to create a binary file and write data in it.

with open("binary", 'bw') as bin_file:
    for i in range(1, 17):
        bin_file.write(bytes([i]))  # This is done to convert the data into binary type

with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)
