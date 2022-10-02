'''
status :
1 --> there is no outside function
2 --> there is outside function (add roles)
'''

from response.func.basic import get_hello

def get_response(message):
            # message.mentions[0].id
    if message.content.startswith('$welcome'):
        response = '''Selamat Datang di Server Data Science Indonesia. 
        Apakah kamu cuma bisa lihat 1 atau 2 channel? berarti kamu belom di promote.
        Coba deh : $promote. Steward akan bantu setup.
        Untuk Info lebih lanjut, kunjungi laman ini : bit.ly/dsidiscord1'''
        status = 1
    
    elif message.content.startswith('$halo'):
        response = get_hello(message)
        status = 1

    elif message.content.startswith('$promote'):
        response = ''
        status = 2
    
    # elif message.content.startswith('$bijak'):
    #     response = ...
    #     status = 1

    else:
        response = '''Diriku masih perlu belajar bisa. 
        Try this : $welcome, $halo, $promote'''
        status = 1

    return response,status
    
