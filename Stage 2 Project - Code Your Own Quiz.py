# IPND Stage 2 Final Project
# Build a Fill-in-the-Blanks quiz.
# Prompt a user with a paragraph containing several blanks.
# Ask user to fill in each blank appropriately to complete the paragraph


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Welcome message
def welcomeMessage():
    print "\n"
    print "************************************************"
    print "Welcome to the Star Spangled Banner Lyrics Quiz!"
    print "************************************************"
    print "\n"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Prompt user to select desired quiz level
def selectQuizLevel():
    print "Quiz levels: "
    print "1 - First verse"
    print "2 - Second verse"
    print "3 - Third verse"
    print "4 - Fourth verse"
    print "\n"
    global quizLevel
    quizLevel = raw_input("Enter a number 1-4 to select a verse: ")

# Check that user input is an appropriate number
    if quizLevel == "1" or quizLevel == "2" or quizLevel == "3" or quizLevel == "4":
        print "\n" + "You selected verse " + quizLevel + "."
# If user input is not an appropriate number, reprompt
    else:
        print "\n" + "ERROR! Please enter 1, 2, 3, or 4 to select a verse." + "\n"
        selectQuizLevel()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Prompt user to select number of guesses for each question (1-10)
def selectNumTries():
    global numTries
    numTries = raw_input("Now choose how many tries you have for each question (1-10): ")

# Check that user input is an appropriate number
    if numTries == "1" or numTries == "2" or numTries == "3" or numTries == "4" or numTries == "5" or numTries == "6" or numTries == "7" or numTries == "8" or numTries == "9" or numTries == "10":
        print "\n" + "You selected " + numTries + " try/tries for each question. Let's begin."
# If user input is not an appropriate number, reprompt
    else:
        print "\n"
        print "ERROR!" + "\n" + "Please enter an integer 1-10 to choose how many tries you have for each question."
        selectNumTries()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Show paragraph with numbered blanks 4 or more blanks to fill in)
def printBlankVerse():
    print "This is verse " + quizLevel + " of the 'Star Spangled Banner':" + "\n"

    if quizLevel == "1":
        print blankVerse1
    if quizLevel == "2":
        print blankVerse2
    if quizLevel == "3":
        print blankVerse3
    if quizLevel == "4":
        print blankVerse4

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Star Spangled Banner Verses with blanks for quiz

global blankVerse1
blankVerse1 = """\
O say can you [__1__], by the dawn's early light,
What so proudly we hail'd at the twilight's last gleaming,
Whose broad [__2__] and bright [__3__] through the perilous fight
O'er the ramparts we watch'd were so gallantly streaming?
And the rocket's red glare, the bombs bursting in air,
Gave proof through the night that our [__4__] was still there,
O say does that star-spangled banner yet wave
O'er the land of the free and the home of the brave?
"""
# [1] = see, [2] = stripes, [3] = stars, [4] = flag

global blankVerse2
blankVerse2 = """\
On the shore dimly seen through the mists of the deep
Where the foe's haughty host in dread silence reposes,
What is that which the breeze, o'er the towering steep,
As it fitfully blows, half conceals, half discloses?
Now it catches the gleam of the morning's first beam,
In full glory reflected now shines in the stream,
'Tis the star-spangled [__1__] - O long may it [__2__]
O'er the land of the [__3__] and the home of the [__4__]!
"""
# [1] = banner, [2] = wave, [3] = free, [4] = brave

global blankVerse3
blankVerse3 = """\
And where is that band who so vauntingly swore,
That the havoc of war and the battle's confusion
A home and a [__1__] should leave us to more?
Their blood has wash'd out their foul footstep's pollution.
No [__2__] could save the hireling and slave
From the terror of flight or the gloom of the grave
And the star-spangled banner in [__3__] doth wave
O'er the land of the [__4__] and the home of the brave.
"""
# [1] = Country, [2] = refuge, [3] = triumph, [4] = free

global blankVerse4
blankVerse4 = """\
O thus be it ever when freemen shall stand
Between their lov'd [__1__] and the war's desolation!
Blest with vict'ry and [__2__] may the heav'n rescued land
Praise the power that hath made and [__3__] us a nation!
Then conquer we must, when our cause it is just,
And this be our motto - "In God is our trust,"
And the star-spangled banner in triumph shall wave
O'er the [__4__] of the free and the [__1__] of the brave.
"""
# [1] = home, [2] = peace, [3] = preserv'd, [4] = land


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Check to see if user's word guess is correct
def checkWordGuess(quizLevel, verseBlankNumber, wordGuess):

    verse1answers = ["see", "stripes", "stars", "flag"]
    verse2answers = ["banner", "wave", "free", "brave"]
    verse3answers = ["Country", "refuge", "triumph", "free"]
    verse4answers = ["home", "peace", "preserv'd", "land"]

    global checkWordGuessResult

    if quizLevel == "1" and verse1answers[verseBlankNumber-1] == wordGuess:
        checkWordGuessResult = "Correct"
    elif quizLevel == "2" and verse2answers[verseBlankNumber-1] == wordGuess:
        checkWordGuessResult = "Correct"
    elif quizLevel == "3" and verse3answers[verseBlankNumber-1] == wordGuess:
        checkWordGuessResult = "Correct"
    elif quizLevel == "4" and verse4answers[verseBlankNumber-1] == wordGuess:
        checkWordGuessResult = "Correct"
    else:
        checkWordGuessResult = "Wrong"

    return checkWordGuessResult

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Set string to be updated with verse corresponding to user selected quizLevel
def setVerseToUpdate(quizLevel):

    global verseToUpdate

    if quizLevel == "1":
        verseToUpdate = blankVerse1
    elif quizLevel == "2":
        verseToUpdate = blankVerse2
    elif quizLevel == "3":
        verseToUpdate = blankVerse3
    elif quizLevel == "4":
        verseToUpdate = blankVerse4
    return verseToUpdate


##########################################################
# Build a Fill-in-the-Blanks quiz
##########################################################

# Prompt a user with a paragraph containing several blanks
welcomeMessage()
selectQuizLevel()
selectNumTries()
printBlankVerse()

# Ask user to fill in each blank appropriately to complete the paragraph
numTriesLeft = int(numTries)
verseBlankNumber = 1
setVerseToUpdate(quizLevel)

while (verseBlankNumber < 5):
    wordGuess = raw_input("You have " + str(numTriesLeft) + " try/tries left to guess the word for blank number " + str(verseBlankNumber) + ": ")
    checkWordGuess(quizLevel, verseBlankNumber, wordGuess)

    if checkWordGuessResult == "Correct":
        print "\n" + "Nice Job! Here is the updated verse: " + "\n"
        verseBlanks = ["[__1__]", "[__2__]", "[__3__]", "[__4__]"]
        verseToUpdate = verseToUpdate.replace(verseBlanks[verseBlankNumber-1], wordGuess)
        print verseToUpdate
        numTriesLeft = numTries
        verseBlankNumber = verseBlankNumber + 1
        if verseBlankNumber == 5:
            print "Congratulations! You completed the verse correctly."

    elif checkWordGuessResult != "Correct":
        numTriesLeft = int(numTriesLeft) - 1
        if numTriesLeft == 0:
            print "Wrong word. You have no more tries left. Game over."
            break
        print "Wrong word. Try again." + "\n"
