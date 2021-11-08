import smtplib
from random import shuffle
import copy
import secrets

AMOUNT = 10

class TooMuchInTheTeam(Exception):
    pass

def nb_participants_check(L):
    for i, team in enumerate(L):
        M = [e for A in L[:i]+L[i+1:] for e in A]
        if len(M) < len(L[i]):
            raise TooMuchInTheTeam(f"Too much participants in {team[0][2]}")

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

def make_pairs(L):
    R = []
    M = copy.deepcopy(L)
    shuffle(M)
    for e in M:
        shuffle(e)
    L_new = copy.deepcopy(M)
    nb_teams = len(L_new)
    for i, team in enumerate(L_new):
        for j, e in enumerate(L_new[i]):
            if len(M) == 1:
                M_next = M[0]
            else:
                M_next =  (M[:i]+M[i+1:])[(j+1)%(len(M)-1)]
            M_next_len = len(M_next)
            k = secrets.randbelow(M_next_len)
            gift_to = M_next[k]
            R.append((e, gift_to))
            del M_next[k]
            if M_next_len == 1:
                M = [e for e in M if e != []]
    return R

def send_email(L):
    from_addr = 'secret.santa.tipe@gmx.fr'

    server = smtplib.SMTP_SSL('mail.gmx.com', 465)
    server.set_debuglevel(1)
    server.ehlo

    server.login('secret.santa.tipe@gmx.fr', 'H)W8x{-Kc#=qN5g8')

    for e in L:
        to_addrs = e[0][3]
        subject = "Secret Santa - Tirage au sort"
        text = f"Bonjour {e[0][0]},\nCette année, tu es en charge du cadeau de {e[1][0]} {e[1][1]} ({e[1][2]}). Je te rappelle que le budget est de {AMOUNT}€.\nJoyeux Nöel à toi !"

        message = f"Subject: {subject}\nFrom: {from_addr}\nTo: {to_addrs}\n\n"
        message = message + text
        server.sendmail(from_addr, to_addrs, message.encode("utf8"))

    server.quit()

def Secret_Santa(file):
    try:
        L = group_by_team(csv_to_list(file))
        nb_participants_check(L)
        send_email(make_pairs(L))
    except TooMuchInTheTeam as TeamError:
        print(TeamError)

Secret_Santa('data.csv')