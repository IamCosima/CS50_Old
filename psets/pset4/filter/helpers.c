#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float aveRGB;
    //Iterate through the height of the image
    for (int i = 0; i < height; i++)
    {
        //Iterate through the Width of the image
        for (int j = 0; j < width; j++)
        {
            aveRGB = round(((float) image[i][j].rgbtBlue + (float)  image[i][j].rgbtGreen + (float) image[i][j].rgbtRed) / 3);
            image[i][j].rgbtBlue = aveRGB;
            image[i][j].rgbtGreen = aveRGB;
            image[i][j].rgbtRed = aveRGB;
        }

    }

    return;


}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed, sepiaGreen, sepiaBlue;
    float originalRed, originalGreen, originalBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalBlue =  image[i][j].rgbtBlue;
            originalGreen = image[i][j].rgbtGreen;
            originalRed =  image[i][j].rgbtRed;

            //calculate for sepiaColor
            sepiaRed = round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);


            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
            }

            //calculate for sepiaGreen
            sepiaGreen = round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }
            //Calculate for sepiaBlue
            sepiaBlue = round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);
            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaBlue;
            }


        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temR, temB, temG;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            temB =  image[i][j].rgbtBlue;
            temG =  image[i][j].rgbtGreen;
            temR =  image[i][j].rgbtRed;

            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;

            image[i][width - j - 1].rgbtRed = temR;
            image[i][width - j - 1].rgbtGreen = temG;
            image[i][width - j - 1].rgbtBlue = temB;

        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    int r = 0;
    int g = 0;
    int b = 0;


    return;
}
