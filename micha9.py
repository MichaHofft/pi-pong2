from PiPongBasis import ZeichenKarte, PixelKarte, SpielBasis, Spieler
import random
import math

class Geist(Spieler):

    def Start(self):
        self.SetzeGroesse(5,5)
        self.SetzePosition(32,32)
        self.SetzeGeschwidigkeit(0.09,0.11)
        self.SetzeLeitplanken(0, 63, 0, 63)
        self.ModusFrei()
        self.kachel = None

    def Male(self,x,y):
        print(x,y)
        # self.basis.MaleBlock(x,y,x+4,y+4, self.basis.FarbeBlauIntensiv)
        self.basis.MaleSprite(x,y,self.kachel)

class Pacman(SpielBasis):

    def SpielStart(self):
        pmk = PixelKarte("pacman-kacheln5x5v2.bmp")
        pmkInit = "QWERTZUJabcd.* -|OLKIYXCV+~"
        pacmanKacheln = {}
        for i in range(len(pmkInit)):
            pacmanKacheln[pmkInit[i]] = pmk.TeilBild(6*i,0, 5,5)
        welt = ZeichenKarte(11,13, [ 
            "I-----------O", 
            "|...........|", 
            "|.I-O.-----.|", 
            "|.K-L.......|", 
            "|.....I---O.|", 
            "|.I---X---L.|", 
            "|.|.........|", 
            "|.|.I--O...-Y", 
            "|.|.K--L.|ab|", 
            "|........|cd|", 
            "K--------X--L"
            ])
        self.WeltKarte = PixelKarte(64,64)
        self.WeltKarte.BaueVonZeichenKarte(pacmanKacheln, welt, 5,5)
        self.WeltKarte.SchreibeBild("e.bmp")

        self.x = 0

        blinky = Geist()
        blinky.kachel = pacmanKacheln['a']
        self.AddiereSpieler(blinky)

    def SpielBerechneEinBild(self):

        if False:
            self.MaleBlock(self.x,0,self.x+5,63, self.FarbeBlauIntensiv)
            self.x = self.x + 1
            if self.x > 58:
                self.x = 0

        if False:
            self.MaleSprite(0,0,self.WeltKarte)

# TEST

