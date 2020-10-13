### Słownik
***


	Wykorzystuje kolejność dodawania, bo nie ma indexów, jesy uporządkowany od pythona 3.6
    
    Słownik domyślnie jest nieiterowalny, ale można dopisać mu iterator.

    False, tupla lub “ “ mogą być kluczami w słowniku, bo są immutable i są hashowalne. 

    value - kazdy poprawny tym pytona -
    key - hashowalne wartości, które są niemutowalne

- nazwaZmiennej['klucz'] = "wartość" - dodawanie danych do słownika
   
        books = {'autor': 'książka', 'autor2': 'książka2', 'autor3': 'książka3'}
        
        books['autor4'] = 'ksiązka4'
        
- iteracja po 
       
- dict.items() - zwraca klucze i warośc    
- dict.keys() - zwraca klucze
- dict.values() - wartości
    
        books.keys()
        LUB
        dict.keys(books)

- dict.fromkeys(key, value) - zwraca słownik o podanych kluczach(iterable) i wartościach

            x = ('key1', 'key2', 'key3')
            y = 0
            thisdict = dict.fromkeys(x, y)
        OUTPUT:
            {'key1': 0, 'key2': 0, 'key3': 0}

- dict.popitem() - usuwa z podanego słownika i zwraca ostatnią parę (klucz, wartość) jako tuple 2 elementową. 
 Pary są zwracane w kolejności LIFO (ostatnie weszło, pierwsze wyszło), czyli zwraca ostatni element.
 Wyrzuca KeyError, jeśli słownik jest pusty
    
        temp = thisdict.popitem()
        OUTPUT
        ('key3', 0)


 - dict.setdefault(key, value) - zwraca value z podanego klucza, jeżeli jest w słowniku. Jeżeli go nie ma,
 dodaje do słownika wartość z podanym kluczem, jako pierwszym parametrem i value, jako drugim. Jeżeli nie ma Value podanego
 dodaje defaultowo None
 
        print(books.setdefault('autor'))
        OUTPUT --> książka
        print(books.setdefault('dupa'))
        OUTPUT --> None + dodanie do słownika
        print(books.setdefault('dupa', 666))
        OUTPUT --> 666 + dodanie do słownika (jeżeli dupa już jest ma value None!)
    
 - dict.get(key) - wypluwa wartość z podanego klucza

    Funkcja get pozwala także sprytnie ominąć sytuację, w której błąd może wywalić program.

            d= {"a": 1,"b": 2,}- # słownik wartości
            d.get("bbb", "nie ma takiego klucza") - nie ma klucza 'bbb', wyrzuca drugi parametr.
            W przypadku braku drugiego parametru zwraca None

- dict.update(nowysłownik) - będzie aktualizować listę z wynikami. Jeżeli nie będzie danego elementu wcześniej to zostanie on dopisany

        b = {'autor2':'222222'}
        print(books.update(b))
- dict.clear() - czyści zawartość podanego słownika

- del - usuwa podane parametry ze słownika

        del(books['autor'])

    