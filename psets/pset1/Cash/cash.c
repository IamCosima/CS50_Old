#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float Owed;//Amount Entered by the user
    do
    {
        Owed = get_float("Enter Owed Amount: ");//Loop until the value entered by the user is > 0
    }
    while (Owed < 0);


    int Counter = 0;


    Owed = Owed * 100;//Changing from dollars to cents


    int Cents = round(Owed);// Rounding off to stop floating point precision errors


    while (Cents >= 25)//Checking if 25 can be subtracted
    {
        Cents = Cents - 25;
        ++Counter;

    }
    while (Cents >= 10) //Checking if 10 can be subtracted
    {
        Cents = Cents - 10;
        ++Counter;
    }
    while (Cents >= 5) //Checking if 5 can be subtracted
    {
        Cents = Cents - 5;
        ++Counter;
    }

    while (Cents >= 1) //Checking if 1 can be subtracted
    {
        Cents = Cents - 1;
        ++Counter;
    }

    printf("%i\n", Counter); //Returning Value to the user
}