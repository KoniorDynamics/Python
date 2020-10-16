# String 

- string należy do podstawowych typów danych w python,
- string jest to ciąg znaków (łańcuch znaków) tzw. charpointów,
- właściwości stringa: kolekcja, uporządkowana, immutable, homogeniczna (jednorodna),
- string podajemy w cudzysłowach podwójnych lub pojedyńczych (zamiennie)

## Operacje na stringach:

1. Slicing -> cięcie napisów
    - wykonujemy poprzez dodanie do stringa kwadratowych nawiasów:
        `text[]` wewnątrz których umieszczamy liczby będące parametrami oznaczającymi miejsce rozpoczęcia, zakończenia
        a także krok podziału `[start:stop:step]`:
        
         * `text[0]` -> zwraca pierwszy znak
         * `text[-1]` -> zwraca ostatni znak
         * `text[0:3]` -> zwraca znaki od indeksu 0 do indeksu 2 (wynika to z faktu, że przedział jest lewostronnie
                         domknięty, to znaczy, że element znajdujący się pod indeksem końcowym nie zostanie włączony.)
         * `text[::4]` -> zwraca co 4 znak od początku do końca
         * `text[::-1]` -> zwraca odwrócone wyrażenie (txet) 
            
2. Rodzielanie napisów za pomocą metody `split()`
    - metoda `split()` pozwala na dzielenie tekstu np. podział wyrazów po spacji, przecinku.
      `Split()` jako parametr przyjmuje separator którym może być znak lub ciąg znaków rozdzielających fragment
      tekstu ktory chcemy podzielić. W wyniku działania tej metody otrzymujemy listę z elementami które są wynikiem
      podziału. 
      
         ```python
      zwierzęta = "kot,pies,papuga,chomik"
      zwierzęta.split(',')
      ['kot', 'pies', 'papuga', 'chomik']
        ```
   
3. Łączenie napisów za pomocą metody `join()`
    - kilka znaków lub wyrazów można połączyć w jedną całość poprzez użycie przed zbiorem elementów `"".join()`; pomiędzy 
    cudzysłowami podajemy separator, w nawiasach podajemy parametr czyli zmienną na której chcemy zastosować daną metodę
    
         ```python
      wyrazy = ['ala', 'ma', 'kota']
      " ".join(wyrazy)
      'ala ma kota'
         ```

4. Długość ciągu znaków
    - za pomocą metody `len()` możemy sprawdzić, z ilu znaków składa się string; należy pamiętać, że zliczane są
    również spacje i znaki przestankowe
    
        ```python
      text = "ala ma kota"
      x = len(text)
      print(x)
      11
        ```
    
5. Manipulowanie wielkością liter
    - do manipulowania wielkością liter służy kilka metod:
        * `upper()` -> tekst drukowanymi literami
        
             ```python
          text = "ala"
          text.upper()
          'ALA'
            ``` 
       
        * `lower()` -> tekst małymi literami
        
            ```python
          text = "ALA"
          text.lower()
          'ala'
          ``` 
        * `capitalize()` -> pierwsza litera wyrażenia drukowana
        
            ```python
          text = "ala ma kota"
          text.capitalize()
          'Ala ma kota'
          ```
        
        * `title()` -> pierwsza litera każdego słowa drukowana
        
            ```python
          text = "ala ma kota"
          text.capitalize()
          'Ala Ma Kota'
          ```
        
        * `swapcase()` -> zamienia małe litery na drukowane a drukowane na małe
        
            ```python
          text = "Ala MA kotA"
          text.capitalize()
          'aLA ma KOTa'
          ```
        
6. Walidacja napisów
    - jeśli tekst przechowywyany w zmiennej pochodzi z innego źródła np. od użytkowanika to trzeba dokonać jego
    walidacji. W tym celu wykorzystujemy mechanizmy wbudowane w Pythona które możemy rozpoznać po nazwie
    rozpoczynającej się od `is`
    
        * jesli chcemy sprawdzić, czy ciąg znaków składa się z samych liter możemy skorzystać z metody `isalpha()`:
        
            ```python
          "ala".isalpha()
          True
           ```
        
            ```python
          "ala1".isalpha()
          False
           ```
        
        * jesli chcemy sprawdzić, czy ciąg znaków składa się z samych cyfr możemy skorzystać z metody `isdigit()`:
        
             ```python
          "123".isdigit()
          True
           ```
        
             ```python
          "123.23".isdigit()
          False
           ```
        
        * jeśli chcemy sprawdzić, czy ciąg znaków składa się tylko ze znaków białych tzn spacji, tabów możemy wykorzystać
        metodę `isspace()`:
        
             ```python
          "   ".isspace()
          True
           ```
        
        * w podobny sposób możemy sprawdzić wielkość liter za pomocą metod `islower()`, `isupper()` oraz `istitle()`
    
