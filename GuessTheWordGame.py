#open dictionary.txt in the explorer tab
import random

#creates a list of all words in the dictionary
DictionaryFileName = "dictionary.txt"
OpenDictionary = open(DictionaryFileName)
WordList = list(OpenDictionary.read().splitlines())

#function to randomly select a word until it is 6 characters or less
def SelectWord():
    global SelectedWord
    global ScrambledWord
    SelectedWord = "aaaaaaa"
    while len(SelectedWord) > 6:
        WordNumber = random.randint(0, 79767)
        SelectedWord = WordList[WordNumber]
    #scrambles the selected word
    Letters = list(SelectedWord)
    random.shuffle(Letters)
    ScrambledWord = "".join(Letters)

GameRound = 1
PlayerLives = 3
PlayerScore = 0
#plays each round until all rounds have been played, or the player runs out of lives
while GameRound <= 2 and PlayerLives > 0:
    if GameRound != 1:
        print(" ")
        print("Random small word selected")
        print("Now playing Round " + str(GameRound))
        print(" ")
        GameRound = GameRound + 1
    else:
        print("Dictionary loaded, random small word selected")
        print("Now playing Round " + str(GameRound))
        print(" ")
        GameRound = GameRound + 1
    #performs the SelectWord function, and provides the scrambled word to the user, along with the true word for testing
    SelectWord()
    print("Your scrambled word is: " + str(ScrambledWord))
    print("*For testing and checking purposes* (Actual word is " + str(SelectedWord) + ")")
    print(" ")
    #ensures round 2 only begins once round 1 is completed
    CorrectGuess = False
    while CorrectGuess == False:
        PlayerGuess = (input("Please enter your guess for this word: "))
        #verifies the players guess is the correct length
        while len(PlayerGuess) != len(SelectedWord):
            print(" ")
            print("Your guess is an invalid length, please try again. No lives have been lost in this instance")
            PlayerGuess = (input("Please enter your guess for this word: "))
        #carries out the correct response to a correct or incorrect guess
        if PlayerGuess == SelectedWord:
            CorrectGuess = True
            PlayerScore = PlayerScore + int(len(SelectedWord))
            print("You guessed your word correctly!")
            print("You have been awarded " + str(len(SelectedWord)) + " points!")
            print(" ")
            if GameRound <= 2:
                print("Your current score is " + str(PlayerScore))
            PlayerLives = 3
            if GameRound <= 2:
                print("Your have all 3 lives again")
        else:
            PlayerLives = PlayerLives - 1
            print("You incorrectly guessed your word")
            if PlayerLives == 0:
                print("The correct answer was " + str(SelectedWord))
            print(" ")
            print("Your current score is " + str(PlayerScore))
            print("Your current life count is " + str(PlayerLives))
            print(" ")
            if PlayerLives == 0:
                CorrectGuess = True
                GameRound = 3
#displays the end-of-game results
if PlayerLives == 0:
    print("Unfortunately you have run out of lives")
if PlayerScore == 0:
    print("Unfortunately you did not score any point, better luck next time")
else:
    print("Congratulations! Your final score was " + str(PlayerScore) + " points!")