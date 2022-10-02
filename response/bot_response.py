'''
status :
1 --> there is no outside function
2 --> there is outside function (add roles)
'''
# $bijak

from response.func.basic import get_hello, get_invalid_message, get_welcome


def get_response(message):
    if message.content.startswith('$welcome'):
        response = get_welcome()
        status = 1

    elif message.content.startswith('$halo'):
        response = get_hello(message)
        status = 1

    elif message.content.startswith('$promote'):
        response = ''
        status = 2

    else:
        response = get_invalid_message()
        status = 1

    return response, status
