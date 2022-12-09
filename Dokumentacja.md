# Battleships
> Autor: Tymiec
## Projekt gry w Statki za pomocą biblioteki Pygame
Lorem ipsum

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

W pętli while losujemy dwie zmienne od 0 do 9 których używamy jako koordynatów do rozpoczęcia kładzenia statku tak długo aż nie znajdziemy miejsca na planszy ship_board(plansza statków gracza lub komputer). Sprawdzamy czy statek o podanej długości zmieści się w wylosowanych koordynatach.

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


## Napisane przy użyciu
- Python 3.11.0
- Pygame 2.1.3.dev8

> Zaktualizowano 09.12.2022