7. Usuwanie niepotrzebnych znaków białych
    - jeśli string posiada niepotrzebne znaki białe możemy je usunąć wykorzystując metodę `strip()`:
    
         ```python
      "  ala   ".strip()
      'ala'
       ```
    
    - możemy również dokładnie zdefiniować, czy chcemy usunąć niepotrzebne znaki białe z lewej (`lstrip()`) lub
    z prawej (`rstrip()`) strony textu.
    
8. Znajdowanie wzorców w stringach
    - python posiada wbudowaną operację `in` która pozwala nam przy przetwarzaniu stringów sprawdzić,
    czy dany wzorzec tam występuje:
    
         ```python
      text = "ala ma kota"
      print("ala" in text)
      True
       ```
    
    - możemy uzyskać również informację o miejscu, w którym znajduje się konkretny ciąg znaków za pomocą metod
    `find()` oraz `index()`:
    
         ```python
      text = "ala ma kota"
      text.find('m')
      '4 -> zwrócony zostaje index litery m'
       ```
    
         ```python
      text = "ala ma kota"
      text.index('m')
      '4 -> zwrócony zostaje index litery m'
       ```
        
         ```python
      text = "ala ma kota"
      text.find('ola')
      '-1 -> jeśli wzorzec nie isnieje to metoda ta zwraca wartość -1'
      ```
    
         ```python
      text = "ala ma kota"
      text.index('ola')
      'ValueError -> jesli wzorzec nie istnieje to metoda index() zwraca błąd'
       ```

   - jeżeli dany wzorzec występuje więcej niż jeden raz, istnieje metoda `count()` która pozwala je policzyć:
    
        ```python
     text = "ala ma kota"
     text.count('a')
     4
        ```
    
   - istnieją metody `startwith()` oraz `endwith()` dzięki którym możemy sprawdzić, czy dany string rozpoczyna się
    lub kończy daną sekwencją znaków:
    
        ```python
     text = "Ala ma kota"
     print(text.startwith("Ala"))
     True
        ```
    
        ```python
     text = "Ala ma kota"
     print(text.endwith("psa"))
     False
        ```
    
   - wzorzec możemy zmienić na inny za pomocą metody `replace()` w której jako parametry podajemy co chcemy zastąpić,
    czym chcemy zastąpić oraz, jako trzeci parametr możemy podać cyfrę która ograniczy liczbę zmian:
    
        ```python
     "ala ma kota".replace(" ", ",")
     "ala,ma,kota"
           
     "ala ma kota".replace(" ", ",", 1)
     "ala,ma kota"
        ```

9. Bloki tekstowe
    - jeśli tworzymy zmienną która przechowuje tekst składający się z wielu linii i wcięć, możemy użyć bloków tekstowych
    aby zachować jego formatowanie:
    
        ```python
      text = """
      Lorem ipsum, dolor
          sit
      amet."""
        
      print(text)
        
      Lorem ipsum, dolor
          sit
      amet.
        ```

10. Nowe linie i tabulacja
    - w python istnieją znaki specjalne za pomocą których można umieścić znak na końcu linii (\n) oraz
    wykonać tabulację (\t) jednak używanie ich jest mniej czytelne niż bloki tekstu.
    
11. Funkcja print
    - funkcja print służy do wyświetlania elementów przekazanych jej jako parametr
    
        ```python
      print("ala ma kota")
      ala ma kota
        ```
    
    - można wyświetlać różne typy danych obok siebie
    - domyślnym separatorem jest spacja, można to zmienić poprzez przekazanie parametru `sep`
    
        ```python
      print("ala", "ma", "kota", sep="|")
      ala|ma|kota
        ```
    
    - funkcja print pozwala zapisywać tekst od razu do pliku, w tym celu trzeba ustawić wartość parametru file
    poprzez podanie zmiennej plikowej:
    
        ```python
      filename = 'test_file.txt'
      with open(filename, mode='w') as file:
          txt = 'wiadomość testowa'
          file.write(txt)
        
      with open('test_file.txt', mode='r') as file:
          file_content = file.read()
          print(file_content) 
          'wiadomość testowa'
        ```