# basic funciton to find mean
def nadji_prosek(lista):
    """Find mean value of given list, with added function to process dictionary"""
    if type(lista) == dict:
        prosek = sum(lista.values()) / len(lista)
    else:
        prosek = sum(lista) / len(lista)

    return prosek


print("dictionary", nadji_prosek({"a": 1, "b": 2, "c": 3}))
print("simple list", nadji_prosek([1, 2, 3, 4, 5]))
