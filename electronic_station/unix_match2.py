import re

def unix_match(filename, pattern):

    pattern = pattern.replace('.','\.')
    pattern = pattern.replace('?','.')
    pattern = pattern.replace('*','.*')
    if '[!]' in pattern:
        pattern = pattern.replace('[!]','\[\!\]')
    else:
        pattern = pattern.replace('!','^')

    try:
        re.search(rf'{pattern}', filename).group()
        return True
    except:
        return False


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    assert unix_match('[!]check.txt', '[!]check.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")