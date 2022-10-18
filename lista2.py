lista = []
while True:
  num = input("Podaj liczbe: ")
  if num == "": break
  lista.append(float(num))
  print("najmniejsza liczba w twojej liscie:", min(lista))
  print(lista)