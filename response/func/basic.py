
def get_welcome():
    reply = '''Selamat Datang di Server Data Science Indonesia. 
        
        Apakah kamu hanya bisa lihat 1 atau 2 channel? artinya kamu belom di promote.
        Coba deh : $promote. Steward akan bantu setup.
        Untuk Info lebih lanjut, kunjungi laman ini : bit.ly/dsidiscord1.
        
        Jika kamu sudah bisa melihat semua channel, Silahkan mulai diskusi, berbagi dan kontribusi.
        Terima kasih.

        Warm Regards,
        Steward
        '''
    return reply

def get_invalid_message():
    reply = '''Diriku masih perlu belajar bisa. 
        Try this : $welcome, $halo, $promote'''
    return reply