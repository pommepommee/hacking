from email.mime import base
import socket
import sys
import codecs
from time import sleep

# Le bot vous répond alors par un message privé.
# Il s’agit d’une chaîne de caractères encodée.
# Vous devez lui renvoyer le message décodé. 
# Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le bot reçoit le message !ep1.

host = "irc.root-me.org"
port = 6667
channel = b"#root-me_challenge"
botnick = b"Candy"
trash = ""

def compute(token):
    ans = codecs.decode(token, 'rot_13')
    print(token, '=', ans)
    return ans.encode()

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting to:"+ host)
irc.connect((host, port))
irc.send(b"USER PommeBot PommeBot PommeBot : this is a fun bot\r\n")
irc.send(b"NICK PommeBot\r\n")
irc.send(b"msg nickserv register 123456789 tom522011@hotmail.fr\r\n")
irc.send(b"msg nickserv identify 123456789")
irc.send(b"JOIN " + channel + b"\r\n")

quit = False
while not quit:
    trash = irc.recv(7000)
    if trash.find(b'PING'):
        irc.send(b"PONG" + trash.split()[1] + b"\r\n")
    trash = irc.recv(7000)
    quit = True
    

irc.send(b"PRIVMSG " + botnick + b" !ep3\r\n")
trash = irc.recv(7000)
token = trash.split(b":")[-1].decode()
ans = compute(token)

irc.send(b"PRIVMSG " + botnick + b" !ep3 -rep " + ans + b"\r\n")
text = irc.recv(500)
print(text)

irc.close()