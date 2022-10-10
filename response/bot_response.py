'''
status :
1 --> there is no outside function
2 --> there is outside function (add roles)
'''

from response.func.basic import get_invalid_message, get_welcome
from response.func.intermediate import get_hello, get_randq


def get_response(message):
    if message.content.startswith('$welcome'):
        response = get_welcome()
        status = 1

    elif message.content.startswith('$halo'):
        response = get_hello(message)
        status = 1

    elif message.content.startswith('$bijak'):
        response = get_randq()
        status = 1

    elif message.content.startswith('$promote'):
        response = ''
        status = 2

    else:
        response = get_invalid_message()
        status = 1

    return response, status
