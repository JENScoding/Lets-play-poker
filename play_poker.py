import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from IPython.display import clear_output

# Passwoerter
mult = 528
passwort_seed = random.seed(42)
gen_passwoerter = []
for index in range(16):
    num = np.arange(2, 5 + index)
    comp = [not x for x in np.isin(num, gen_passwoerter)]
    num = random.sample(tuple(num[comp]), 1)
    gen_passwoerter.append(num[0])
alle_p = np.array(gen_passwoerter) * mult
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


# vor dem start Spieleranzahl, -namen etc festlegen
def anzahl_spieler():
    read = input("Anzahl Spieler: ")
    return int(read)


def spieler_namen(n_spieler):
    spieler = ["Spieler: ", "", "", "", "", "", "", "", ""]
    for ind in range(1, (n_spieler + 1)):
        spieler[ind] = input(f"Name von Spieler {ind}: ")
    return tuple(spieler)


def spieler_nummer(name, spieler, n_spieler):
    spieler_dict = {}
    for ind in range(1, (n_spieler + 1)):
        spieler_dict[f"{spieler[ind]}"] = ind
    return spieler_dict[name]


def dict_spieler(spieler, n_spieler):
    spieler_dict = {}
    for ind in range(1, (n_spieler + 1)):
        spieler_dict[ind] = spieler[ind]
    return spieler_dict


def dein_name(spieler, n_spieler):
    name = input("Gebe deinen Namen ein: ")
    print("\nDu hast die Spielernummer ", spieler_nummer(name, spieler, n_spieler))
    return name


def enter_password():
    pas1 = input("Erster Teil des Passworts: ")
    pas2 = input("Zweiter Tel des Passworts: ")
    return int(pas1), int(pas2)


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

    print("\nPot: ", int(t_pot))

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


part = 1  # nehm immer die zweite Liste (dient zur Verwirrung)


def offenlegen(runde, karten_im_spiel, n_spieler):
    breite = np.arange(0, len(karten_im_spiel[part]))
    vergeben = np.array(alle_p[0:(2 * n_spieler)]) / mult
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
    if (bank[0] - geld_einsatz[0] < 0
            or bank[1] - geld_einsatz[1] < 0
            or bank[2] - geld_einsatz[2] < 0
            or bank[3] - geld_einsatz[3] < 0
            or bank[4] - geld_einsatz[4] < 0
            or bank[5] - geld_einsatz[5] < 0
            or bank[6] - geld_einsatz[6] < 0
            or bank[7] - geld_einsatz[7] < 0):
        message = "stop"
    else:
        message = "go"

    return message


# check Konto waehrend des Spiels
def check_konto_zwischenstand(spieler, bank, geld_einsatz, n_spieler):
    stand = {}
    for index in range(0, n_spieler):
        stand[f"{spieler[index + 1]}"] = (
                int(bank[index]) - int(geld_einsatz[index]))
    print(stand)


# bestimme wer die Blinds hat
def big_blind(bb, n_spieler):
    if n_spieler - bb < 0:
        bb = 1
    return bb


# zweiter Part von Liste karten_ziehen ist nur interessant. Der Rest
# dient nur zur Verwirrung
def karten_ziehen(seed, n_spieler, offene_karten):
    random.seed(seed)
    spiel_karten_plus = [random.sample(karten, 15),
                         random.sample(karten, n_spieler * 2 + offene_karten),
                         random.sample(karten, 15)]
    return spiel_karten_plus


# ziehe Karten mit Seed
def set_seed():
    seed = int(np.random.randint(1, 9999, 1))
    plt.text(0, 0.8, "New seed:", size=50, color="orange")
    plt.text(0, 0.3, seed, size=100, color="orange")
    plt.axis("off");
    return seed


def enter_seed(n_spieler, offene_karten, passwort):
    read = input("Seed: ")
    seed = int(read)
    karte1 = karten_ziehen(seed, n_spieler, offene_karten)[part][int(passwort[0] / mult)]
    karte2 = karten_ziehen(seed, n_spieler, offene_karten)[part][int(passwort[1] / mult)]
    return karte1, karte2


# Einsaetze legen
def bieten(geld_einsatz, erster, spieler, n_spieler, spieler_dict, fold, bank, small_b):
    start = spieler_nummer(erster, spieler, n_spieler)
    vorheriger = []
    for index in range(n_spieler):
        if index + start - n_spieler > 0:
            gehe_zu = index + start - n_spieler
        else:
            gehe_zu = start + index

        if fold[(gehe_zu - 1)]:
            state = "out"
        else:
            read = input(f"{spieler_dict[gehe_zu]}: ")
            if read == "fold":
                fold[(gehe_zu - 1)] = True
                state = geld_einsatz[(gehe_zu - 1)][0]
            elif read == "check":
                state = geld_einsatz[(gehe_zu - 1)][0]
            elif index > 0 and (any(np.array(vorheriger) > int(read)) or
                                int(read) < small_b):
                raise Exception("Einsatz zu niedrig!")
            else:
                geld_einsatz[(gehe_zu - 1)] += int(read)
                vorheriger.append(int(read))

                message = check_konto_limit(bank, geld_einsatz)
                if message == "stop":
                    geld_einsatz[(gehe_zu - 1)] -= int(read)
                    raise Exception(f"{spieler_dict[gehe_zu]} hat nicht"
                                    f" mehr genug Geld auf dem Konto!"
                                    f" Der Einsatz muss"
                                    f" neu festgelegt werden!")

                state = geld_einsatz[(gehe_zu - 1)][0]

        print(f"Einsatz insgesamt {spieler_dict[index + 1]}: {state}")

    print("\nGo\n")

    return geld_einsatz


