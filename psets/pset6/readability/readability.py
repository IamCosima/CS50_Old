from cs50 import get_string

Let = 0
Word = 1
Sent = 0
# asking for the user to input Text

Text = get_string("Text: ")

# for loop to check whats is contained in the string
for i in range(len(Text)):
    # check if the char is a letter and inc Count
    if(Text[i].isalpha()):
        Let += 1

    # check if it is a whitespace and inc Words
    if (Text[i].isspace()):
        Word += 1

    # Check if it is the end of a sentence and inc sentence
    if (Text[i] == '!' or Text[i] == '?' or Text[i] == '.'):
        Sent += 1


# Algorithm for reading level
L = Let / Word * 100
S = Sent / Word * 100

index = 0.0588 * L - 0.296 * S - 15.8

# Rounding values and storing them into integers
In = round(index)
Let = round(Let)
Word = round(Word)
Sent = round(Sent)

# Checking the Level of Reading
if (index > 16):
    print("\nGrade 16+\n")

elif (index < 1):

    print("\nBefore Grade 1\n")

else:
    print("Grade", In)

