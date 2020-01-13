import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Bajaj"
    bike["model"] = "Pulsar 200 NS"
    bike["color"] = "Navy Blue"
    bike["engine_size"] = "200cc"
    bike["engin_size"] = "200cc"
    for key in bike.keys():
        print(key)

    print(bike["model"])
    print(bike["color"])
    print(bike["engin_size"])  # incorrect key which is still there in shleve.db
    del bike["engin_size"]     # delete the incorrect key from the shelve.db
    for key in bike.keys():
        print(key)             # print the keys to confirm it is deleted from shelve.db

"""Shelves are really persistent which means, if we make an incorrect entry of key in the shelve db, it will still be
stored and you will be able to retrieve the values."""
