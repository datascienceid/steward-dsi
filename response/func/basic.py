
def get_welcome():
    reply = '''Selamat Datang di Server Data Science Indonesia.

    Apakah kamu hanya bisa lihat 1 atau 2 channel?
    artinya kamu belom di promote.
    Coba deh : $promote. Steward akan bantu setup.
    Untuk Info lebih lanjut, kunjungi laman ini : bit.ly/dsidiscord1.

    Jika kamu sudah bisa melihat semua channel, 
    Silahkan mulai diskusi, berbagi dan kontribusi.
    Terima kasih.

    Warm Regards,
    Steward
    '''
    return reply


def get_invalid_message():
    reply = '''Diriku masih perlu belajar bisa.
    Try this : $welcome, $halo, $promote'''
    return reply


def get_promote_message(uuid, opt='success'):
    if opt == 'success':
        reply = "Welcome "+uuid+". Kamu sudah dipromosikan menjadi Member Server. "
        reply += "Sekarang kamu bisa bergabung diberbagai channel diserver ini."
        return reply
    elif opt == 'failed':
        reply = "Halo "+uuid+". Kamu belum mendaftarkan discord id kamu ke datascience.or.id. "
        reply = reply + "Tolong daftarkan di isian 'telegram'. Jika sudah terlanjur terisi dengan telegram id, tolong diganti dengan discord id. "
        reply = reply + "Contoh discord id: steward_dsi#9568. "
        reply = reply + "Setelah itu ketik $promote kembali. "
        reply = reply + "Untuk lebih detilnya, bisa kunjungi : bit.ly/dsidiscord1"
    elif opt == 'ready':
        reply = "Halo "+uuid+'''. Kamu sudah dipromosikan. Untuk Role yang lebih, bisa hubungi @admin.'''
    else:
        reply = 'undefined message'
    return reply
