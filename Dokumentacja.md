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
Lorem ipsum

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
Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum 

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
*1. Co zrobić jeżeli na moim ekranie 1920x1080 okno gry jest zbyt duże?*
Jeżeli na ekranie 1920x1080 okno gry nie mieści się na wysokość to prawdopodobnie skala jest ustawiona na wartość większą niż 100%.
Aby to zmienić wystarczy wejść do
System -> Wyświetlacz -> Skala i Układ i zmienić skalę na 100%
*2. Po wygranej nie czyszczone są wszystkie zmienne.*
Nie rozwiązany, trzeba dopisać funkcję czyszczącą wszystkie zmienne
*3. Będąc w pętli przygotowań nie da się wielokrotnie wyczyścić tablicy*
Rozwiązane tymczasowo dając graczowi możliwość tylko ręcznego rozmieszczania statków (bez ograniczenia ich długości do takich jakie ma komputer ale z ograniczoną ilością do 20) lub jednorazowego kliknięcia przycisku do generowania

## Napisane przy użyciu
- Python 3.11.0
- Pygame 2.1.3.dev8

> Zaktualizowano 10.12.2022