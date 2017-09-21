import random
print "Igra - Ugani stevilo"
secret = random.randint(0,50)
guess = 0
index=1

while True:

    guess = int (raw_input("Ugani stevilo med 0 in 50:"))
    index += 1
    if guess == secret:
        print "Cestitam, uganil si v poskusu st. " + str(index)
        break
    elif guess > secret:
        print "Stevilo je manjse"
        if index >= 5:
            print "Konec je ugibanja, 5x si ze ugibal. Stevilo, ki si ga iskal je: " + str(secret)
            break
    elif guess < secret:
        print "Stevilo je vecje"
        if index >= 5:
            print "Konec je ugibanja, 5x si ze ugibal. Stevilo, ki si ga iskal je: " + str(secret)
            break