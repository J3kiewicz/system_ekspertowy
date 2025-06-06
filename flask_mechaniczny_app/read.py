
#stary kod
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

# Wczytanie danych z pliku CSV
df = pandas.read_csv("Kierunki_excel.csv")

d = {'Scisle': 0, 'Humanistyczne': 1}
df['scisle_czy_humanistyczne'] = df['scisle_czy_humanistyczne'].map(d)

d = {'Tak': 0, 'Nie': 1, '?': -1}
df['sektor'] = df['sektor'].map(d)

d = {'Biologia_Chemia_Geografia': 0, 'Matematyka_Informatyka_Fizyka': 1, '?': -1}
df['co_wolisz1'] = df['co_wolisz1'].map(d)


d = {'Tak': 0, 'Nie': 1, '?': -1}
df['nowe_technologie'] = df['nowe_technologie'].map(d)

d={'Systemy_komunikacji':0,'Programy_i_aplikacje':1, 'Mechanika_i_robotyka':1, '?':-1}
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

# Wybór cech (features) do analizy
features = [
'scisle_czy_humanistyczne',
'sektor',
'co_wolisz1',
'nowe_technologie',
'zainteresowania',
'budynki',
'technika_czy_kreatywnosc',
'finanse',
'przyszlosc_zawodowa',
'matematyka_czy_fizyka',
'ludzie',
'chemia_czy_biologia',
'lekarz',
'jama_ustna',
'chemia',
'sport_i_sylwetka',
'zywienie',
'gdzie_pracowac',
'noworodki',
'zwierzeta',
'leczenie_zwierzat',
'ekologia',
'podroze',
'co_wolisz2',
'angielski',
'prawo',
'administracja',
'jezyk_obce',
'kultura',
'lubisz_robic',
'instytucje_kulturalne'
]


# Przygotowanie X (cechy) i y (target)
x = df[features]
y = df['kierunek_dla_ciebie']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)

# Dane wejściowe do przewidywania - muszą zawierać wszystkie kolumny z 'features'
input_data = pandas.DataFrame([[0, 1, 0, 1, 0, -1, 1, 0, -1, -1, 0, 0, 1, 1, 0, 0, 1, -1, 1, 0, -1, 0, 1, -1, 0, 1, -1, -1, 3, 1, -1]], columns=features)
print(dtree.predict(input_data))

data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

print(df) 