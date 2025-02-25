#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    // Start Size will Prompt until the number is greater than 9 or equal to 9
    int PopStartSize;
    do
    {
       PopStartSize = get_int("Enter Starting Population Size");
    }
    while (PopStartSize < 9);

    // TODO: Prompt for end size
     // End Size will Prompt until the number is greater than Start size
    int PopEndSize;
    do
    {
      PopEndSize = get_int("Enter Ending Population Size");
    }
    while (PopEndSize < PopStartSize);
    //Initialise the year to 0
    int year = 0;

    // TODO: Calculate number of years until we reach threshold

    //While Loop fpr calculation
    while (PopStartSize < PopEndSize)
      {
          PopStartSize = PopStartSize + (PopStartSize/3 - PopStartSize/4);
           ++year;
      }

    // TODO: Print number of years
    printf("Years: %i\n", year);
}
