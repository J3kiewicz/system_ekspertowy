from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Wczytanie danych
df = pd.read_csv("Kierunki_excel.csv")


d = {'Scisle': 0, 'Humanistyczne': 1}
df['scisle_czy_humanistyczne'] = df['scisle_czy_humanistyczne'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['sektor'] = df['sektor'].map(d)

d = {'Biologia_Chemia_Geografia': 0, 'Matematyka_Informatyka_Fizyka': 1, '?': -1}
df['co_wolisz1'] = df['co_wolisz1'].map(d)


d = {'Tak': 0, 'Nie': 1, '?': -1}
df['nowe_technologie'] = df['nowe_technologie'].map(d)

d={'Systemy_komunikacji':0,'Programy_i_aplikacje':1, 'Mechanika_i_robotyka':2, '?':-1}
df['zainteresowania']=df['zainteresowania'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['budynki'] = df['budynki'].map(d)

d = {'Techniczny': 0, 'Kreatywnym': 1, '?': -1}
df['technika_czy_kreatywnosc'] = df['technika_czy_kreatywnosc'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['finanse'] = df['finanse'].map(d)

d = {'Jako_analityk_doradca': 0, 'Jako_ksiegowy': 1, 'Jako_lider_menedzer':2, '?': -1}
df['przyszlosc_zawodowa'] = df['przyszlosc_zawodowa'].map(d)

d = {'Matematyka': 0, 'Fizyka': 1, '?': -1}
df['matematyka_czy_fizyka'] = df['matematyka_czy_fizyka'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['ludzie'] = df['ludzie'].map(d)

d = {'Chemia': 0, 'Biologia': 1, '?': -1}
df['chemia_czy_biologia'] = df['chemia_czy_biologia'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['lekarz'] = df['lekarz'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['jama_ustna'] = df['jama_ustna'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['chemia'] = df['chemia'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['sport_i_sylwetka'] = df['sport_i_sylwetka'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['zywienie'] = df['zywienie'].map(d)

d = {'Szpital': 0, 'Karetka': 1, '?': -1}
df['gdzie_pracowac'] = df['gdzie_pracowac'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['noworodki'] = df['noworodki'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['zwierzeta'] = df['zwierzeta'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['leczenie_zwierzat'] = df['leczenie_zwierzat'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['ekologia'] = df['ekologia'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['podroze'] = df['podroze'].map(d)

d = {'Historia_WOS': 0, 'Zajecia_jezykowe': 1, '?': -1}
df['co_wolisz2'] = df['co_wolisz2'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['angielski'] = df['angielski'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['prawo'] = df['prawo'].map(d)

d = {'Miedzynarodowa': 0, 'Krajowa': 1, '?': -1}
df['administracja'] = df['administracja'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['jezyk_obce'] = df['jezyk_obce'].map(d)

d = {'Krajow_nordyckich': 0, 'Japonii': 1, 'Chin': 2, 'Krajow_niemiecko-jezykowych': 3, 'Krajow_romansko-jezykowych': 4, 'Krajow_slowianskich': 5, '?': -1}
df['kultura'] = df['kultura'].map(d)

d = {'Pisac_wlasne_tekst': 0, 'Pomagac_innym': 1, 'Pracowac_w_mediach_i_reklamie': 2, 'Zajmowac_sie_kultura_i_sztuka': 3, '?': -1}
df['lubisz_robic'] = df['lubisz_robic'].map(d)


d = {'Tak': 0, 'Nie': 1, '?': -1}
df['instytucje_kulturalne'] = df['instytucje_kulturalne'].map(d)

# Powtórz dla innych kolumn jak w Twoim przykładzie...

# Przygotowanie cech
features = [
    'scisle_czy_humanistyczne', 'sektor', 'co_wolisz1', 'nowe_technologie', 'zainteresowania', 
    'budynki', 'technika_czy_kreatywnosc', 'finanse', 'przyszlosc_zawodowa', 'matematyka_czy_fizyka', 
    'ludzie', 'chemia_czy_biologia', 'lekarz', 'jama_ustna', 'chemia', 'sport_i_sylwetka', 
    'zywienie', 'gdzie_pracowac', 'noworodki', 'zwierzeta', 'leczenie_zwierzat', 'ekologia', 
    'podroze', 'co_wolisz2', 'angielski', 'prawo', 'administracja', 'jezyk_obce', 'kultura', 
    'lubisz_robic', 'instytucje_kulturalne'
]

kierunki_dane= {
    'Stomatologia': {
        "description": "Studia poświęcone zdrowiu jamy ustnej, leczeniu zębów i innych problemów stomatologicznych.",
        "zdj": "stomotologia.webp"
    },
    'Lekarski': {
        "description": "Studia przygotowujące do zawodu lekarza, obejmujące szeroką wiedzę medyczną i praktyki kliniczne.",
        "zdj": "lekarski.jpg"
    },
    'Farmacja': {
        "description": "Studia z zakresu tworzenia, produkcji i zastosowania leków oraz farmakologii.",
        "zdj": "farmacja.webp"
    },
    'Poloznictwo': {
        "description": "Studia przygotowujące do opieki nad kobietami w ciąży, podczas porodu i po porodzie.",
        "zdj": "poloznictwo.jpg"
    },
    'Pielegniarstwo': {
        "description": "Studia przygotowujące do zawodu pielęgniarki, obejmujące opiekę nad chorymi i dbanie o ich zdrowie.",
        "zdj": "pielegniarka.webp"
    },
    'Ratownictwo_medyczne': {
        "description": "Studia przygotowujące do udzielania pierwszej pomocy i działania w sytuacjach kryzysowych.",
        "zdj": "ratownictwo.jpg"
    },
    'Dietetyka': {
        "description": "Studia zajmujące się zdrowym żywieniem i dietoterapią dla różnych grup pacjentów.",
        "zdj": "dietetyka.webp"
    },
    'Fizjoterapia': {
        "description": "Studia z zakresu leczenia i rehabilitacji za pomocą ćwiczeń fizycznych i terapii manualnych.",
        "zdj": "fizjoterapia.webp"
    },
    'Biotechnologia': {
        "description": "Studia łączące biologię z technologią, skupiające się na wykorzystaniu organizmów i ich części do produkcji i badań.",
        "zdj": "biotechnologia.webp"
    },
    'Analityka_chemiczna': {
        "description": "Studia skupiające się na technikach analizy chemicznej i identyfikacji substancji.",
        "zdj": "analityka.jpg"
    },
    'Weterynaria': {
        "description": "Studia poświęcone zdrowiu i leczeniu zwierząt, zarówno domowych, jak i gospodarskich.",
        "zdj": "weterynaria.jpg"
    },
    'Ochrona_srodowiska': {
        "description": "Studia zajmujące się ochroną przyrody i zarządzaniem zasobami naturalnymi.",
        "zdj": "ochrona.jpg"
    },
    'Zoologia': {
        "description": "Studia zajmujące się badaniem zwierząt, ich anatomii, ekologii i zachowań.",
        "zdj": "zoologia.jpg"
    },
    'Turystyka_i_rekreacja': {
        "description": "Studia przygotowujące do pracy w sektorze turystycznym i organizacji czasu wolnego.",
        "zdj": "turystyka.jpg"
    },
    'Geodezja': {
        "description": "Studia zajmujące się pomiarami i mapowaniem powierzchni ziemi.",
        "zdj": "geodezja.jpg"
    },
    'Telekomunikacja': {
        "description": "Studia z zakresu technologii przesyłu informacji na odległość, w tym telefonii i internetu.",
        "zdj": "telekomunikacja.jpg"
    },
    'Informatyka': {
        "description": "Studia z zakresu programowania, tworzenia oprogramowania i zarządzania systemami komputerowymi.",
        "zdj": "informatyka.jpg"
    },
    'Mechatronika': {
        "description": "Studia łączące inżynierię mechaniczną, elektroniczną i informatyczną w celu projektowania i budowy inteligentnych systemów.",
        "zdj": "mechatronika.jpg"
    },
    'Budownictwo': {
        "description": "Studia z zakresu projektowania, wznoszenia i utrzymania budynków oraz infrastruktury.",
        "zdj": "budownictwo.jpg"
    },
    'Architektura': {
        "description": "Studia zajmujące się projektowaniem budynków i przestrzeni, łączące sztukę z technologią.",
        "zdj": "architektura.jpg"
    },
    'Ekonomia': {
        "description": "Studia z zakresu zarządzania zasobami, produkcją i dystrybucją dóbr oraz usług.",
        "zdj": "ekonomia.jpg"
    },
    'Finanse_i_rachunkowosc': {
        "description": "Studia zajmujące się zarządzaniem finansami, inwestycjami i księgowością.",
        "zdj": "finanse.webp"
    },
    'Zarzadzanie': {
        "description": "Studia z zakresu planowania, organizowania i kierowania działalnością przedsiębiorstw.",
        "zdj": "zarzadzanie.jpg"
    },
    'Matematyka': {
        "description": "Studia zajmujące się teoriami i metodami matematycznymi oraz ich zastosowaniem w różnych dziedzinach.",
        "zdj": "matematyka.jpg"
    },
    'Fizyka': {
        "description": "Studia z zakresu badania praw rządzących przyrodą, od najmniejszych cząsteczek po kosmos.",
        "zdj": "fizyka.jpg"
    },
    'Prawo': {
        "description": "Studia zajmujące się systemem prawnym, jego zasadami i praktykami oraz przygotowujące do zawodów prawniczych.",
        "zdj": "prawo.jpg"
    },
    'Stosunki_miedzynarodowe': {
        "description": "Studia zajmujące się analizą relacji między państwami, organizacjami międzynarodowymi i problemami globalnymi.",
        "zdj": "stosunki.jpg"
    },
    'Administracja': {
        "description": "Studia z zakresu zarządzania organizacjami publicznymi i administracji państwowej.",
        "zdj": "administracja.jpeg"
    },
    'Skandynawistyka': {
        "description": "Studia zajmujące się kulturą, językiem i historią krajów skandynawskich.",
        "zdj": "skandynawistyka.jpg"
    },
    'Japonistyka': {
        "description": "Studia zajmujące się językiem, kulturą i historią Japonii.",
        "zdj": "japonistyka.jpg"
    },
    'Sinologia': {
        "description": "Studia zajmujące się językiem, kulturą i historią Chin.",
        "zdj": "sinologia.jpg"
    },
    'Filologia__germanska': {
        "description": "Studia zajmujące się językiem, kulturą i literaturą krajów niemieckojęzycznych.",
        "zdj": "germanska.jpg"
    },
    'Filologia_romanska': {
        "description": "Studia zajmujące się językami, kulturą i literaturą krajów romańskich.",
        "zdj": "romanska.jpg"
    },
    'Filologia_slowianska': {
        "description": "Studia zajmujące się językami, kulturą i literaturą krajów słowiańskich.",
        "zdj": "slowianska.jpg"
    },
    'Filologia_angielska': {
        "description": "Studia zajmujące się językiem, kulturą i literaturą krajów anglojęzycznych.",
        "zdj": "angielska.jpg"
    },
    'Edytorstwo': {
        "description": "Studia zajmujące się przygotowywaniem tekstów do publikacji.",
        "zdj": "edytorstwo.jpg"
    },
    'Logopedia': {
        "description": "Studia zajmujące się terapią i diagnozą zaburzeń mowy.",
        "zdj": "logopedia.jpg"
    },
    'Dziennikarstwo': {
        "description": "Studia zajmujące się pozyskiwaniem, opracowywaniem i publikacją informacji.",
        "zdj": "dziennikarstwo.jpg"
    },
    'Kulturoznawstwo': {
        "description": "Studia zajmujące się badaniem kultur różnych społeczeństw i ich wpływu na współczesny świat.",
        "zdj": "kulturoznactwo.jpg"
    },
    'Filologia_polska': {
        "description": "Studia zajmujące się językiem, kulturą i literaturą polską.",
        "zdj": "polska.jpg"
    }
}


# Przygotowanie danych do modelu
X = df[features]
y = df['kierunek_dla_ciebie']

# Tworzenie i trenowanie modelu drzewa decyzyjnego
dtree = DecisionTreeClassifier()
dtree.fit(X, y)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        scisle_czy_humanistyczne = request.form.get("scisle_czy_humanistyczne", "-1")
        sektor = request.form.get("sektor", "-1")
        co_wolisz1 = request.form.get("co_wolisz1", "-1")
        nowe_technologie = request.form.get("nowe_technologie", "-1")
        zainteresowania = request.form.get("zainteresowania", "-1")
        budynki = request.form.get("budynki", "-1")
        technika_czy_kreatywnosc = request.form.get("technika_czy_kreatywnosc", "-1")
        finanse = request.form.get("finanse", "-1")
        przyszlosc_zawodowa = request.form.get("przyszlosc_zawodowa", "-1")
        matematyka_czy_fizyka = request.form.get("matematyka_czy_fizyka", "-1")
        ludzie = request.form.get("ludzie", "-1")
        chemia_czy_biologia = request.form.get("chemia_czy_biologia", "-1")
        lekarz = request.form.get("lekarz", "-1")
        jama_ustna = request.form.get("jama_ustna", "-1")
        chemia = request.form.get("chemia", "-1")
        sport_i_sylwetka = request.form.get("sport_i_sylwetka", "-1")
        zywienie = request.form.get("zywienie", "-1")
        gdzie_pracowac = request.form.get("gdzie_pracowac", "-1")
        noworodki = request.form.get("noworodki", "-1")
        zwierzeta = request.form.get("zwierzeta", "-1")
        leczenie_zwierzat = request.form.get("leczenie_zwierzat", "-1")
        ekologia = request.form.get("ekologia", "-1")
        podroze = request.form.get("podroze", "-1")
        co_wolisz2 = request.form.get("co_wolisz2", "-1")
        angielski = request.form.get("angielski", "-1")
        prawo = request.form.get("prawo", "-1")
        administracja = request.form.get("administracja", "-1")
        jezyk_obce = request.form.get("jezyk_obce", "-1")
        kultura = request.form.get("kultura", "-1")
        lubisz_robic = request.form.get("lubisz_robic", "-1")
        instytucje_kulturalne = request.form.get("instytucje_kulturalne", "-1")



        input_data = [
    int(scisle_czy_humanistyczne if scisle_czy_humanistyczne != '' else '-1'),
    int(sektor if sektor != '' else '-1'),
    int(co_wolisz1 if co_wolisz1 != '' else '-1'),
    int(nowe_technologie if nowe_technologie != '' else '-1'),
    int(zainteresowania if zainteresowania != '' else '-1'),
    int(budynki if budynki != '' else '-1'),
    int(technika_czy_kreatywnosc if technika_czy_kreatywnosc != '' else '-1'),
    int(finanse if finanse != '' else '-1'),
    int(przyszlosc_zawodowa if przyszlosc_zawodowa != '' else '-1'),
    int(matematyka_czy_fizyka if matematyka_czy_fizyka != '' else '-1'),
    int(ludzie if ludzie != '' else '-1'),
    int(chemia_czy_biologia if chemia_czy_biologia != '' else '-1'),
    int(lekarz if lekarz != '' else '-1'),
    int(jama_ustna if jama_ustna != '' else '-1'),
    int(chemia if chemia != '' else '-1'),
    int(sport_i_sylwetka if sport_i_sylwetka != '' else '-1'),
    int(zywienie if zywienie != '' else '-1'),
    int(gdzie_pracowac if gdzie_pracowac != '' else '-1'),
    int(noworodki if noworodki != '' else '-1'),
    int(zwierzeta if zwierzeta != '' else '-1'),
    int(leczenie_zwierzat if leczenie_zwierzat != '' else '-1'),
    int(ekologia if ekologia != '' else '-1'),
    int(podroze if podroze != '' else '-1'),
    int(co_wolisz2 if co_wolisz2 != '' else '-1'),
    int(angielski if angielski != '' else '-1'),
    int(prawo if prawo != '' else '-1'),
    int(administracja if administracja != '' else '-1'),
    int(jezyk_obce if jezyk_obce != '' else '-1'),
    int(kultura if kultura != '' else '-1'),
    int(lubisz_robic if lubisz_robic != '' else '-1'),
    int(instytucje_kulturalne if instytucje_kulturalne != '' else '-1')
]
        


        # Predykcja
        wynik = dtree.predict([input_data])[0]
        description = kierunki_dane.get(wynik, {}).get("description", "Opis niedostępny.")
        zdj = kierunki_dane.get(wynik, {}).get("zdj", "zdjęcie nie dostępne")
        formatted_wynik = wynik.replace('_', ' ')

        return render_template("results.html", wynik=formatted_wynik, description=description, zdj=zdj)

    return render_template("index.html")

@app.route('/clear')
def clear():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)