"""
File: stanCodoshop.py
Name: Jerry Yu
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    red_avg = red
    green_avg = green
    blue_avg = blue
    # calculating the color distance
    c_d = ((red_avg-pixel.red)**2 + (green_avg-pixel.green)**2 + (blue_avg - pixel.blue)**2)
    color_distance = math.sqrt(c_d)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # red_total = 0
    # green_total = 0
    # blue_total = 0
    # # adding the value of every pixels together
    # for i in range(len(pixels)):
    #     red_total += pixels[i].red
    #     green_total += pixels[i].green
    #     blue_total += pixels[i].blue
    # # calculating the average by dividing the total amount with the number of pixels
    # red = red_total//len(pixels)
    # green = green_total//len(pixels)
    # blue = blue_total//len(pixels)
    # rgb = [red, green, blue]
    # return rgb
    total_r = sum(pixel.red for pixel in pixels)
    total_g = sum(pixel.green for pixel in pixels)
    total_b = sum(pixel.blue for pixel in pixels)
    avg_lst = [total_r//len(pixels), total_g//len(pixels), total_b//len(pixels)]
    return avg_lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg = get_average(pixels)
    dist_lst = []
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        dist_lst.append((dist, pixel))
    return min(dist_lst, key=lambda ele: ele[0])[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size
    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # extracting image from images
    for x in range(width):
        for y in range(height):
            pixel_lst = []
            for i in range(len(images)):
                pixel_lst.append(images[i].get_pixel(x, y))
            result.get_pixel(x, y).red = get_best_pixel(pixel_lst).red
            result.get_pixel(x, y).green = get_best_pixel(pixel_lst).green
            result.get_pixel(x, y).blue = get_best_pixel(pixel_lst).blue

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