# printe aktuelle Kontostaende
def aktueller_stand(spieler, bank, n_spieler, start_geld):
    stand = {}
    for index in range(0, n_spieler):
        stand[f"{spieler[index + 1]}"] = int(bank[index])
    print(stand)
    if np.sum(bank) != start_geld * 8:
        print("Summe aller Konten ist nicht mehr",
              start_geld * 8, "-> Fehlerhafte Eingabe!")


# wer hat welche blinds
def info_blinds(spieler, spiel_runde, n_spieler, small_b, big_b):
    small_blind = spieler[spiel_runde]
    print("Small Blind: ", small_blind, " -> ", small_b)
    big_blind_sp = spieler[big_blind(spiel_runde + 1, n_spieler)]
    print("Big Blind:   ", big_blind_sp, " -> ", big_b)
    print("Beginn:      ", small_blind)
    return small_blind


# einmal die scheibe drehen lassen
def clock(angle=0, ax=None):
    circle1 = plt.Circle((2, 2), 1, color="black", fill=False)
    rec1 = mpatches.Rectangle((1.5, 3), 1, 0.5)
    rec2 = mpatches.Rectangle((1.95, 3), 0.1, -0.5, color="red")
    my_col = ["green", "blue", "orange", "red", "brown", "magenta"]
    degrees = []
    for index in range(0, 13):
        degrees.append(index * 30 - angle * 30)
    wedge_odd = []
    for index in [0, 2, 4, 6, 8, 10]:
        wedge_odd.append(mpatches.Wedge((2, 2), 1,
                                        degrees[index] - 15,
                                        degrees[index + 1] - 15,
                                        fc=my_col[int(index / 2)],
                                        hatch="O"))
    wedge_yel = []
    for index in [1, 3, 5, 7, 9, 11]:
        wedge_yel.append(mpatches.Wedge((2, 2), 1,
                                        degrees[index] - 15,
                                        degrees[index + 1] - 15,
                                        fc="yellow",
                                        hatch=""))
    plt.text(np.sin(angle * 2 * np.pi / 12) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12) * 0.9 + 1.98, "12",
             rotation=angle * -30,
             size=12, color="orange")
    plt.text(np.sin(angle * 2 * np.pi / 12 - np.pi) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12 - np.pi) * 0.9 + 1.98, "6",
             rotation=angle * -30 + 180,
             size=12, color="orange")
    plt.text(np.sin(angle * 2 * np.pi / 12 - 1 / 3 * np.pi) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12 - 1 / 3 * np.pi) * 0.9 + 1.98, "10",
             rotation=angle * -30 + 60,
             size=12, color="orange")
    plt.text(np.sin(angle * 2 * np.pi / 12 - 2 / 3 * np.pi) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12 - 2 / 3 * np.pi) * 0.9 + 1.98, "8",
             rotation=angle * -30 + 120,
             size=12, color="orange")
    plt.text(np.sin(angle * 2 * np.pi / 12 + 2 / 3 * np.pi) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12 + 2 / 3 * np.pi) * 0.9 + 1.98, "4",
             rotation=angle * -30 - 120,
             size=12, color="orange")
    plt.text(np.sin(angle * 2 * np.pi / 12 + 1 / 3 * np.pi) * 0.75 + 1.9,
             np.cos(angle * 2 * np.pi / 12 + 1 / 3 * np.pi) * 0.9 + 1.98, "2",
             rotation=angle * -30 - 60,
             size=12, color="orange")
    my_wedges = wedge_odd + wedge_yel
    my_wedges.append(circle1)
    my_wedges.append(rec1)
    my_wedges.append(rec2)
    for wedge in my_wedges:
        ax.add_artist(wedge)
    return my_wedges


def rotating_disc(min_spins=100000, max_spins=150000):
    nn = np.random.randint(min_spins, max_spins, 1)[0]
    for rollen in range(1, nn):
        wurf_1 = np.random.randint(1, 13, 1)
        if (rollen / 5000).is_integer():
            fig, ax = plt.subplots()
            clock(angle=wurf_1[0], ax=ax)
            ax.set_xlim([0, 4])
            ax.set_ylim([0, 4])
            ax.axis('equal')
            plt.axis("off")
            plt.show()
            clear_output(wait=True)
        else:
            continue
