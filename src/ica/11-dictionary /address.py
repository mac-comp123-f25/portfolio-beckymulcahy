betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]

print(address_book)

address_book.append({'Name': 'Becky',
                 'Phone': 'x3316',
                 'Street': '502 Wingate Road',
                 'City': 'Baltimore',
                 'State': 'MD',
                 'Email': 'bmulcahy@macalester.edu'})

address_book.append({'Name': 'Ella',
                 'Phone': 'x5518',
                 'Street': '1618 San Pascal',
                 'City': ' Pasadena',
                 'State': 'CA',
                 'Email': 'ewuancipink@macalester.edu'})

def filter_by_city(city, address_book):
    result = []
    for entry in address_book:
        if entry['City'] == city:
            result.append(entry)
    return result



