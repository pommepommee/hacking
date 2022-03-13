import socket
import sys
from math import sqrt
from time import sleep

# Vous devez calculer la racine carré du nombre n°1 et multiplier le résultat obtenu par le nombre n°2.
# Vous devez ensuite arrondir à deux chiffres après la virgule le résultat obtenu.
# Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le bot reçoit le message !ep1.

host = "irc.root-me.org"
port = 6667
channel = b"#root-me_challenge"
botnick = b"Candy"
trash = ""

def compute(token):
    numbers = [int(x) for x in token.split('/')]
    x = round(sqrt(numbers[0]) * numbers[1], 2)
    return bytes(str(x).encode('ASCII'))

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
    

irc.send(b"PRIVMSG " + botnick + b" !ep1\r\n")
trash = irc.recv(7000)
token = trash.split(b":")[-1].decode()
ans = compute(token)

irc.send(b"PRIVMSG " + botnick + b" !ep1 -rep " + ans + b"\r\n")
text = irc.recv(500)
print(text)

irc.close()