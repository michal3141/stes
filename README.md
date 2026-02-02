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

MODYFIKACJE ARKUSZY:
W pierwszym arkuszu -> Składowiska odpadów W11 była literka "h". Zamienione na 0.

@TODO:
Sprawdzić najlepsze warianty wyjściowe z w. Łagiewniki, Tuchowska, Blacharska


