import smtplib
from random import shuffle

def csv_to_list(file):
    with open(file) as f:
        L = f.read().splitlines()
    L = L[1:]
    for i, e in enumerate(L):
        L[i] = e.split(';')
    return L

def make_pairs(L):
    shuffle(L)
    length = len(L)
    M = [('', '')]*length
    for i, e in enumerate(L):
        M[i] = (L[i], L[(i+1)%length])
    return M

def send_email(L):
    from_addr = 'secret.santa.tipe@gmx.fr'

    server = smtplib.SMTP_SSL('mail.gmx.com', 465)
    server.set_debuglevel(1)
    server.ehlo

    server.login('secret.santa.tipe@gmx.fr', 'H)W8x{-Kc#=qN5g8')

    for e in L:
        to_addrs = e[0][2]
        subject = "Secret Santa - Tirage au sort"
        text = f"Bonjour {e[0][0]},\nCette année, tu es en charge du cadeau de {e[1][0]} {e[1][1]} !\nJoyeux Nöel à toi !"

        message = f"Subject: {subject}\nFrom: {from_addr}\nTo: {to_addrs}\n\n"
        message = message + text
        server.sendmail(from_addr, to_addrs, message.encode("utf8"))

    server.quit()

print(send_email(make_pairs(csv_to_list('data.csv'))))