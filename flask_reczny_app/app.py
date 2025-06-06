from flask import Flask, jsonify, redirect, render_template, request, flash, url_for
from durable.lang import *
import json
import requests
Dane='ss'
app = Flask(__name__)
# Inicjalizacja systemu reguł w Durable Rules
with ruleset('jaka_ktora_kierunek'):
    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Tak') & (m.jama_ustna == 'Tak'))
    def Stomatologia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Stomatologia', 'opis': 'Studia poświęcone zdrowiu jamy ustnej, leczeniu zębów i innych problemów stomatologicznych.', 'zdjecie': zdjecie['Stomatologia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Tak') & (m.jama_ustna == 'Nie'))
    def Lekarski(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Lekarski', 'opis': 'Studia przygotowujące do zawodu lekarza, obejmujące szeroką wiedzę medyczną i praktyki kliniczne.', 'zdjecie': zdjecie['Lekarski'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Nie') & (m.gdzie_pracowac == 'Karetka'))
    def Ratownictwo_medyczne(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Ratownictwo medyczne', 'opis': 'Studia przygotowujące do udzielania pierwszej pomocy i działania w sytuacjach kryzysowych.', 'zdjecie': zdjecie['Ratownictwo medyczne'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Tak') & (m.zywienie == 'Tak'))
    def Dietetyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Dietetyka', 'opis': 'Studia zajmujące się zdrowym żywieniem i dietoterapią dla różnych grup pacjentów.', 'zdjecie': zdjecie['Dietetyka'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Tak'))
    def Farmacja(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Farmacja', 'opis': 'Studia z zakresu tworzenia, produkcji i zastosowania leków oraz farmakologii.', 'zdjecie': zdjecie['Farmacja'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Tak') & (m.zywienie == 'Nie'))
    def Fizjoterapia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Fizjoterapia', 'opis': 'Studia z zakresu leczenia i rehabilitacji za pomocą ćwiczeń fizycznych i terapii manualnych.', 'zdjecie': zdjecie['Fizjoterapia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Nie') & (m.chemia_czy_biologia == 'Biologia'))
    def Biotechnologia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Biotechnologia', 'opis': 'Studia łączące biologię z technologią, skupiające się na wykorzystaniu organizmów i ich części do produkcji i badań.', 'zdjecie': zdjecie['Biotechnologia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Nie') & (m.chemia_czy_biologia == 'Chemia'))
    def Analityka_chemiczna(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Analityka chemiczna', 'opis': 'Studia skupiające się na technikach analizy chemicznej i identyfikacji substancji.', 'zdjecie': zdjecie['Analityka chemiczna'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Nie') & (m.zwierzeta == 'Tak') & (m.leczenie_zwierzat == 'Tak'))
    def Weterynaria(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Weterynaria', 'opis': 'Studia poświęcone zdrowiu i leczeniu zwierząt, zarówno domowych, jak i gospodarskich.', 'zdjecie': zdjecie['Weterynaria'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Nie') & (m.zwierzeta == 'Tak') & (m.leczenie_zwierzat == 'Nie') & (m.ekologia == 'Tak'))
    def Ochrona_srodowiska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Ochrona srodowiska', 'opis': 'Studia zajmujące się ochroną przyrody i zarządzaniem zasobami naturalnymi.', 'zdjecie': zdjecie['Ochrona srodowiska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Nie') & (m.zwierzeta == 'Tak') & (m.leczenie_zwierzat == 'Nie') & (m.ekologia == 'Nie'))
    def Zoologia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Zoologia', 'opis': 'Studia zajmujące się badaniem zwierząt, ich anatomii, ekologii i zachowań.', 'zdjecie': zdjecie['Zoologia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Nie') & (m.zwierzeta == 'Nie') & (m.podroze == 'Nie'))
    def Geodezja(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Geodezja', 'opis': 'Studia zajmujące się pomiarami i mapowaniem powierzchni ziemi.', 'zdjecie': zdjecie['Geodezja'] })
##
    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Nie') & (m.zwierzeta == 'Nie') & (m.podroze == 'Tak'))
    def Turystyka_i_Rekreacja(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Turystyka i rekreacja', 'opis': 'Studia przygotowujące do pracy w sektorze turystycznym i organizacji czasu wolnego.', 'zdjecie': zdjecie['Turystyka i rekreacja'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Tak') & (m.zainteresowania == 'Systemy komunikacji'))
    def Telekomunikacja(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Telekomunikacja', 'opis': 'Studia z zakresu technologii przesyłu informacji na odległość, w tym telefonii i internetu.', 'zdjecie': zdjecie['Telekomunikacja'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Tak') & (m.zainteresowania == 'Programy i aplikacje'))
    def Informatyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Informatyka', 'opis': 'Studia z zakresu programowania, tworzenia oprogramowania i zarządzania systemami komputerowymi.', 'zdjecie': zdjecie['Informatyka'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Tak') & (m.zainteresowania == 'Mechanika i robotyka'))
    def Mechatronika(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Mechatronika', 'opis': 'Studia łączące inżynierię mechaniczną, elektroniczną i informatyczną w celu projektowania i budowy inteligentnych systemów.', 'zdjecie': zdjecie['Mechatronika'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Tak') & (m.technika_czy_kreatywnosc == 'Technicznym'))
    def Budownictwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Budownictwo', 'opis': 'Studia z zakresu projektowania, wznoszenia i utrzymania budynków oraz infrastruktury.', 'zdjecie': zdjecie['Budownictwo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Tak') & (m.technika_czy_kreatywnosc == 'Kreatywnym'))
    def Architektura(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Architektura', 'opis': 'Studia zajmujące się projektowaniem budynków i przestrzeni, łączące sztukę z technologią.', 'zdjecie': zdjecie['Architektura'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Nie') & (m.finanse == 'Tak') & (m.przyszlosc_zawodowa == 'Jako analityk, doradca'))
    def Ekonomia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Ekonomia', 'opis': 'Studia z zakresu zarządzania zasobami, produkcją i dystrybucją dóbr oraz usług.', 'zdjecie': zdjecie['Ekonomia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Nie') & (m.finanse == 'Tak') & (m.przyszlosc_zawodowa == 'Jako ksiegowy'))
    def Finanse_i_rachunkowosc(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Finanse i rachunkowosc', 'opis': 'Studia zajmujące się zarządzaniem finansami, inwestycjami i księgowością.', 'zdjecie': zdjecie['Finanse i rachunkowosc'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Nie') & (m.finanse == 'Tak') & (m.przyszlosc_zawodowa == 'Jako lider, menedzer'))
    def Zarzadzanie(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Zarzadzanie', 'opis': 'Studia z zakresu planowania, organizowania i kierowania działalnością przedsiębiorstw.', 'zdjecie': zdjecie['Zarzadzanie'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Nie') & (m.finanse == 'Nie') & (m.matematyka_czy_fizyka == 'Matematyka'))
    def Matematyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Matematyka', 'opis': 'Studia zajmujące się teoriami i metodami matematycznymi oraz ich zastosowaniem w różnych dziedzinach.', 'zdjecie': zdjecie['Matematyka'] })

    ##
    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Matematyka, Informatyka, Fizyka') & (m.nowe_technologie == 'Nie') & (m.budynki == 'Nie') & (m.finanse == 'Nie') & (m.matematyka_czy_fizyka == 'Fizyka'))
    def Fizyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Fizyka', 'opis': 'Studia z zakresu badania praw rządzących przyrodą, od najmniejszych cząsteczek po kosmos.', 'zdjecie': zdjecie['Fizyka'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Historia, WOS') & (m.prawo == 'Tak'))
    def Prawo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Prawo', 'opis': 'Studia zajmujące się systemem prawnym, jego zasadami i praktykami oraz przygotowujące do zawodów prawniczych.', 'zdjecie': zdjecie['Prawo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Historia, WOS') & (m.prawo == 'Nie') & (m.administracja == 'Miedzynarodowa'))
    def Stosunki_miedzynarodowe(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Stosunki miedzynarodowe', 'opis': 'Studia zajmujące się analizą relacji między państwami, organizacjami międzynarodowymi i problemami globalnymi.', 'zdjecie': zdjecie['Stosunki miedzynarodowe'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Historia, WOS') & (m.prawo == 'Nie') & (m.administracja == 'Krajowa'))
    def Administracja(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Administracja', 'opis': 'Studia z zakresu zarządzania organizacjami publicznymi i administracji państwowej.', 'zdjecie': zdjecie['Administracja'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Krajow nordyckich'))
    def Skandynawistyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Skandynawistyka', 'opis': 'Studia zajmujące się kulturą, językiem i historią krajów skandynawskich.', 'zdjecie': zdjecie['Skandynawistyka'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Japonii'))
    def Japonistyka(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Japonistyka', 'opis': 'Studia zajmujące się językiem, kulturą i historią Japonii.', 'zdjecie': zdjecie['Japonistyka'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Chin'))
    def Sinologia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Sinologia', 'opis': 'Studia zajmujące się językiem, kulturą i historią Chin.', 'zdjecie': zdjecie['Sinologia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Krajow niemiecko-jezykowych'))
    def FilologiaGermanska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Filologia germanska', 'opis': 'Studia zajmujące się językiem, kulturą i literaturą krajów niemieckojęzycznych.', 'zdjecie': zdjecie['Filologia germanska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Krajow romańsko-jezykowych'))
    def FilologiaRomanska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Filologia romanska', 'opis': 'Studia zajmujące się językami, kulturą i literaturą krajów romańskich.', 'zdjecie': zdjecie['Filologia romanska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Tak') & (m.kultura == 'Krajow slowiańskich'))
    def FilologiaSlowianska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Filologia slowianska', 'opis': 'Studia zajmujące się językami, kulturą i literaturą krajów słowiańskich.', 'zdjecie': zdjecie['Filologia slowianska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.angielski == 'Nie'))
    def FilologiaAngielska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Filologia angielska', 'opis': 'Studia zajmujące się językiem, kulturą i literaturą krajów anglojęzycznych.', 'zdjecie': zdjecie['Filologia angielska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Pisac wlasne teksty'))
    def Edytorstwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Edytorstwo', 'opis': 'Studia zajmujące się przygotowywaniem tekstów do publikacji.', 'zdjecie': zdjecie['Edytorstwo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Pomagac innym'))
    def Logopedia(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Logopedia', 'opis': 'Studia zajmujące się terapią i diagnozą zaburzeń mowy.', 'zdjecie': zdjecie['Logopedia'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Zajmowac sie kultura i sztuka') & (m.instytucje_kulturalne == 'Tak'))
    def Kulturoznawstwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Kulturoznawstwo', 'opis': 'Studia zajmujące się badaniem kultur różnych społeczeństw i ich wpływu na współczesny świat.', 'zdjecie': zdjecie['Kulturoznawstwo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Zajmowac sie kultura i sztuka') & (m.instytucje_kulturalne == 'Tak'))
    def Kulturoznawstwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Kulturoznawstwo', 'opis': 'Studia zajmujące się badaniem kultur różnych społeczeństw i ich wpływu na współczesny świat.', 'zdjecie': zdjecie['Kulturoznawstwo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Zajmowac sie kultura i sztuka') & (m.instytucje_kulturalne == 'Nie'))
    def FilologiaPolska(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Filologia polska', 'opis': 'Studia zajmujące się językiem, kulturą i literaturą polską.', 'zdjecie': zdjecie['Filologia polska'] })

    @when_all((m.scisle_czy_humanistyczne == 'Humanistyczne') & (m.co_wolisz2 == 'Zajecia jezykowe') & (m.lubisz_robic == 'Pracowac w mediach i reklamie'))
    def Dziennikarstwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Dziennikarstwo', 'opis': 'Studia zajmujące się pozyskiwaniem, opracowywaniem i publikacją informacji.', 'zdjecie': zdjecie['Dziennikarstwo'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Nie') & (m.gdzie_pracowac == 'Karetka'))
    def RatownictwoMedyczne(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Ratownictwo medyczne', 'opis': 'Studia przygotowujące do udzielania pierwszej pomocy i działania w sytuacjach kryzysowych.', 'zdjecie': zdjecie['Ratownictwo medyczne'] })

    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Nie') & (m.gdzie_pracowac == 'Szpital') & (m.noworodki == 'Tak'))
    def Poloznictwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Poloznictwo', 'opis': 'Studia przygotowujące do opieki nad kobietami w ciąży, podczas porodu i po porodzie.', 'zdjecie': zdjecie['Poloznictwo'] })
    
    @when_all((m.scisle_czy_humanistyczne == 'Scisle') & (m.co_wolisz1 == 'Biologia, Chemia, Geografia') & (m.sektor == 'Tak') & (m.ludzie == 'Tak') & (m.lekarz == 'Nie') & (m.chemia == 'Nie') & (m.sport_i_sylwetka == 'Nie') & (m.gdzie_pracowac == 'Szpital') & (m.noworodki == 'Nie'))
    def Pielegniarstwo(c):
        c.assert_fact({ 'ktora': c.m.ktora, 'wynik': 'Pielegniarstwo', 'opis': 'Studia przygotowujące do zawodu pielęgniarki, obejmujące opiekę nad chorymi i dbanie o ich zdrowie.', 'zdjecie': zdjecie['Pielegniarstwo'] })

    @when_all(+m.ktora)
    def output(c):
        print('Propozycja: {0}.{1} Opis filmu: {2} {3}'.format(c.m.ktora, c.m.wynik, c.m.opis, c.m.zdjecie))
        global Dane
        #Dane=''+('Propozycja: {0}.{1} Opis filmu: {2}'.format(c.m.rekomendacja, c.m.wynik, c.m.opis))
        Dane = [
        'Propozycja: ' + c.m.ktora,
        c.m.wynik,
        c.m.opis,
        c.m.zdjecie,
        ]
    

zdjecie = {
        'Stomatologia': 'stomotologia.webp',
        'Lekarski': 'lekarski.jpg',
        'Farmacja': 'farmacja.webp',
        'Poloznictwo': 'poloznictwo.jpg',
        'Pielegniarstwo': 'pielegniarka.webp',
        'Ratownictwo medyczne': 'ratownictwo.jpg',
        'Dietetyka': 'dietetyka.webp',
        'Fizjoterapia': 'fizjoterapia.webp',
        'Biotechnologia':'biotechnologia.webp',
        'Analityka chemiczna': 'analityka.jpg',
        'Weterynaria': 'weterynaria.jpg',
        'Ochrona srodowiska': 'ochrona.jpg',
        'Zoologia': 'zoologia.jpg',
        'Turystyka i rekreacja': 'turystyka.jpg',
        'Geodezja': 'geodezja.jpg',
        'Telekomunikacja': 'telekomunikacja.jpg',
        'Informatyka': 'informatyka.jpg',
        'Mechatronika': 'mechatronika.jpg',
        'Budownictwo': 'budownictwo.jpg',
        'Architektura': 'architektura.jpg',
        'Ekonomia': 'ekonomia.jpg',
        'Finanse i rachunkowosc': 'finanse.webp',
        'Zarzadzanie': 'zarzadzanie.jpg',
        'Matematyka': 'matematyka.jpg',
        'Fizyka': 'fizyka.jpg',
        'Prawo': 'prawo.jpg',
        'Stosunki miedzynarodowe': 'stosunki.jpg',
        'Administracja': 'administracja.jpeg',
        'Skandynawistyka': 'skandynawistyka.jpg',
        'Japonistyka': 'japonistyka.jpg',
        'Sinologia': 'sinologia.jpg',
        'Filologia germanska': 'germanska.jpg',
        'Filologia romanska': 'romanska.jpg',
        'Filologia slowianska': 'slowianska.jpg',
        'Filologia angielska': 'angielska.jpg',
        'Edytorstwo': 'edytorstwo.jpg',
        'Logopedia' : 'logopedia.jpg',
        'Dziennikarstwo' : 'dziennikarstwo.jpg',
        'Kulturoznawstwo' : 'kulturoznactwo.jpg',
        'Filologia polska': 'polska.jpg',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        scisle_czy_humanistyczne = request.form.get('scisle_czy_humanistyczne')
        co_wolisz1 = request.form.get('co_wolisz1')
        co_wolisz2 = request.form.get('co_wolisz2')
        sektor = request.form.get('sektor')
        ludzie = request.form.get('ludzie')
        lekarz = request.form.get('lekarz')
        jama_ustna = request.form.get('jama_ustna')
        chemia = request.form.get('chemia')
        sport_i_sylwetka = request.form.get('sport_i_sylwetka')
        gdzie_pracowac = request.form.get('gdzie_pracowac')
        zywnienie = request.form.get('zywienie')
        chemia_czy_biologia = request.form.get('chemia_czy_biologia')
        zwierzeta = request.form.get('zwierzeta')
        leczenie_zwierzat = request.form.get('leczenie_zwierzat')
        ekologia = request.form.get('ekologia')
        nowe_technologie = request.form.get('nowe_technologie')
        zainteresowania = request.form.get('zainteresowania')
        budynki = request.form.get('budynki')
        technika_czy_kreatywnosc = request.form.get('technika_czy_kreatywnosc')
        finanse = request.form.get('finanse')
        przyszlosc_zawodowa = request.form.get('przyszlosc_zawodowa')
        matematyka_czy_fizyka = request.form.get('matematyka_czy_fizyka')
        administracja = request.form.get('administracja')
        angielski = request.form.get('angielski')
        kultura = request.form.get('kultura')
        jezyk_obce = request.form.get('jezyk_obce')
        prawo = request.form.get('prawo')
        podroze = request.form.get('podroze')
        lubisz_robic = request.form.get('lubisz_robic')
        instytucje_kulturalne = request.form.get('instytucje_kulturalne')
        noworodki = request.form.get('noworodki')

        post('jaka_ktora_kierunek',{
        'ktora':'1',
        'scisle_czy_humanistyczne': scisle_czy_humanistyczne,
        'co_wolisz1': co_wolisz1,
        'co_wolisz2': co_wolisz2,
        'sektor': sektor,
        'ludzie': ludzie,
        'lekarz': lekarz,
        'jama_ustna': jama_ustna,
        'chemia': chemia,
        'sport_i_sylwetka': sport_i_sylwetka,
        'gdzie_pracowac': gdzie_pracowac,
        'zywienie': zywnienie,
        'chemia_czy_biologia': chemia_czy_biologia,
        'zwierzeta': zwierzeta,
        'leczenie_zwierzat': leczenie_zwierzat,
        'ekologia': ekologia,
        'nowe_technologie': nowe_technologie,
        'zainteresowania': zainteresowania,
        'budynki': budynki,
        'technika_czy_kreatywnosc': technika_czy_kreatywnosc,
        'finanse': finanse,
        'przyszlosc_zawodowa': przyszlosc_zawodowa,
        'matematyka_czy_fizyka': matematyka_czy_fizyka,
        'administracja': administracja,
        'angielski': angielski,
        'kultura': kultura,
        'prawo' : prawo,
        'podroze' : podroze,
        'jezyk_obce': jezyk_obce,
        'lubisz_robic': lubisz_robic,
        'instytucje_kulturalne': instytucje_kulturalne,
        'noworodki': noworodki,
        });
        return render_template('results.html', wynik=Dane)
    return render_template('index.html')

@app.route('/clear', methods=['GET'])
def clear():
    global Dane
    Dane = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