class TestSpielBasis(SpielBasis):

    BIT_OBEN = 0x01
    BIT_UNTEN = 0x02
    BIT_LINKS = 0x04
    BIT_RECHTS = 0x08
    BIT_BODEN = 0x10
    BIT_PUNKT = 0x20
    BIT_WUMMS = 0x40

    def SpielStart(self):        
        
        self.WeltKarte = PixelKarte(64,64)
        
        self.WeltDaten = [
            [ 0x25, 0x23, 0x23, 0x21, 0x23, 0x23, 0x23, 0x29, 0x1C, 0x25, 0x23, 0x23 ],
            [ 0x4C, 0x15, 0x19, 0x2C, 0x15, 0x11, 0x19, 0x2C, 0x1C, 0x2C, 0x15, 0x11 ],
            [ 0x2C, 0x16, 0x1A, 0x2C, 0x16, 0x12, 0x1A, 0x2C, 0x1E, 0x2C, 0x16, 0x12 ],
            [ 0x24, 0x23, 0x23, 0x20, 0x23, 0x21, 0x23, 0x22, 0x23, 0x22, 0x23, 0x21 ],
            [ 0x2C, 0x17, 0x1B, 0x2C, 0x1D, 0x2C, 0x17, 0x13, 0x11, 0x13, 0x1B, 0x2C ],
            [ 0x26, 0x23, 0x23, 0x28, 0x1C, 0x26, 0x23, 0x29, 0x1C, 0x25, 0x23, 0x2A ],
            [ 0x11, 0x11, 0x19, 0x2C, 0x14, 0x13, 0x1B, 0x2C, 0x1E, 0x2C, 0x17, 0x13 ],
            [ 0x10, 0x10, 0x18, 0x2C, 0x1C, 0x25, 0x23, 0x22, 0x21, 0x22, 0x23, 0x29 ],
            [ 0x12, 0x12, 0x1A, 0x2C, 0x1E, 0x2C, 0x15, 0x11, 0x00, 0x11, 0x19, 0x2C ],
            [ 0x23, 0x23, 0x23, 0x20, 0x23, 0x28, 0x14, 0x00, 0x00, 0x00, 0x18, 0x24 ],
            [ 0x11, 0x11, 0x19, 0x2C, 0x1D, 0x2C, 0x16, 0x12, 0x12, 0x12, 0x1A, 0x2C ],
            [ 0x10, 0x10, 0x18, 0x2C, 0x1C, 0x24, 0x23, 0x23, 0x23, 0x23, 0x23, 0x28 ] ]

        self.WeltZeilen = 12
        self.WeltSpalten = 12
        self.KachelBreite = 5
        self.KachelHoehe = 5

        pmk = PixelKarte("/home/pi/ada2/pi-pong/pacman-kacheln5x5v3.bmp")
        self.Punkt = pmk.TeilBild(6*13,0, 5,5)        
        self.Wumms = pmk.TeilBild(6*14,0, 5,5)

        self.PacmanBilder = [
            pmk.TeilBild(6*0,0, 5,5),
            pmk.TeilBild(6*1,0, 5,5),
            pmk.TeilBild(6*2,0, 5,5),
            pmk.TeilBild(6*3,0, 5,5),
            pmk.TeilBild(6*4,0, 5,5),
            pmk.TeilBild(6*5,0, 5,5),
            pmk.TeilBild(6*6,0, 5,5),
            pmk.TeilBild(6*7,0, 5,5),
        ]

        self.GeistBilder = [
            pmk.TeilBild(6*8,0, 5,5),
            pmk.TeilBild(6*12,0, 5,5),
            pmk.TeilBild(6*9,0, 5,5),
            pmk.TeilBild(6*12,0, 5,5),
            pmk.TeilBild(6*10,0, 5,5),
            pmk.TeilBild(6*12,0, 5,5),
            pmk.TeilBild(6*11,0, 5,5),
            pmk.TeilBild(6*12,0, 5,5),
        ]

        self.FontKlein = self.LadeFont("../rpi-rgb-led-matrix/fonts/5x7.bdf")

        self.SeriellOeffnen()
        self.Lotsen = self.LeereLotsen()

    def StartPunkt(self, zeile, spalte):
        # alle koordinaten fangen bei (1,1) an, damit man links noch platz hat
        xs = 1 + self.KachelBreite * spalte
        ys = 1 + self.KachelHoehe * zeile 
        return xs, ys

    def MaleKachelBoden(
            self, spiel : SpielBasis, bande, farbe, zeile, spalte, 
            form, formOben, formUnten, formLinks, formRechts):

        xs, ys = self.StartPunkt(zeile, spalte) 
        xsb = xs + bande
        ysb = ys + bande

        xe = xs + self.KachelBreite
        ye = ys + self.KachelHoehe
        xeb = xe - bande
        yeb = ye - bande

        # male nur fuer umgebungskacheln

        if form & self.BIT_BODEN > 0:

            if form & self.BIT_OBEN > 0:
                spiel.MaleLinie(
                    xsb if formLinks & 0x10 == 0 else xs, ysb, 
                    xeb if formRechts & 0x10 == 0 else xe, ysb, farbe)

            if form & self.BIT_UNTEN > 0:
                spiel.MaleLinie(
                    xsb if formLinks & 0x10 == 0 else xs, yeb, 
                    xeb if formRechts & 0x10 == 0 else xe, yeb, farbe)

            if form & self.BIT_LINKS > 0:
                spiel.MaleLinie(
                    xsb, ysb if formOben & 0x10 == 0 else ys, 
                    xsb, yeb if formUnten & 0x10 == 0 else ye, farbe)

            if form & self.BIT_RECHTS > 0:
                spiel.MaleLinie(
                    xeb, ysb if formOben & 0x10 == 0 else ys, 
                    xeb, yeb if formUnten & 0x10 == 0 else ye, farbe)

        # male nur fuer gangkacheln

        if form & self.BIT_BODEN == 0:

            if spalte == 0:
                spiel.MaleLinie(xs - 1, ys, xs - 1, ye, farbe)

            if spalte >= self.WeltSpalten - 1:
                spiel.MaleLinie(xe + 1, ys, xe + 1, ye, farbe)

            if zeile == 0:
                spiel.MaleLinie(xs, ys - 1, xe, ys - 1, farbe)
            
            if zeile >= self.WeltZeilen - 1:
                spiel.MaleLinie(xs, ye + 1, xe, ye + 1, farbe)

    def MaleWeltBoden(self, bande, farbe):
        for z in range(0, self.WeltZeilen):
            for s in range(0, self.WeltSpalten):
                self.MaleKachelBoden(
                    self, bande, farbe, z, s, 
                    self.WeltDaten[z][s],
                    self.WeltDaten[z - 1][s] if z > 0 else 0x10,
                    self.WeltDaten[z + 1][s] if z < self.WeltSpalten-1 else 0x10,
                    self.WeltDaten[z][s - 1] if s > 0 else 0x10,
                    self.WeltDaten[z][s + 1] if s < self.WeltZeilen-1 else 0x10)

    def MaleWeltSachen(self):
        for z in range(0, self.WeltZeilen):
            for s in range(0, self.WeltSpalten):
                
                form = self.WeltDaten[z][s]
                xs, ys = self.StartPunkt(z, s) 
                
                if form & self.BIT_PUNKT > 0:
                    self.MaleSprite(xs + 1, ys + 1, self.Punkt)

                if form & self.BIT_WUMMS > 0:
                    self.MaleSprite(xs + 1, ys + 1, self.Wumms)


