import random

def get_hello(message):
    list_hello = [
        'halo.. apa kabar '+str(message.author)+'?'
        ,'hai.. hai..'
        ,'how are you?'
        ,'are you still calling me?'
        ,'wait a minute'
        ,'tunggu dulu'
        ,'kamu manggil?'
        ,'sebentar ya..'
        ,'siapa disitu?'
        ,str(message.author)+' masih manggil ajah'
        ,'ada yg bisa dibantu?'
        ,"yes yes.. what's up?"
        ,"coba ditunggu sebentar ya"
        ,str(message.author)+' lagi apa?'
        ,'baru kenal ya?'
        ,'silahkan bisa dimulai.'
        ,'lagi nonton nih.'
        ,'butuh temen ya?'
        ,'aku masih random lho..'
        ,'jangan mulai deh..'
        ,'masih baru ya?'
        ,'hey, '+str(message.author)+' lagi sendiri ya?'
        ,'halo,'+str(message.author)+' udah makan?'
        ,'...'
        ,'bisa ditunggu kan ya? wait ..'
        ,'sesuai pesanan ya..'
        ,'pasti ada jalan'
        ,'helloo'
        ,'Hai, sudah $promote belom?'
        ,'Kalo mention, jangan lupa $promote'
        ,'hey, '+str(message.author)+' sudah kenalan dengan yg lain kah?'
        ,'halo.. sudah tau DSI belom?'
        ,'hai hai,. sudah belajar Data hari ini?'
        ,'hey, '+str(message.author)+' sudah Melek Data?'
    ]

    return random.choice(list_hello)