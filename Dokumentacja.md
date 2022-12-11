# Battleships - Projekt gry w Statki za pomocą biblioteki Pygame
> Autor: Tymiec

## *Celem minimum projektu jest stworzenie grywalnej gry w statki przy użyciu biblioteki pygame.*

**Cele minimum:**

- [X] gracz może zaznaczać pola jako statki

- [X] dynamicznie rysowana plansza

- [X] algorytm rozmieszczania statków

- [X] spójny styl graficzny (pixel art)

- [X] muzyka pasująca klimatycznie (szanty ale brzmiące tak jak na konsoli NES)

- [X] jakkolwiek lepszy niż losowy algorytm strzelania przez komputer ale bez dawania mu wiedzy gdzie są statki

- [X] prosty ekran podsumowania

- [X] generowanie grafik animacji, trafień i liczb za pomocą spriteów

- [X] klikalne przyciski i pętla gry w której nie zagnieżdżamy się w nieskończoność przeskakując po menu

- [X] brak często pojawiających się błędów uniemożliwiających rozgrywkę



**Cele na moment w którym będę miał chwilę czasu:**
- [ ] dodać animacje 
    - [ ] wybuchu przy trafeniu statku/wody

    - [ ] inne sprite'y dla każdego statku 

    - [ ] informację o zatopieniu całego statku  

    - [ ] animację wygranej gracza i przegranej gracza

- [ ] zmianę muzyki na przyspieszoną o 35% jeżeli gracz/komputer mają mniej niż 5 statków do trafienia

- [ ] ulepszony algorytm strzelania przez komputer (jeżeli trafi, to szuka w okolicy statku)

- [ ] dynamiczne skalowanie pozycji myszki i okna gry

- [ ] ograniczenie długości statków stawianych przez gracza do tych ustalonych (częściowo zrobione ale nie ukończone)

- [ ] menu opcji


## Jak grać?
Aby zagrać wystarczy uruchomić plik battleships.py będąc w głównym folderze z plikami. 

Po uruchomienie kliknąć przycisk PLAY.

Jeżeli chcemy samemu ustawić statki to klikamy myszką na planszy po lewej w miejscach w których chcemy postawić część statku. Możemy ustawić maksymalnie 20 części statku. Jeżeli ustawimy mniej to utrudniamy sobie grę.

Możemy także wygenerować statki, z powodu błędu generowanie jest aktualnie tylko możliwe przed postawienieniem jakiejkolwiek części statku na planszy.
Gdy ustawimy statki klikamy przycisk START i zaczynamy grę.

Na planszy po prawej stronie wybieramy pole w które chcemy strzelić, czerwony X symbolizuje trafienie a niebieskie pole symbolizuje pudło. Jeżeli trafimy to dostajemy kolejne strzał, jeżeli nie trafimy następny strzał odda komputer w naszą planszę.

Gra kończy się w momencie zatopienia wszystkich statków gracza lub komputera

Po zakończeniu widzimy planszę podsumowującą.
Moves - liczba oddanych strzałów 
Hits - liczba trafień

## Omówienie wybranych fragmentów kodu
Przyjęte wartości:
- 0 - puste pole

- 1 - trafione pole na którym był statek

- 2 - pudło

- 3 - statek

- 4 - trafiony statek (jeszcze nie zaimplementowane)

- 5 do 7 - tekstury dla mgły wojny (jeszcze nie zaimplementowane)

- 10 - pole na którym wiemy że nie może być statku/nie możemy postawić statku

---

### **Algorytm rozmieszczania statków** - ```Generate_whole_board()``` i ```Generate_ship()```
```Generate_ship(length)```

W pętli while losujemy dwie zmienne od 0 do 9 których używamy jako koordynatów do rozpoczęcia kładzenia statku tak długo aż nie znajdziemy miejsca na planszy ship_board(plansza statków gracza lub komputer). Sprawdzamy czy statek o podanej długości zmieści się w wylosowanych koordynatach. Jeżeli tak to go kładziemy, jeśli nie to powtarzamy losowanie punktu i zwracamy ```False```.

