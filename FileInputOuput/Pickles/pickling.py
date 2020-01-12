# Pickling is the method of serialization of objects in Python. It isn't easy to write data in the binary files as we
# saw in the previous examples. Hence, pickling provides a way to safely write a data in the binary file and reading
# from it when required.

import pickle
imelda = ("More Mayhem",
          "Imelda May",
          2011,
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Kentish Town Waltz"),
           (4, "Mayhem")))
with open("imelda.pickle", 'bw') as imelda_file:  # Write to the file with extension .pickle
    pickle.dump(imelda, imelda_file)              # dump the data(imelda tuple) in the pickle file

# To retrieve the data from the pickled file, we need to use the pickle.load() method

with open("imelda.pickle", 'br') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
print(imelda2)

# write some more data in the binary file using pickle.

even = list(range(0, 20, 2))
odd = list(range(1, 20, 2))

with open("imelda.pickle", "ba") as imelda_file:
    pickle.dump(even, imelda_file)
    pickle.dump(odd, imelda_file)
    pickle.dump(2998302, imelda_file)

with open("imelda.pickle", 'br') as imelda_pickled:
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

for i in even_list:
    print(i)

for j in odd_list:
    print(j)

print(x)
