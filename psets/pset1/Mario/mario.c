#include <cs50.h>
#include <stdio.h>

int main(void)
{

    //Prompting the user to enter a width value until it is between 1 and 8 inclusive
    int Width;
    do
    {
        Width = get_int("Enter the Height of the Pyramid");

    }
    while (Width <= 0 || Width >= 9);


    //For loop for making the Pyramid
    for (int I = 1; I <= Width; I++)// For loop for the Height of both pyramids
    {
        for (int L = Width - 1  ; L >= I ; --L) //For loop for making the Spaces to allign it to the right
        {
            printf(" ");
        }

        for (int j = 1 ; j <= I ; j++)//For loop For the Hashes
        {
            printf("#");
        }
        printf("\n");
    }


}