class Aktor:

    RICHT_LINKS = 0
    RICHT_UNTEN = 1
    RICHT_RECHTS = 2
    RICHT_OBEN = 3

    def __init__(self, spiel : TestSpielBasis, zeile, spalte, richt):
        self.Spiel = spiel
        self.Richtung = richt
        self.Zeile = zeile
        self.Spalte = spalte
        self.Geschwind = 2.0
        self.Phase = 0

        self.Ticks = 0
        self.Blink = False

        self.Richts = [self.RICHT_LINKS, self.RICHT_UNTEN, self.RICHT_RECHTS, self.RICHT_OBEN]
        self.AntiRicht = [self.RICHT_RECHTS, self.RICHT_OBEN, self.RICHT_LINKS, self.RICHT_UNTEN]

    """ Male Aktor an aktueller Position. Sollte in Unterklassen ueberladen werden """
    def Male(self):
        pass

    """ Schalte eine Zeiteinheit weiter. Aktualisere Bilder und Positionen """
    def Ticke(self):

        # neue Richtung einschlagen?
        (nr, ng) = self.CheckNeueRichtung()
        if nr >= 0 and nr != self.Richtung:
            
            # tricky: Wechsel von X auf Y oder umgekehrt
            x0, y0 = self.Normvektor(self.Richtung)
            x1, y1 = self.Normvektor(nr)

            if abs(x0) != abs(x1) or abs(y0) != abs(y1):
                # X/Y Wechsel .. erlaube das nur an ganzen Zeilen/ Spalten
                if self.Phase <= 0.2 or self.Phase >= 0.8:
                    # merke die alte Posi
                    ozs = (self.Zeile, self.Spalte)
                    # wenn weit vorgedrungen, aktualisiere Zeile/ Spalte auf nächste Positon
                    if self.Phase >= 0.8:
                        self.Zeile += int(y0)
                        self.Spalte += int(x0)

                    # teste hier auf Kollisionen        
                    kolls = self.TestKollisionen()
                    if nr in kolls:
                        # wickle wieder zurück
                        (self.Zeile, self.Spalte) = ozs
                    else:
                        # schlage wirklich von der (alten/ neuen) Zeilen/ Spalten Posi 
                        # eine neue Richtung ein
                        self.Phase = 0.0
                        self.Richtung = nr
            else:
                # gegenläufig
                self.Phase = 1.0 - self.Phase

                # damit muss auch Zeile/ Spalte angepasst werden
                self.Zeile += int(y0)
                self.Spalte += int(x0)

                # neue Richtung behalten
                self.Richtung = nr

            # statte Pacman wieder mit Geschwindigkeit aus
            self.Geschwind = ng

        # (alte) Richtung fortschreiben
        self.Ticks = (self.Ticks + 1) % 50
        self.Blink = self.Ticks > 25
        self.Phase += 0.02 * self.Geschwind
        if self.Phase >= 1.0:
            xn, yn = self.Normvektor(self.Richtung)
            self.Zeile += int(yn)
            self.Spalte += int(xn)
            self.Phase = 0.0
            self.SchrittGetan()

    def Normvektor(self, richt):
        if richt == self.RICHT_LINKS:
            return -1.0, 0.0
        if richt == self.RICHT_UNTEN:
            return 0.0, 1.0
        if richt == self.RICHT_RECHTS:
            return 1.0, 0.0
        if richt == self.RICHT_OBEN:
            return 0.0, -1.0    
        return 0.0, 0.0

    def PixelPos(self):
        xs, ys = self.Spiel.StartPunkt(self.Zeile, self.Spalte)
        xn, yn = self.Normvektor(self.Richtung)

        xs += xn * self.Phase * self.Spiel.KachelBreite
        ys += yn * self.Phase * self.Spiel.KachelHoehe

        return int(xs), int(ys)

    """ Checkt für die aktuelle Positionen die Kollisionen mit umliegenden Wänden.
        Gibt eine Liste von Richtungen zurück, die BLOCKIERT sind. """
    def TestKollisionen(self):
        res = []

        if self.Spalte >= self.Spiel.WeltSpalten - 1 or self.Spiel.WeltDaten[self.Zeile][self.Spalte + 1] & self.Spiel.BIT_BODEN > 0:
            res.append(self.RICHT_RECHTS)

        if self.Spalte <= 0 or self.Spiel.WeltDaten[self.Zeile][self.Spalte - 1] & self.Spiel.BIT_BODEN > 0:
            res.append(self.RICHT_LINKS)

        if self.Zeile >= self.Spiel.WeltZeilen - 1 or self.Spiel.WeltDaten[self.Zeile + 1][self.Spalte] & self.Spiel.BIT_BODEN > 0:
            res.append(self.RICHT_UNTEN)

        if self.Zeile <= 0 or self.Spiel.WeltDaten[self.Zeile - 1][self.Spalte] & self.Spiel.BIT_BODEN > 0:
            res.append(self.RICHT_OBEN)

        return res

    """ Wird aufgerufen, nachdem ein ganzer Gross-Schritt getan wurde """
    def SchrittGetan(self):
        pass

    """ Checkt an jedem kleinen Pixel-Schritt, ob eine NEUE Richtung eingeschlagen werden soll.
        Gibt auch die Geschwindigkeit rerück
        Gibt sonst (-1, 1.0) zurueck """
    def CheckNeueRichtung(self):
        return (-1, 1.0)


