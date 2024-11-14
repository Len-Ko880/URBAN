calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    kortej = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return  kortej

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Грузовик'))
print(string_info('Воодушевление'))
print(string_info('коврик'))
print(is_contains('газ', ['ведро', 'ГАзопровод', 'ГАЗ']))
print(is_contains('мяч', ['водолаз', 'бита', 'ОВощ']))
print(is_contains('БЕг', ['ПОбег', 'скороСТЬ', 'бег']))

print(calls)