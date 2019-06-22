import socket
from threading import Thread
import os
import pickle
MAX_BYTES = 65535
dict = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 1080))
print('Listening at {}'.format(sock.getsockname()))
while True:
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('utf-8')
    if text == "editar":
        with open('book.pickle','rb') as f:
            data = pickle.load(f)
            print(data)
            dat = [*data]
            dat = sorted(dat)
            print(dat)
            dato = " ".join(dat)
            sock.sendto(dato.encode('utf-8'),address)
            j=1
            while j==1:
                newdata, address = sock.recvfrom(MAX_BYTES)
                newdat = newdata.decode('utf-8')
                print(newdat)

                if newdat in dat:
                    prdat = newdat
                    sendNow = " ".join(data[newdat])
                    sock.sendto(sendNow.encode('utf-8'),address)
                elif newdat == 'sair':
                    j=2
                else:
                    with open("book.pickle", "wb") as f:
                        newdat = newdat.split(" ")
                        if newdat[0] == '':
                            data.pop(prdat)
                            pickle.dump(data, f)
                            dat = [*data]
                            dat = sorted(dat)
                            dato = " ".join(dat)
                            sock.sendto(dato.encode('utf-8'), address)
                        else:
                            popped = data.pop(prdat)
                            data[newdat[0]] = newdat[1:5]
                            pickle.dump(data,f)
                            print(data)
                            dat = [*data]
                            dat = sorted(dat)
                            dato = " ".join(dat)
                            sock.sendto(dato.encode('utf-8'), address)
    if text == "adicionar":
        data,address = sock.recvfrom(MAX_BYTES)
        data = data.decode('utf-8')
        with open("book.pickle","rb") as f:
            dici = pickle.load(f)
        with open("book.pickle", "wb") as f:
            dat = data.split(" ")
            dici[dat[0]] = dat[1:5]
            pickle.dump(dici,f)
            print(dici)
    if text == "consultar":
        with open("book.pickle","rb") as f:
            dic = pickle.load(f)
            data = [*dic]
            dat = " ".join(data)
            sock.sendto(dat.encode('utf-8'),address)
            print(dic)
            j=1
            while j==1:
                word, address = sock.recvfrom(MAX_BYTES)
                word = word.decode('utf-8')
                print(word)
                if word in [*dic]:
                    data = dic[word]
                    print(dic[word])
                    data = " ".join(data)
                    data = data.encode('utf-8')
                    sock.sendto(data,address)
                elif word == "sair":
                    j=2