class AktorPacman(Aktor):

    def __init__(self, spiel : TestSpielBasis, zeile, spalte, richt):
        # normaler Aktor
        super().__init__(spiel, zeile, spalte, richt)
        self.NormGeschwind = 2.0

    def Male(self, spiel : TestSpielBasis):
        bild = spiel.PacmanBilder[2 * self.Richtung + (1 if self.Blink else 0)]
        xs, ys = self.PixelPos()
        spiel.MaleSprite(xs, ys, bild)

    """ Laeuft in eine Richtung undstoppt wenn es nicht weitergeht """
    def SchrittGetan(self):
        
        kolls = self.TestKollisionen()
        if self.Richtung in kolls:
            self.Geschwind = 0.0

    def CheckNeueRichtung(self):

        if self.Spiel.Lotsen[0].Links:
            return (self.RICHT_LINKS, self.NormGeschwind)

        if self.Spiel.Lotsen[0].Rechts:
            return (self.RICHT_RECHTS, self.NormGeschwind)

        if self.Spiel.Lotsen[0].Oben:
            return (self.RICHT_OBEN, self.NormGeschwind)

        if self.Spiel.Lotsen[0].Unten:
            return (self.RICHT_UNTEN, self.NormGeschwind)

        return (-1, 1.0)


class AktorGeist(Aktor):

    BLINKY = 0
    PINKY = 1
    INKY = 2
    CLYDE = 3

    MODUS_VERHALTEN = 0
    MODUS_WANDERN = 1
    MODUS_ANGST = 2

    MODUS_KURZ = ["Fo", "Wa", "An" ]

    def __init__(self, spiel : TestSpielBasis, zeile, spalte, richt, rolle):
        # normaler Aktor
        super().__init__(spiel, zeile, spalte, richt)
        # Rolle
        self.Rolle = rolle
        # etwas langsamer 
        self.Geschwind *= 0.8
        # erstmal nicht verletztlich
        self.Modus = self.MODUS_VERHALTEN
        self.ZielModus = False
        self.ZielZ = 0
        self.ZielS = 0
        self.Angst = False        

    def Male(self, spiel : TestSpielBasis):
        bild = spiel.GeistBilder[2 * self.Rolle + (1 if self.Angst else 0)]
        xs, ys = self.PixelPos()
        spiel.MaleSprite(xs, ys, bild)

    """ Euklidische Distanz """
    def Distanz(self, z1, s1, z2, s2):
        return math.sqrt((z2-z1)**2 + (s2-s1)**2)

    """ Laeuft selbststaendig hin und her und nimmt Abzweigungen """
    def SchrittGetan(self):

        # wo dürfen wir nicht hin?
        kolls = self.TestKollisionen()

        # stehen wir direkt vor einer Wand?
        vorWand = self.Richtung in kolls

        # Sammeln von Moeglichkeiten von Richtung
        mglRicht = []

        # kommen wir an einem Abzweig vorbei?
        # wir koennen jede Richtung nehmen, die NICHT rueckwarts fuehrt
        kolls = self.TestKollisionen()
        for r in self.Richts:
            # fuehrt zu einer Kollision?
            if r in kolls:
                continue
            # wir vermeiden, direkt umzudrehen, ausser wir stehen vor einer Wand
            antiRicht = r == self.AntiRicht[self.Richtung]
            if (not vorWand) and antiRicht:
                continue
            # Super spezial: Eingang in Hoehle verhindern
            if self.Zeile == 7 and self.Spalte == 8 and r == self.RICHT_UNTEN:
                continue
            # Bewertung
            nv = self.Normvektor(r)            
            bewert = 0.0 + self.Distanz(self.Zeile + int(nv[1]), self.Spalte + int(nv[0]), self.ZielZ, self.ZielS)
            # gilt als Moeglichkeit
            mglRicht.append ((r, bewert))
            if not antiRicht:
                # 2 x dazu, um wahrscheinlicher *nicht* die Richtung wechseln
                mglRicht.append ((r, bewert))

        # Reissleine
        if len(mglRicht) < 1:
            self.Geschwind = 0.0
            return

        # OK, mindestens 2 Moeglichkeiten die wir nutzen koennen
        if self.ZielModus:
            
            # Zielmodus
            # Sortieren mittels Lambda
            mglRicht.sort(key=lambda x: x[1])

            # das Beste nehmen
            self.Richtung = mglRicht[0][0]

        else:
            # mehr nach Zufall
            nexti = random.randint(0, len(mglRicht) - 1)
            self.Richtung = mglRicht[nexti][0]

        # hoffentlich fein ..
        pass
    
    def GeheModus(self, modus):
        """ Schaltet um in einen neuen Modus """
        # merken
        self.Modus = modus
        # umschalten
        if modus == self.MODUS_WANDERN:
            self.ZielModus = True
            self.Angst = False
            # die einzelnen Ziele sind nicht ganz intuitiv nach der Reihenfolge der Geister
            self.ZielZ, self.ZielS = (0, spiel.WeltSpalten-1)
            if self.Rolle == self.PINKY:
                self.ZielZ, self.ZielS = (0,0)
            if self.Rolle == self.INKY:
                self.ZielZ, self.ZielS = (spiel.WeltZeilen-1, spiel.WeltSpalten-1)
            if self.Rolle == self.CLYDE:
                self.ZielZ, self.ZielS = (spiel.WeltZeilen-1, 4)
            return

        if modus == self.MODUS_ANGST:
            self.ZielModus = False
            self.Angst = True
            return

        # sonst: normales Verhalten
        # auch hier arbeiten wir im Zielmodus, ausser fuer Inky, der läuft frei
        self.ZielModus = self.Rolle != self.INKY
        self.Angst = False

    def AktualisiereModus(self, pacZ, pacS, pacRicht):
        """ Laufende Aktualisierung des Modus """
        if self.Modus == self.MODUS_VERHALTEN:
            
            d = self.Distanz(self.Zeile, self.Spalte, pacZ, pacS)
            
            if self.Rolle == self.BLINKY:
                # Blinky folgt immer Pacman
                self.ZielZ, self.ZielS = pacZ, pacS
            if self.Rolle == self.PINKY:
                # Pinky laeuft immer dorthin, wo Packman in 4 Kacheln sein wird
                nv = self.Normvektor(pacRicht)
                self.ZielZ = max(0, min(self.Spiel.WeltZeilen - 1, pacZ + 4 * int(nv[1])))
                self.ZielS = max(0, min(self.Spiel.WeltSpalten - 1, pacS + 4 * int(nv[0])))
            if self.Rolle == self.INKY:
                pass
            if self.Rolle == self.CLYDE:
                # Wenn Distanz > 8 dann wie Blinky, sonst in die eigene Homebase
                if d > 8.0:
                    self.ZielZ, self.ZielS = pacZ, pacS
                else:
                    self.ZielZ, self.ZielS = (spiel.WeltZeilen-1, 4)

