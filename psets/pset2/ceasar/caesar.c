#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //Checking if the user inputted 1 argumnet if not print out an error
    string key;
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //store value of the key and declare the int to store the value once validated
    key = argv[1];
    int Ceasar;
    for (int i = 0, m = strlen(key); i < m; i++)
    {
        //Check if a valid argument is made and that it is a number and not a letter of the alphabet else print Error
        if (isdigit(key[i]))
        {
            Ceasar = atoi(key);
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    //Change the Plaintext to a Ciphered text
    string PlainText = get_string("Enter Plaintext");
    printf("plaintext: %s\n", PlainText);
    string Cipher = PlainText;
    // Go through the chars of the string and change them according to the Caesar’s algorithm denoted as ci = (pi + k) % 26
    for (int j = 0, n = strlen(Cipher); j < n; j++)
    {
        // Checks if it is a uppercase letter and then keeps it uppercase when adding the key
        if (isupper(Cipher[j]))
        {
            Cipher[j] = ((Cipher[j] - 65) + Ceasar) % 26 + 65;
        }
        //Checks if it is lowercase and keeps it lowercase when adding the key
        else if (islower(Cipher[j]))
        {
            Cipher[j] = ((Cipher[j] - 97) + Ceasar) % 26 + 97;

        }
        //If not any of the above leave it the same and do not change it
        else
        {
            Cipher[j] = Cipher[j];
        }
    }

    //Print out of the output
    printf("ciphertext: %s\n", Cipher);
}