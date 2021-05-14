def isometric_strings(str1, str2):

    iter = 0
    try:
        while str1!=str2:
            str1 = str1.replace(str1[iter], str2[iter])
            iter+=1
        return True
    except:
        return False


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