```Generate_whole_board()```

W pętli while pobieramy z tablicy ships_1 długości statków. Potem wywołujemy funkcję generowania statków o określonej długości tak długo aż komputerowi nie uda się zmieścić wszystkich statków ponieważ przy pewnych ustawieniach jeden ze statków nie miał się gdzie zmieścić. Zapobiegam temu sprawdzając za każdym razem czy liczba pól zawierających statek jest równa 20

---

### **Rysowanie sprite'ów**

Wszystkie spritey rysujemy względem lewego górnego rogu okna 0,0

Jako iż łatwiej jest nam zmieniać wartość liczbową niż co chwilę przeładowywać plik to używamy sprite'ów do animacji, zaznaczania pól oraz wyświetlania liczb na ekranie podsumowania.

Najłatwiej działanie spritów zrozumieć patrząc na przykładowy sprite. 
(hit_sprite)
Jeżeli popatrzymy na hit_sprite to zobaczymy że jego wysokość to 38 a długość jest wielokrotnością 38.
Wybieramy więc kwadrat 38x38 ze sprite'a za pomocą mnożenia liczby 38. Przykładowo jeżeli zaczniemy na 0 to będziemy mieli kwadrat 38x38 odpowiadający pustemu polu.
Rysowanie planszy odbywa się w dość podobny sposób. Jako iż koordynaty [x, y] ustalamy względem lewego górnego roku okna to wystarczyło wyliczyć dystans z lewego górnego rogu do lewego górnego rogu planszy. Wtedy naszym 0,0 jest początek planszy. Mnożąc wtedy 
x = wybrane_pole * 38
y = wybrane_pole * 38
jesteśmy w stanie schludnie generować planszę. Do tego czym wypełnimy pole sluży nam właśnie hit_sprite. 
Pobieramy wartość danego pola i mnożymy wartość_pola * 38.
---

### **Prosty algorytm strzałów komputera** - ```Computer_targeting()```
W pętli while losujemy dwie zmienne od 0 do 9 których używamy jako koordynatów strzału tak długo aż nie znajdziemy miejsca na planszy hit_board_1(plansza statków gracza) w które nie został oddany już strzał 
```python
hit_board_1[x][y] != 1
```
albo nie zostało ono oznaczone jako takie na którym nie może być statku 
```python
hit_board_1[x][y] != 10
``` 
Pola oznaczamy jako takie na których nie może być statku przy trafieniu pola ze statkiem.Ponieważ jeżeli wiemy że statki nie mogą być obok siebie to po przekątnych od danego kwadratunie może być żadnego statku.

---

## Znane problemy i rozwiązania:
**1. Co zrobić jeżeli na moim ekranie 1920x1080 okno gry jest zbyt duże?**

Jeżeli na ekranie 1920x1080 okno gry nie mieści się na wysokość to prawdopodobnie skala jest ustawiona na wartość większą niż 100%.
Aby to zmienić wystarczy wejść do
System -> Wyświetlacz -> Skala i Układ i zmienić skalę na 100%

**2. Po wygranej nie czyszczone są wszystkie zmienne.**

Nie rozwiązany, trzeba dopisać funkcję czyszczącą wszystkie zmienne

**3. Będąc w pętli przygotowań nie da się wielokrotnie wyczyścić tablicy**

Rozwiązane tymczasowo dając graczowi możliwość tylko ręcznego rozmieszczania statków (bez ograniczenia ich długości do takich jakie ma komputer ale z ograniczoną ilością do 20) lub jednorazowego kliknięcia przycisku do generowania

## Napisane przy użyciu
- Python 3.11.0
- Pygame 2.1.3.dev8

> Zaktualizowano 10.12.2022