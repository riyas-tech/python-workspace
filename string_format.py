name = 'riyas'
print('Hello {}'.format(name))

num = 1000.987123
print(f'{num:.2f}')


message = 'Hello'
print('{0}  ---   {1}'.format(name, message))


store_id = 1101

# 1. ### YOUR CODE HERE ###
store_id = str(store_id)

# 2. ### YOUR CODE HERE ###
print(type(store_id))

### YOUR CODE HERE ###
def zip_checker(zipcode):
    if len(zipcode) == 5:
        if zipcode[0:2] =='00':
            return 'Invalid ZIP Code.'
        else:
            return zipcode
    elif zipcode[0] != '0':
        zipcode = '0' + zipcode
        return zipcode
    else:
        return 'Invalid ZIP Code.'
    
print(zip_checker('02806'))     # Should return 02806.
print(zip_checker('2806'))      # Should return 02806.
print(zip_checker('0280'))      # Should return 'Invalid ZIP Code.'
print(zip_checker('00280'))     # Should return 'Invalid ZIP Code.'


url = "https://exampleURL1.com/r626c36"

# 1. ### YOUR CODE HERE ###
id = url[-7:]

# 2. ### YOUR CODE HERE ###
print(id)


# Sample valid URL for reference while writing your function:
url = 'https://exampleURL1.com/r626c36'

### YOUR CODE HERE ###
def url_checker(url):
    url = url.split('/')
    protocol = url[0]
    store_id = url[-1]
    # If both protocol and store_id bad
    if protocol != 'https:' and len(store_id) != 7:
        print(f'{protocol} is an invalid protocol.',
            f'\n{store_id} is an invalid store ID.')
    # If just protocol bad
    elif protocol != 'https:':
        print(f'{protocol} is an invalid protocol.')
    # If just store_id bad
    elif len(store_id) != 7:
        print(f'{store_id} is an invalid store ID.')
    # If all ok
    else:
        return store_id