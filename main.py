def string_info(str_):
    global calls_
    calls_ += 1
    info_str = (len(str_), str_.upper(), str_.lower())
    return info_str

def is_contains(str_, list_to_search):
    global calls_
    calls_ += 1
    str_ = str_.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if str_ in list_to_search:
        return True
    else:
        return False

calls_ = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls_)

