import smtplib
from random import shuffle

AMOUNT = 10

def csv_to_list(file):
    with open(file) as f:
        L = f.read().splitlines()
    L = L[1:]
    for i, e in enumerate(L):
        L[i] = e.split(',')
    return L

def group_by_team(L):
    teams = []
    for e in L:
        if e[2] not in teams:
            teams.append(e[2])
    nb_teams = len(teams)
    M = [[] for _ in range(nb_teams)]
    for i, team in enumerate(teams):
        for e in L:
            if e[2] == team:
                M[i].append(e)
    return M

def make_pairs_aux(L):
    length = len(L)
    M = [('', '')]*length
    for i, e in enumerate(L):
        M[i] = (L[i], L[(i+1)%length])
    return M

def make_pairs(L):
    R = []
    for i in range(len(L)):
        M = [e for A in L[:i]+L[(i+1)%(len(L)+1):] for e in A]
        shuffle(M)
        R.append(make_pairs_aux(M[len(L[i]):]))
    return [e for A in M for e in A]

def send_email(L):
    from_addr = 'secret.santa.tipe@gmx.fr'

    server = smtplib.SMTP_SSL('mail.gmx.com', 465)
    server.set_debuglevel(1)
    server.ehlo

    server.login('secret.santa.tipe@gmx.fr', 'H)W8x{-Kc#=qN5g8')

    for e in L:
        to_addrs = e[0][2]
        subject = "Secret Santa - Tirage au sort"
        text = f"Bonjour {e[0][0]},\nCette année, tu es en charge du cadeau de {e[1][0]} {e[1][1]}, je te rappelle que le budget est de {AMOUNT}€\nJoyeux Nöel à toi !"

        message = f"Subject: {subject}\nFrom: {from_addr}\nTo: {to_addrs}\n\n"
        message = message + text
        server.sendmail(from_addr, to_addrs, message.encode("utf8"))

    server.quit()

# send_email(make_pairs(csv_to_list('data.csv')))

# print(make_pairs(group_by_team(csv_to_list('data.csv'))))

L = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
shuffle(L)
for e in L:
    shuffle(e)
print(L)