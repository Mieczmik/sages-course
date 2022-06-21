# ZADANIE 5 : dla poniższych list stwórz listę tupli,
# której pierwszy element
# stanowi iloraz wysokości przez liczbę pięter,
# drugi element to sama nazwa kraju
# z listy 'miejsca', a trzeci element to nazwa budynku:
wysokosci = [829, 632, 601,599.3,554.5 ]
liczba_pieter = [163, 128,120,115,123]
miejsca = ['Dubaj, Zjednoczone Emiraty Arabskie','Szanghaj, Chiny','Mekka, Arabia Saudyjska', 'Shenzhen, Chiny', 'Seul, Korea Południowa']
nazwy = ['Burj Khalifa', 'Shanghai Tower','Abradż al-Bajt','Ping An Finance Centern','Lotte World Tower']

list_of_tuple = [(wysokosci[i] / liczba_pieter[i], miejsca[i], nazwy[i]) for i in range(len(wysokosci))]
print(list_of_tuple)