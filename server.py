#!/usr/bin/python
"""Server hosting Texas Hold 'Em games

Eventually I want to be able to host more than one table

First, implement a table structure for players to join, watch, and leave
"""
import socket
import player
import pitch

connections=[]
s=socket.socket()
host=socket.gethostname()
port=11037
s.bind((host,port))
s.listen(10)
print '[INFO] Server listening on port '+str(port)

tab = pitch.Pitch()
print '[INFO] Table created'

while True:
    sit = 'a'
    c, addr=s.accept()
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    uname = c.recv(50)
    user = player.Player(uname)
    print uname+' has walked in, everyone stare!'
    c.send('Welcome to the table '+uname+'!')
    sit = c.recv(1)
    if sit == 'w':
        print uname+' is watching the table'
        c.send('You\'re watching the table.\t\tpervert..')
        tab.watchers.append(user)
        connections.append((c, addr, uname))
        continue
    elif sit == 'p':
        print uname+' is playing'
        c.send('You\'re really playing? Good luck.')
        tab.players.append(user)
        connections.append((c, addr, uname))
        continue
    else:
        del user
        print 'Users still here:'
        for x in connections:
            print str(x[2])+'@'+str(x[1])
        c.send('Goodbye.')
        print uname+' left this realm'
        c.close
        continue