class TestSpielLogik(TestSpielBasis):

    # fuer die Logik siehe: https://gameinternals.com/understanding-pac-man-ghost-behavior
    # und: https://www.gamedeveloper.com/design/the-pac-man-dossier
    # und: https://dev.to/code2bits/pac-man-patterns--ghost-movement-strategy-pattern-1k1a

    def SpielStart(self):
        # Konstruktor von Super Klasse
        TestSpielBasis.SpielStart(self)    

        # Alle Aktoren in einem Array, Pacman zuletzt
        self.Aktoren = [            
            AktorGeist(self, 7,4, Aktor.RICHT_OBEN, AktorGeist.BLINKY),
            AktorGeist(self, 9,8, Aktor.RICHT_OBEN, AktorGeist.PINKY),
            AktorGeist(self, 9,7, Aktor.RICHT_OBEN, AktorGeist.INKY),
            AktorGeist(self, 9,9, Aktor.RICHT_OBEN, AktorGeist.CLYDE),
            AktorPacman(self, 0,0,Aktor.RICHT_RECHTS)
        ]

        self.GeistPhase = 0
        self.GeistModus = AktorGeist.MODUS_VERHALTEN

    def Pacman(self):
        return self.Aktoren[0]

    def MaleAktoren(self):
        for m in self.Aktoren:
            if m is not None:
                m.Ticke()
                m.Male(self)

    def SchalteGeistPhase(self):
        self.GeistPhase -= 5
        if self.GeistPhase < 0:

            # Zustandsmaschine
            if self.GeistModus == AktorGeist.MODUS_WANDERN:
                self.GeistModus = AktorGeist.MODUS_WANDERN
                self.GeistPhase = 7 * 200
            elif self.GeistModus == AktorGeist.MODUS_VERHALTEN:
                self.GeistModus = AktorGeist.MODUS_VERHALTEN
                self.GeistPhase = 7 * 200
            elif self.GeistModus == AktorGeist.MODUS_ANGST:
                self.GeistModus = AktorGeist.MODUS_WANDERN
                self.GeistPhase = 5 * 200

            # fuer alle Geister
            for m in self.Aktoren:
                if isinstance(m, AktorGeist):
                    m.GeheModus(self.GeistModus)

    def AktualisiereModi(self):

        # suche pacman
        pac = None
        for m in self.Aktoren:
            if isinstance(m, AktorPacman):
                pac = m

        # fuer alle Geister
        if pac is not None:
            for m in self.Aktoren:
                if isinstance(m, AktorGeist):
                    m.AktualisiereModus(pac.Zeile, pac.Spalte, pac.Richtung)

    def MaleTexte(self):
        xs, ys = self.StartPunkt(8,0)
        self.MaleText(self.FontKlein, xs + 1, ys + 1, self.FarbeGruenIntensiv, AktorGeist.MODUS_KURZ[self.GeistModus])

    def LeseSeriell(self):
        self.Lotsen = self.SeriellLeseLotsen()

        # dbg = "%0.4X" % self.Lotsen[2]
        # self.MaleText(self.FontKlein, 20, 20, self.FarbeWeiss, dbg)
    
    def SpielBerechneEinBild(self):
        self.MaleBlock(0,0,63,63, self.GebeFarbe(0, 40, 0))
        
        # self.MaleWeltBoden(2, self.GebeFarbe(0, 100, 100))
        self.MaleWeltBoden(1, spiel.FarbeWeiss)

        self.MaleWeltSachen()

        self.LeseSeriell()

        self.MaleAktoren()

        self.SchalteGeistPhase()

        self.AktualisiereModi()

        self.MaleTexte()

# Haupt-Funktion
if __name__ == "__main__":
    # Zufall starten

    random.seed()
    # spiel = Pacman()
    spiel = TestSpielLogik()
    if (not spiel.process()):
        pass
