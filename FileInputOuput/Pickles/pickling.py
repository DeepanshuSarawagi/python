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
