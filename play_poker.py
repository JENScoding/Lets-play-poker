import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# die folgenden Zeilen muessen je nach Spiel angepasst werden
spieler = ("Spieler: ", "Anton", "Rafa", "Tico", "Alex", "Jens", "", "", "")

n_spieler = 5
offene_karten = 5

# Passwoerter
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
            print(Name_check)
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[2]):
        if (Passwort1 == c) and (Passwort2 == d):
            print(Name_check)
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[3]):
        if (Passwort1 == e) and (Passwort2 == f):
            print(Name_check)
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[4]):
        if (Passwort1 == g) and (Passwort2 == h):
            print(Name_check)
            secret(Name)
        else:
            raise Exception("Falsches Passwort")

    if (Name_check == spieler[5]):
        if (Passwort1 == i) and (Passwort2 == j):
            print(Name_check)
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
def pot(geld_einsatz):
    pot = (geld_einsatz[0] + geld_einsatz[1] + geld_einsatz[2] + geld_einsatz[3]
           + geld_einsatz[4] + geld_einsatz[5] + geld_einsatz[6] + geld_einsatz[7])
    return int(pot)


def sieger(sieger, bank, geld_einsatz, total_pot):
    if (sieger == spieler[1]):
        bank[0] += total_pot
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[2]):
        bank[0] -= geld_einsatz[0]
        bank[1] += total_pot
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[3]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] += total_pot
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[4]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] += total_pot
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[5]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] += total_pot
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[5]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] += total_pot
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[6]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] += total_pot
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[7]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] += total_pot
        bank[7] -= geld_einsatz[7]

    elif (sieger == spieler[8]):
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] += total_pot


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

part = 2 # nehm immer die zweite Liste (dient zur Verwirrung)

def offenlegen(runde, karten_im_spiel):
    breite = np.arange(0, len(karten_im_spiel[part]))
    vergeben = np.array(alle_p)
    rest = np.isin(breite, vergeben)
    for i in range(0, rest.size):
        rest[i] = not rest[i]
    rest = list(breite[rest])

    nullte = "   "
    erste = karten_im_spiel[part][rest[0]]
    zweite = karten_im_spiel[part][rest[1]]
    dritte = karten_im_spiel[part][rest[2]]
    vierte = karten_im_spiel[part][rest[3]]
    fuenfte = karten_im_spiel[part][rest[4]]

    fig, ax = plt.subplots()

    # Karten definieren
    if runde == "null":
        Karte1 = beschriftung(nullte)
        Karte2 = beschriftung(nullte)
        Karte3 = beschriftung(nullte)
        Karte4 = beschriftung(nullte)
        Karte5 = beschriftung(nullte)

    if (runde == "flop"):

        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = beschriftung(nullte)
        Karte5 = beschriftung(nullte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte)
    elif (runde == "turn"):
        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = beschriftung(vierte)
        Karte5 = beschriftung(nullte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte)
    elif (runde == "river"):
        Karte1 = beschriftung(erste)
        Karte2 = beschriftung(zweite)
        Karte3 = beschriftung(dritte)
        Karte4 = beschriftung(vierte)
        Karte5 = beschriftung(fuenfte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte,
              "    --    ", fuenfte)

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

# bestimme wer die Blinds hat und wer anfaengt

def big_blind(bb):
    if (n_spieler - bb < 0):
        bb = 1
    return bb

def beginn(b):
    if (n_spieler - b < -1):
        b = 2
    elif (n_spieler - b < 0):
        b = 1
    return b

# zweiter Part von Liste alle_karten ist nur interessant. Der Rest
# dient nur zur Verwirrung

def alle_karten(seed):
    random.seed(seed)
    alle_karten = [random.sample(karten, 15),
                   random.sample(karten, n_spieler * 2 + offene_karten),
                   random.sample(karten, 15)]
    return alle_karten


