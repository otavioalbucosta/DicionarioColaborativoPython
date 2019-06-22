import socket
import datetime
MAX_BYTES = 65535
import pickle
dict = {'vento': ['wind', 'kaze', 'wind', 'vento'], 'tempo': ['time', 'jikan', 'zeit', 'tempo'], 'calor': ['heat', 'atsusa', 'warme', 'calore'], 'palavra': ['word', 'kotoba', 'wort', 'parola']}
#while True:
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #text = input("Digite o que você quer fazer: adicionar ou consultar?")
    #data = text.encode('utf-8')
   # sock.sendto(data, ('127.0.0.1', 1080))
   # data, address = sock.recvfrom(MAX_BYTES)
   # print(data.decode('utf-8'))
   # text = input()
   # sock.sendto(text.encode('utf-8'),address)
   # data, address = sock.recvfrom(MAX_BYTES)
   # print(data.decode('utf-8'))
with open('book.pickle','wb') as f:
    pickle.dump(dict,f)
