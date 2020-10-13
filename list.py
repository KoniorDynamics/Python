# Lista to kolekcja uporządkowana mutable heterogeniczna
# Numerowanie indeksów od 0

a = [1, 2, (3, 4), 'ala']

# Ustalenie liczby elementów listy z pomocą metody len
d = len(a)
print(f" liczba elementów {d}")

# Do dodania elementu do listy można użyć metody append lub insert.
# Przy pomocy append dodajemy element na koniec listy.
a.append(99)
print(f"dodanie elementu na koniec listy {a}")
# Uzywając metody insert możemy dodać element (drugi parametr) w określone miejsce (pierwszy parametr- podajemy indeks).
a.insert(1, 'element')
print(f"dodanie elementu  w określone miejsce listy {a}")

# Usuwanie elementów z listy można wykonać przy pomocy metod pop i remove.
# Gdy chcemy usunąć ostatni element z listy używamy pop bez przekazania parametru.
a.pop()
print(f'usunięcie elementu- domyślnie ostatniego {a}')
# Gdy chcemy usunąć z listy element o zdanaym indeksie  używamy pop i jako parametr przekazujemy indeks tego elementu.
print(f'wyciągnięcie usuwanego elementu {a.pop(3)}')
print(f'usuwanie elementu o zadanym indeksie {a}')
# Gdy checemy usunąć znany element używamy metody remove i jako parametr przekazujemy ten elementu
a.remove('element')
print(f'usuwanie elementu o zdanej nazwie {a}')
# Do usuwania wszystkich elementów z listy służy metoda clear.
a.clear()
print(f'usuwanie wszystkich elementów listy {a}')

a = [1, 2, (3, 4), 'ala']
# Ustalamy indeks danego elementu przy omocy metody indeks, jako parametr przekazujemy dany element.
c = a.index('ala')
print(f'ustalanie indeksu danego elementu {c}')

# Zmianę kolejności elemetów w liście można uzyskać za pomocą reversed lub slicingu.
reversed(a)
print(f'zmiana kolejności reversed {list(reversed(a))}')
b = a[::-1]
print(f'zmiana kolejności slicing {b}')

# Zastosowanie slicingu:
# zmiana kolejności -jw
# wyciągnięcie elementu o zadanym indeksie
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = z[2]
print(f'slicing - wyciąganie elementu {x}')
# wyciągnięcie kolejnych elementu o indeksie ooczątkowym - przedział zamknięty i końcowym - przedział otwarty.
w = z[1:5]
print(f'slicing - wyciąganie elementów o określonych indeksach {w}')
# wyciągnięcie co 2 elementu
q = z[::2]
print(f'slicing - wyciąganie co 2 elementu od początku {q}')
# wyciągnięcie co 3 elementu od końca
y = z[::-3]
print(f'slicing - wyciąganie co 3 elementu od końca {y}')
# wyciągnięcie elementów od określonego indexu do końca
n = z[3::]
print(f'wyciągnięcie elementów od tego z indexem 3 do końca {n}')
# przypisanie wartości elementowi listy o danym idx
z[3] = 4444
print(f'przypisanie wartości elementowi listy o danym idx {z}')

# Do posortowania listy int lub float w kolejności malejącej lub rosnącej mozna użyć metody sorted
z = [1, 2.5, 1.1, 15, -5, 13, 0, -155.89, -5]
z.sort(reverse=True)
print(f'sortowanie - kolejność malejąca {z}')
z.sort(reverse=False)
print(f'sortowanie - kolejność wzrastająca {z}')

# Modyfikowanie elementów listy używając iterowania.
u = [x + 1 for x in z]
print(f'iterowanie po liście {u}')

# Z elementów listy można stworzyć string używając metodu join
# gdy elementy są stringami
o = ['ala', 'ela']
p = ', '.join(o)
print(f'łączenie stringów z listy w jeden string {p}', type(p))
# gdy elementy listy nie są stringami najpierw trzeba je zamienić na strigi przy pomocy np comprehension
s = ','.join([str(x) for x in z])
print(f'tworzenie stringa z elementów listy {s}', type(s))

# Listę stringów zawierających wewnątrz liczby cąłkowite można zminic na listę int za pomocą comprehension
k = ['1', '2', '3', '4']
i = [int(x) for x in k]
print(f'tworzenie listy int z listy  strigów {i} ')


# Zsumować elementy listy będących int lub float można przy pomocy metody sum lub
sum_z= sum(z)
print(f'sumowanie elementów listy {sum_z}')
# Wyciąganie najmniejszej wartości
min_z = min(z)
print(f'najmniejsza wartość {min_z}')
# Wyciąganie największej wartości
max_z=max(z)
print(f'największa wartość {max_z}')

# Kopiowanie listy
u = a.copy()
print(f'kopiowanie listy {u}')

# Łączenie list można wykonać dodając je do siebie, metodą append połączoną z comprehension oraz metodą extend
ku = k + u
print(f'łączenie list {ku}')
[k.append(x) for x in u]
print(f'łączenie list {k}')
k.extend(z)
print(f'łączenie list {k}')

# Do stworzenia listy o danej strukturze używamy list comprehension.
g = [x for x in range(1, 11)]
print(f'generowanie listy {g}')
h = [[y for y in range(1, 3)] for x in range(1, 4)]
print(f'generowanie listy w liście {h}')
h = [[{} for y in range(1, 3)] for x in range(1, 4)]
print(f'generowanie listy słowników w liście {h}')

# Do utworzenia listy tupli indeksu i przypisanego do niego elementu używamy metody enumerate.
r = ['ala', 'ula', 'ela', 'ula']
j = [(x, y) for x, y in enumerate(r)]
print(f'tworzenie listy tupli z przypisanym indeksem do elementu {j}')

# Do policzenia ile razy występuje dany element w liście można użyc metody count.
e = r.count('ula')
print(f'ile razy występuje dany element w liście {e}')
