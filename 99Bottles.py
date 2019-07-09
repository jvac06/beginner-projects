#Create a program that prints out every line to the song "99 bottles of beer on the wall."
#Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
#Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#Remember, when you reach 1 bottle left, the word "bottles" becomes singular

def beerCountDown(bottle):
    while bottle > 0:
        lessBottle = bottle - 1
        if lessBottle <= 1:
            if bottle == 1:
                wordBottle = "bottle"
                print(str(bottle) + f" {wordBottle} of beer in the wall, " + str(bottle) +f" {wordBottle} of beer.\n"+"Take one down and pass it around, " + str(lessBottle) + " bottles of beer in the wall.")
                break
            else:
                print(str(bottle) + " bottles of beer in the wall, " + str(bottle) +" bottles of beer.\n"+"Take one down and pass it around, " + str(lessBottle) + " bottle of beer in the wall.")
        else:
            print(str(bottle) + " bottles of beer in the wall, " + str(bottle) +" bottles of beer.\n"+"Take one down and pass it around, " + str(lessBottle) + " bottles of beer in the wall.")
        bottle = lessBottle

if __name__ == "__main__":
    beerCountDown(99)
  
 
