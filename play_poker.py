import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Passwoerter
alle_p = [4, 8, 2, 9, 1, 6, 14, 7, 0, 3, 16, 12, 11, 17, 18, 13]
# Anton:
a1 = alle_p[0]
b1 = alle_p[1]
# Rafa:
c1 = alle_p[2]
d1 = alle_p[3]
# Tico:
e1 = alle_p[4]
f1 = alle_p[5]
# Alex:
g1 = alle_p[6]
h1 = alle_p[7]
# Jens:
i1 = alle_p[8]
j1 = alle_p[9]
# Johnny:
k1 = alle_p[10]
l1 = alle_p[11]
# Jonas:
m1 = alle_p[12]
n1 = alle_p[13]
# Quentin:
o1 = alle_p[14]
p1 = alle_p[15]


# plot, wenn Passwort korrekt
def siehe_karten(name_check, name, passwort1, passwort2, spieler):
    if name_check == spieler[1]:
        if (passwort1 == a1) and (passwort2 == b1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[2]:
        if (passwort1 == c1) and (passwort2 == d1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[3]:
        if (passwort1 == e1) and (passwort2 == f1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[4]:
        if (passwort1 == g1) and (passwort2 == h1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[5]:
        if (passwort1 == i1) and (passwort2 == j1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[6]:
        if (passwort1 == k1) and (passwort2 == l1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[7]:
        if (passwort1 == m1) and (passwort2 == n1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")

    if name_check == spieler[8]:
        if (passwort1 == o1) and (passwort2 == p1):
            print(name_check)
            secret(name)
        else:
            raise Exception("Falsches Passwort")


# karten und Funktionen

# erstelle kartendeck
muster = ["♠ ", "♦ ", "♥ ", "♣ "]
zahl = np.arange(2, 11)
zahl = list(zahl.astype(str))
zahl += ["B", "D", "K", "A"]

karten = []
for i in range(0, 4):
    for k in zahl:
        karten.append(muster[i] + k)


# Funktionen zum Zaehlen
def pot(geld_einsatz):
    t_pot = (geld_einsatz[0] + geld_einsatz[1] + geld_einsatz[2] + geld_einsatz[3]
             + geld_einsatz[4] + geld_einsatz[5] + geld_einsatz[6] + geld_einsatz[7])
    return int(t_pot)


def sieger(name, bank, geld_einsatz, total_pot, spieler):
    if name == spieler[1]:
        bank[0] += total_pot - geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[2]:
        bank[0] -= geld_einsatz[0]
        bank[1] += total_pot - geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[3]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] += total_pot - geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[4]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] += total_pot - geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[5]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] += total_pot - geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[5]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] += total_pot - geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[6]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] += total_pot - geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[7]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] += total_pot - geld_einsatz[6]
        bank[7] -= geld_einsatz[7]

    elif name == spieler[8]:
        bank[0] -= geld_einsatz[0]
        bank[1] -= geld_einsatz[1]
        bank[2] -= geld_einsatz[2]
        bank[3] -= geld_einsatz[3]
        bank[4] -= geld_einsatz[4]
        bank[5] -= geld_einsatz[5]
        bank[6] -= geld_einsatz[6]
        bank[7] += total_pot - geld_einsatz[7]


# Funktionen zum plotten
def secret(name):
    fig, ax = plt.subplots()

    # karten definieren
    karte1 = beschriftung(name[0])
    karte2 = beschriftung(name[1])

    print("    ", name[0], "    --    ", name[1])

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='white')

    # place a text box in upper left in axes coords
    ax.text(0.02, 0.95, karte1, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.4, 0.95, karte2, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    plt.axis("off")
    plt.show()


def beschriftung(karte):
    teile = list(karte)

    if len(teile) == 3:
        karte = (
            f"{teile[2]} \n\n"
            f"    {teile[0]}    \n\n"
            f"         {teile[2]}"
        )
    else:
        karte = (
            f"{teile[2] + teile[3]}\n\n"
            f"    {teile[0]}    \n\n"
            f"       {teile[2] + teile[3]}"
        )
    return karte


part = 2  # nehm immer die zweite Liste (dient zur Verwirrung)


def offenlegen(runde, karten_im_spiel, n_spieler):
    breite = np.arange(0, len(karten_im_spiel[part]))
    vergeben = np.array(alle_p[0:(2 * n_spieler)])
    rest = np.isin(breite, vergeben)
    for same in range(0, rest.size):
        rest[same] = not rest[same]
    rest = list(breite[rest])

    nullte = "   "
    erste = karten_im_spiel[part][rest[0]]
    zweite = karten_im_spiel[part][rest[1]]
    dritte = karten_im_spiel[part][rest[2]]
    vierte = karten_im_spiel[part][rest[3]]
    fuenfte = karten_im_spiel[part][rest[4]]

    fig, ax = plt.subplots()

    # karten definieren
    if runde == "null":
        karte1 = beschriftung(nullte)
        karte2 = beschriftung(nullte)
        karte3 = beschriftung(nullte)
        karte4 = beschriftung(nullte)
        karte5 = beschriftung(nullte)

    elif runde == "flop":

        karte1 = beschriftung(erste)
        karte2 = beschriftung(zweite)
        karte3 = beschriftung(dritte)
        karte4 = beschriftung(nullte)
        karte5 = beschriftung(nullte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte)

    elif runde == "turn":
        karte1 = beschriftung(erste)
        karte2 = beschriftung(zweite)
        karte3 = beschriftung(dritte)
        karte4 = beschriftung(vierte)
        karte5 = beschriftung(nullte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte)
    elif runde == "river":
        karte1 = beschriftung(erste)
        karte2 = beschriftung(zweite)
        karte3 = beschriftung(dritte)
        karte4 = beschriftung(vierte)
        karte5 = beschriftung(fuenfte)
        print("    ", erste, "   --   ", zweite,
              "   --   ", dritte, "   --   ", vierte,
              "    --    ", fuenfte)

    else:
        raise Exception("Wrong Argument. Use null, flop, turn or river ")

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='white')

    # place a text box in upper left in axes coords
    ax.text(0, 0.95, karte1, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.35, 0.95, karte2, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(0.7, 0.95, karte3, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(1.05, 0.95, karte4, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    ax.text(1.4, 0.95, karte5, transform=ax.transAxes, fontsize=24,
            verticalalignment='top', bbox=props)
    plt.axis("off")
    plt.show()


# check Kontolimit
def check_konto_limit(bank, geld_einsatz):
    if (bank[0] - geld_einsatz[0] or bank[1] - geld_einsatz[1]
            or bank[2] - geld_einsatz[2] or bank[3] - geld_einsatz[3]
            or bank[4] - geld_einsatz[4] or bank[5] - geld_einsatz[5]
            or bank[6] - geld_einsatz[6] or bank[7] - geld_einsatz[7]):
        print("Spieler hat nicht mehr genug Geld auf dem Konto")
    else:
        print("Go")


# check Konto waehrend des Spiels
def check_konto_zwischenstand(bank, geld_einsatz):
    print("Spieler1: ", bank[0] - geld_einsatz[0],
          "Spieler2: ", bank[1] - geld_einsatz[1],
          "Spieler3: ", bank[2] - geld_einsatz[2],
          "Spieler4: ", bank[3] - geld_einsatz[3],
          "Spieler5: ", bank[4] - geld_einsatz[4],
          "Spieler6: ", bank[5] - geld_einsatz[5],
          "Spieler7: ", bank[6] - geld_einsatz[6],
          "Spieler8: ", bank[7] - geld_einsatz[7])


# bestimme wer die Blinds hat und wer anfaengt
def big_blind(bb, n_spieler):
    if n_spieler - bb < 0:
        bb = 1
    return bb


def beginn(bb, n_spieler):
    if n_spieler - bb < -1:
        bb = 2
    elif n_spieler - bb < 0:
        bb = 1
    return bb


# zweiter Part von Liste alle_karten ist nur interessant. Der Rest
# dient nur zur Verwirrung
def alle_karten(seed, n_spieler, offene_karten):
    random.seed(seed)
    spiel_karten_plus = [random.sample(karten, 15),
                         random.sample(karten, n_spieler * 2 + offene_karten),
                         random.sample(karten, 15)]
    return spiel_karten_plus


# printe aktuelle Kontostaende
def aktueller_stand(spieler, bank, n_spieler):
    stand = {}
    for index in range(0, n_spieler):
        stand[f"{spieler[index + 1]}"] = int(bank[index])
    print(stand)
