def checkio(numbers_array):

    return sorted(numbers_array, key=lambda x:abs(x))





print(checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20])
print(checkio((1, 2, 3, 0)) == [0, 1, 2, 3])
print(checkio((-1, -2, -3, 0)) == [0, -1, -2, -3])