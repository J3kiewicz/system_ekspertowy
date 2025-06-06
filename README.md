Opis projektu
System Ekspercki Wspomagający Wybór Kierunku Studiów to aplikacja, której celem jest pomoc przyszłym studentom w wyborze najlepszego kierunku studiów, dopasowanego do ich zainteresowań i predyspozycji. System wykorzystuje bazę wiedzy, modele decyzyjne oraz reguły wnioskowania, symulując proces podejmowania decyzji przez eksperta edukacyjnego. Projekt powstał w ramach przedmiotu "Inżynieria Wiedzy i Systemy Ekspertowe" na kierunku Informatyka.

Założenia systemu  
Adresaci: Osoby planujące wybór kierunku studiów, chcące znaleźć ścieżkę zgodną z ich zainteresowaniami i umiejętnościami.

Cel: Wskazanie optymalnego kierunku studiów na podstawie odpowiedzi na zestaw pytań dotyczących preferencji naukowych, zawodowych i osobistych.

Metoda: System ekspertowy oparty na drzewie decyzyjnym i regułach, analizujący odpowiedzi użytkownika i wskazujący najlepiej dopasowaną opcję.

Schemat działania  
Zbieranie preferencji: Użytkownik odpowiada na serię pytań (łącznie 31), które dotyczą m.in. preferencji naukowych (ścisłe/humanistyczne), zainteresowań zawodowych, pracy z ludźmi, zwierzętami, nowymi technologiami, finansami, językami obcymi, itd.

Analiza odpowiedzi: Na podstawie odpowiedzi system przechodzi przez drzewo decyzyjne, zawężając możliwe kierunki studiów.

Wynik: System przedstawia rekomendowany kierunek studiów wraz z opisem i ilustracją.

Przykładowe pytania

-Wolisz nauki ścisłe czy humanistyczne?  
-Czy chciałbyś pracować w sektorze medycznym?  
-Czy interesujesz się nowymi technologiami?  
-Czy lubisz pracę z ludźmi?  
-Czy chcesz skupić się na żywieniu?  
-Czy lubisz języki obce?  
-Czy interesuje cię promocja kultury i praca w instytucjach kulturalnych?  
(pełna lista pytań w dokumentacji technicznej)  

Przykładowe wyniki  
System rozpoznaje 40 możliwych kierunków studiów, m.in.:  

-Stomatologia  
-Lekarski  
-Ratownictwo Medyczne  
-Pielęgniarstwo  
-Informatyka  
-Mechatronika  
-Budownictwo  
-Ekonomia  
-Prawo  
-Filologia Angielska  
-Dziennikarstwo  
(pełna lista wyników i warunków w dokumentacji)  

Implementacja  
1. PC Shell
   
Opis: System ekspertowy został zaimplementowany w środowisku PC Shell, które umożliwia definiowanie reguł, źródeł wiedzy i funkcji użytkownika.  

Pliki:  

kierunek.zw – baza wiedzy z regułami wyboru kierunku  
kierunek.bw – plik uruchomieniowy systemu  

Funkcje:

winieta – ekran powitalny  
solver – funkcja wnioskująca  
asystent – uruchamia proces wyboru kierunku  

Interfejs: Okna pytań i wyników, menu główne, ekran pomocy.

2. DeTreex
Opis: Narzędzie do graficznego tworzenia i walidacji drzew decyzyjnych.  

Funkcje:

Import danych z plików (np. Excel/CSV)  
Interaktywne projektowanie i wizualizacja drzew  
Eksport wyników do plików graficznych  

Zastosowanie: Walidacja logiki systemu ekspertowego, testowanie alternatywnych modeli decyzyjnych.

3. Python  
a) Automatyczne generowanie drzew (scikit-learn)  
Opis: Model drzewa decyzyjnego trenowany na danych wejściowych, automatycznie przewiduje kierunek studiów.  

Biblioteki: pandas, scikit-learn, pydotplus, matplotlib  

Działanie:

Wczytanie danych z CSV  
Mapowanie odpowiedzi na wartości numeryczne  
Trenowanie modelu  
Predykcja kierunku studiów na podstawie odpowiedzi użytkownika  

Wizualizacja drzewa decyzyjnego

b) Ręczne reguły decyzyjne (Durable Rules)   
Opis: Każdy kierunek studiów przypisany do zestawu reguł (warunków), które muszą być spełnione przez odpowiedzi użytkownika.  

Biblioteki: durable_rules, Flask  
  
Działanie:

Definicja reguł za pomocą dekoratorów  
Przekazywanie odpowiedzi użytkownika do silnika reguł  
Wyświetlanie rekomendowanego kierunku i opisu  

c) Interfejs webowy (Flask + HTML/JS)  
Opis: Dynamiczny formularz webowy, zbierający odpowiedzi użytkownika krok po kroku.  

Działanie:

Każde pytanie pojawia się po udzieleniu odpowiedzi na poprzednie  
Po zakończeniu - wyświetlenie rekomendacji, opisu i ilustracji kierunku  
Możliwość powrotu do formularza i ponownego wyboru  

Szczegółowa dokumetacja została dodana do repozytorium w formie pliku pdf.
