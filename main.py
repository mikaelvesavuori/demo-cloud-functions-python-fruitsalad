def fruit_salad(request):
    #request_json = request.get_json()
    #print(request_json)

    fruits = ['kiwi', 'orange', 'apple', 'physalis', 'banana']

    fruit_string = list_fruits(fruits)

    print(fruit_string)

    return fruit_string


def list_fruits(fruits):
    string = 'I ate some '

    for fruit in fruits:
        string += f'{fruit}, '

    string = string[:-2]

    return string
