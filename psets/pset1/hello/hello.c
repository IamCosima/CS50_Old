#include <cs50.h> /* cs50 Lib*/
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name?"); /* get the string to put into the printf */
    printf("hello, %s\n", name); /* Name is the variable that is used to store the answer */
}