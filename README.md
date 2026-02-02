# Wstęp

Na podstawie surowych danych ze STEŚ dla odcinka S7 Kraków-Myślenice przeanalizowanych zostało 3288 matematycznie możliwych wariantów przebiegu drogi S7.
Dla każdego wariantu policzone zostały sumaryczne wyniki dla każdego z 79 podkryteriów jako suma wyników ze wszystkich trzech odcinków decyzyjnych dla danego wariantu/kombinacji.
Następnie wartości każdego z podkryteriów znormalizowano do przedziału 0-5 w przestrzeni 3288 wariantów przy użyciu normalizacji min-max.
Większość podkryteriów stanowią destymulanty, czyli kryteria dla których najmniejsza wartość jest najkorzystniejsza. Przykładem takich kryteriów są np. kryteria dotyczące liczby wyburzeń.
Niewielką część kryteriów stanowią stymulanty, czyli takie kryteria dla których największa wartość jest najkorzystniejsza. Przykładem może być prognozowane natężenie ruchu na projektowanej drodze, im większy ruch projektowana droga przejmie tym lepiej.
Przy normalizacji uwzględniono różne rodzaje kryteriów.
Po normalizacji obliczono średnie ważone zgodnie ze standardowymi wzorami uwzględniając też kryteria w których większość lub wszystkie wartości były zerowe.
W wyniku tego oceny większości kryteriów zostały "rozwodnione" obecnością dużej liczby zer, ale nie powinno to stanowić problemu.

# Wyniki

Poniżej omówione zostaną wyniki własnych analiz WAP (wielokryterialna analiza porównawcza).
Wyniki przedstawiane są w postaci wykresów z komentarzem.

Omawianie wyników rozpoczniemy od liczby wyburzeń budynków mieszkalnych dla każdego z 3288 matematycznie możliwych wariantów. Liczba wyburzeń została policzona jako suma liczby wyburzeń na każdym z trzech odcinków decyzyjnych.
Wykres poniżej przedstawia liczbę wyburzeń (oś X) w zależności od węzła początkowego wariantu (oś Y). Numeracja węzłów początkowych jest zgodna ze STEŚ.
Punkty reprezentujące warianty z tego samego węzła zostały oznaczone również tym samym kolorem, nazwa węzła początkowego pojawia się również w legendzie wykresu.
Na poniższym wykresie widzimy że zdecydowanie najwięcej wyburzeń generowały warianty wyprowadzone z węzła Bieżanów, bo od niecałych 300 do blisko 450 w zależności od wariantu.
Warianty z węzłów Południe i Skawina generowały najmniej wyburzeń. Warianty z węzłów Łagiewniki, Tuchowska, Blacharska generowały średnią liczbę wyburzeń budynków mieszkalnych.
![Alt text](graphs/liczba_wyburzen_wezly.png?raw=true "Title")

Poniższy wykres przedstawia również liczbę wyburzeń budynków mieszkalnych, ale tym razem na osi Y znalazł się numer oznaczający numer wariantu na pierwszym odcinku decyzyjnym (od A4 do BDI).
Dzięki temu możemy zobaczyć jak liczba wyburzeń przedstawia się w zależności od tego który z 50-ciu różnych wariantów na pierwszym odcinku decyzyjnym został wybrany (od W1 do W50).
![Alt text](graphs/liczba_wyburzen_odcinki.png?raw=true "Title")

Następny wykres przedstawia już pozycję na liście wariantu według WAP po uwzględnieniu wszystkich kryteriów.
Na osi X mamy pozycję wariantu w rankingu według WAP, na osi Y mamy numer węzła początkowego.
Według analizy najlepiej wypadają warianty z węzłów Południe i Łagiewniki, następnie z węzłów Skawina, Tuchowska i Blacharska, a najgorzej wypadają warianty z węzłów Bieżanów i Niepołomice.
![Alt text](graphs/sumarycznie_wezly.png?raw=true "Title")

Poniżej analogiczny wykres jak wyżej, ale tym razem na osi Y mamy numer wariantu na pierwszym odcinku decyzyjnym (od W1 do W50).
![Alt text](graphs/sumarycznie_odcinki.png?raw=true "Title")

Istotne jest pytanie jak ta klasyfikacja/ranking wariantów ma się do klasyfikacji przedstawionej w STEŚ przez firmię IVIA.
Następny wykres to obrazuje. Na osi X mamy pozycję wariantu w naszej klasyfikacji, na osi Y odpowiadającą pozycję obliczoną w opracowaniu STEŚ.
Widzimy że istnieje wyraźna korelacja między klasyfikacjami, ale nie są one tożsame ze względu na różnice w modelach matematycznych użytych do obliczania WAP.
![Alt text](graphs/pozycja_wariantow_opracowanie_wlasne_vs_stes.png?raw=true "Title")

Kolejny wykres przedstawia ranking wariantów wariantów według kryterium przestrzenno-społecznego. Na osi X mamy pozycję wariantu w tym kryterium, na osi Y mamy numer węzła początkowego.
Widzimy, że według tego kryterium dość dobrze wypadają niektóre warianty z węzłów Tuchowska, Blacharska i Niepołomice.
![Alt text](graphs/spoleczne_wezly.png?raw=true "Title")

Analogiczny wykres jak powyżej tylko na osi Y mamy numer wariantu na pierwszym odcinku decyzyjnym (od W1 do W50).
![Alt text](graphs/spoleczne_odcinki.png?raw=true "Title")

Na wykresie poniżej mamy warianty w ujęciu kryterium transportowo-ruchowego. Wyraźnie widać że im dalsze węzły początkowe od przebiegu obecnej Zakopianki (węzeł Południe) tym gorsze wyniki dla tego kryterium.
![Alt text](graphs/transportowe_wezly.png?raw=true "Title")

Analogiczny wykres jak powyżej tylko na osi Y mamy numer wariantu na pierwszym odcinku decyzjnym (od W1 do W50).
![Alt text](graphs/transportowe_odcinki.png?raw=true "Title")

Więcej wykresów w podkatalogu [graphs](graphs/)

# Uwagi

MODYFIKACJE ARKUSZY:
W arkuszu z danymi dla pierwszego odcinka decyzyjnego w podkryterium "Składowiska odpadów" dla wariantu W11 była literka "h". Zamienione na 0.

