#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //Make sure there are 2 arguments
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw");
        return 1;
    }
    // Open input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        printf("Could not open File");
        return 2;
    }


    //variable for the buffer
    unsigned char buffer[512];
    //count var for filename
    int count = 0;

    //create output file(instancuate)
    FILE *output_file = NULL;
    //var for filename
    char *filename = malloc(8 * sizeof(char));

    //Read the recover file and save values into the array until the file is complete
    while (fread(buffer, sizeof(char), 512, inptr) != 0)
    {
        //Check to see if the file is a JPEG
        if (buffer[0] == 0xff &&  buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            sprintf(filename, "%03i.jpg", count);

            output_file = fopen(filename, "w");

            count++;
        }

        //Check to see if an output file is there to write too and write to it
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }


    }

    //close/free the files to stop mem leaks
    free(filename);
    fclose(output_file);
    fclose(inptr);

    return 0;
}