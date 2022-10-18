theSum = 0
count = 0
average = 0

while True:
    num = input("Wprowadź liczbę albo naciśnij enter aby zatwierdzić:")
    if num == "":
        break

    theSum += float(num)
    count += 1

average = theSum / count

print ("Suma wynosi", theSum)
print ("Średnia: ", average)