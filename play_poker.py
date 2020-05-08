import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# die folgenden Zeilen muessen je nach Spiel angepasst werden
spieler = ("Spieler: ", "Anton", "Rafa", "Tico", "Alex", "Jens", "", "", "")

n_spieler = 5
offene_karten = 5

# Passwörter
alle_p = [4, 8, 2, 9, 1, 6, 14, 7, 0, 3]
# Anton:
a = alle_p[0]
b = alle_p[1]
# Rafa
c = alle_p[2]
d = alle_p[3]
# Tico:
e = alle_p[4]
f = alle_p[5]
# Alex
g = alle_p[6]
h = alle_p[7]
# Jens
i = alle_p[8]
j = alle_p[9]


def siehe_karten(Name_check, Name, Passwort1, Passwort2):
    if (Name_check == spieler[1]):
        if (Passwort1 == a) and (Passwort2 == b):
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[2]):
        if (Passwort1 == c) and (Passwort2 == d):
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[3]):
        if (Passwort1 == e) and (Passwort2 == f):
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[4]):
        if (Passwort1 == g) and (Passwort2 == h):
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[5]):
        if (Passwort1 == i) and (Passwort2 == j):
            secret(Name)
        else:
            raise Exception("Falsches Passwort")


# Karten und Funktionen

# erstelle Kartendeck
muster = ["♠ ", "♦ ", "♥ ", "♣ "]
zahl = np.arange(2, 11)
zahl = list(zahl.astype(str))
zahl += ["B", "D", "K", "A"]

karten = []
for i in range(0, 4):
    for k in zahl:
        karten.append(muster[i] + k)


# sonstige Funktionen
def pot():
    pot = (geld_sp1 + geld_sp2 + geld_sp3 + geld_sp4
           + geld_sp5 + geld_sp6 + geld_sp7 + geld_sp8)
    return int(pot)


def sieger(sieger, bank_sp1, bank_sp2, bank_sp3, bank_sp4,
           bank_sp5, bank_sp6, bank_sp7, bank_sp8):
    if (sieger == spieler[1]):
        bank_sp1 += pot()
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[2]):
        bank_sp1 -= geld_sp1
        bank_sp2 += pot()
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[3]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 += pot()
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[4]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 += pot()
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[5]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 += pot()
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[5]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 += pot()
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[6]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 += pot()
        bank_sp7 -= geld_sp7
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[7]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 += pot()
        bank_sp8 -= geld_sp8

    elif (sieger == spieler[8]):
        bank_sp1 -= geld_sp1
        bank_sp2 -= geld_sp2
        bank_sp3 -= geld_sp3
        bank_sp4 -= geld_sp4
        bank_sp5 -= geld_sp5
        bank_sp6 -= geld_sp6
        bank_sp7 -= geld_sp7
        bank_sp8 += pot()


def secret(Name):
    fig, ax = plt.subplots()

    # Karten definieren
    Karte1 = beschriftung(Name[0])
    Karte2 = beschriftung(Name[1])

    print("    ", Name[0], "    --    ", Name[1])

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='white')

    # place a text box in upper left in axes coords
    ax.text(0.02, 0.95, Karte1, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.4, 0.95, Karte2, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    plt.axis("off")
    plt.show()


def beschriftung(karte):
    teile = list(karte)

    if (len(teile) == 3):
        Karte = (
            f"{teile[2]} \n\n"
            f"    {teile[0]}    \n\n"
            f"         {teile[2]}"
        )
    else:
        Karte = (
            f"{teile[2] + teile[3]}\n\n"
            f"    {teile[0]}    \n\n"
            f"       {teile[2] + teile[3]}"
        )
    return Karte

part = 2

def offenlegen(runde):
    breite = np.arange(0, len(karten_im_spiel[part]))
    vergeben = np.array(alle_p)
    rest = np.isin(breite, vergeben)
    for i in range(0, rest.size):
        rest[i] = not rest[i]
    rest = list(breite[rest])

    erste = karten_im_spiel[part][rest[0]]
    zweite = karten_im_spiel[part][rest[1]]
    dritte = karten_im_spiel[part][rest[2]]
    vierte = karten_im_spiel[part][rest[3]]
    fünfte = karten_im_spiel[part][rest[4]]

    fig, ax = plt.subplots()

    # Karten definieren
    if (runde == "flop"):

        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = []
        Karte5 = []
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte)
    elif (runde == "turn"):
        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = beschriftung(vierte)
        Karte5 = []
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte)
    elif (runde == "river"):
        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = beschriftung(vierte)
        Karte5 = beschriftung(fünfte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte,
              "    --    ", fünfte)

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='white')

    # place a text box in upper left in axes coords
    ax.text(0, 0.95, Karte1, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.35, 0.95, Karte2, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.7, 0.95, Karte3, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(1.05, 0.95, Karte4, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(1.4, 0.95, Karte5, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    plt.axis("off")
    plt.show()


# zweiter Part von Liste alle_karten ist nur interessant. Der Rest
# dient nur zur Verwirrung

def alle_karten(seed):
    random.seed(seed)
    alle_karten = [random.sample(karten, 15),
                   random.sample(karten, n_spieler * 2 + offene_karten),
                   random.sample(karten, 15)]
    return alle_karten


