#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    //Float values for Prescision
    float index;
    float L;
    float S;
    float Count = 0;
    float Words = 1;
    float Sentence = 0;
    //Values to put the rounded float values
    int Let;
    int Word;
    int Sent;
    int In;
    //asking for the user to input Text
    string Text = get_string("Text: ");

    //for loop to check whats is contained in the string
    for (int j = 0, m = strlen(Text); j < m; j++)
    {
        //check if the char is a letter and inc Count
        if (isalpha(Text[j]))
        {
            ++Count;
        } //check if it is a whitespace and inc Words
        if (isspace(Text[j]))
        {
            ++Words;
        }//Check if it is the end of a sentence and inc sentence
        if (Text[j] == '!' || Text[j] == '?' || Text[j] == '.')
        {
            ++Sentence;
        }

    }
    // Algorithm for reading level
    L = Count / Words * 100;
    S = Sentence / Words * 100;

    index = 0.0588 * L - 0.296 * S - 15.8;
    //Rounding values and storing them into integers
    In = round(index);
    Let = round(Count);
    Word = round(Words);
    Sent = round(Sentence);

    //Printing the Output
    printf("%i Letter(s)", Let);
    printf("\n%i Words(s)", Word);
    printf("\n%i Sentence(s)", Sent);

    //Checking the Level of Reading
    if (index > 16)
    {
        printf("\nGrade 16+\n");
    }
    else if (index < 1)
    {
        printf("\nBefore Grade 1\n");
    }
    else
    {
        printf("\nGrade %i\n", In);
    }

}