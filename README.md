# SI
# Projekt z Sztucznej inteligencji
# Temat: Saper

#Skład grupy:
- Jan Białek - lider, 
- Bartosz Fabisiak, 
- Łukasz Paszkowiak, 
- Wojtek Kamiński.

# Opis projektu:
- saper porusza się po planszy,
- jego celem jest rozbrojenie wszystkich bomb,
- bomby wybuchają po pewnym czasie i nie mogą być już rozbrojone.
- saper może poruszać się tylko po pustych polach

# Opis folderów zawartych w projekcie
- images : zawiera grafiki używane do reprezentacji planszy i obiektów
- mapy : zawiera przykładowe mapy
- sprites : zawiera pythonowe obiekty używane w projekcie

# opis algorytmów poruszania:
#- DFS:

Globalnie tworzona jest lista [Solutions], do ktorej docelowo wpisywane są wszystkie prawidłowe ścieżki znalezione przez funkcje [dfs-find].

Funkcja [dfs-find] przyjmuje argumenty:
- [Grid] - lista dwuwymiarowa zawierająca mape
- [Curr_operations] - Lista zawierająca osobną ścieżke na przejście algorytmu w inne miejsce (powinien zacząć od ["N"] sygnalizujący, że to lista)
- [a] - współrzędna x Sapera na mapie
- [b] - współrzędna y Sapera na mapie
- [destination] - lista dwuwymiarowa zawierająca współrzędne bomb na mapie
- [left] - licznik zawierający liczbę pozostałych miejsc do odwiedzenia (powinien zacząć od 0)
- [anti_loop] - licznik zapobiegający zapętleniu (zaczyna od 0).

Dokładne działanie funkcji [dfs-find]:
1. najpierw tworzy nową listę pomocniczą [dest] i przypisuje jej kopie listy [destination]
2. tworzy zmienną pomocniczą [licz] która służy do poprawy indeksów w for poniżej
3. dla każdej współrzędnej bomby z listy 'dest' sprawdza czy nie znajduje się "nad, pod, na lewo, na prawo" od obecnego miejsca współrzędnych [a], [b]:
	Jeżeli tak to za każdą taką współrzędną:
	- usuwa tą współrzędną z listy [dest]
	- do listy [Curr_operations] dodaje na koniec 'B_R lub B_L lub B_U lub B_D' oznaczający rozbrojenie bomby w danym kierunku
	- zwiększa pomocniczy licznik [licz] o 1 służący do obsługi indeksów [dest] (bo zmieniają się przy usuwaniu wspórzędnych)
	- zmniejsza licznik [left] o 1
4.sprawdza czy [left] == 0
	Jeżeli tak to dopisuje obecnie zapisaną ścieżke w [Curr_operations] do listy [Solutions] i zwraca 0
5.sprawdza czy [anti_loop] jest mniejsze od 80 
	Jeżeli tak to wykonuje następne punkty
6.zwiększa licznik [anti_loop] o 1
7. sprawdza czy wcześniej nie poszedł w 'lewo, prawo, góre, dół' sprawdzając ostatni element listy [Curr_operations](dla każdej strony sprawdza osobno)
	Jeżeli tak to
	-sprawdza czy w przeciwnym kierunku na współrzędnej obok znajduje się obiekt None sygnalizujący, że w to miejsce może się ruszyć
		Jeżeli może się ruszyć w to miejsce to
			- tworzy nową listę [operations] osobną dla każdej strony jaką sprawdza i kopuje do niej zawartość listy [Curr_operations]
			- dodaje na koniec listy [operations] 'R lub L lub U lub D' będący skrótem kierunku sprawdzanego miejsca
			- wywołuje funkcje z następującymi argumentami dfs_find(Grid, operations, współrzędną x miejsca,  współrzędną y miejsca, dest, left, anti_loop)
8. Jeżeli nie ma już gdzie pójść zwraca 0

Przed wywołaniem algorytmu trzeba znaleść współrzędne sapera i bomb i podać je jako odpowiednie argumenty .

Po zakończeniu funkcji [dfs-find] w Liście [Solutions] znajdą się wszystkie ścieżki, które [dfs-find] znalazł które odwiedzają wszystkie miejsca z początkwego 
argumentu [destination].

#- A*:
