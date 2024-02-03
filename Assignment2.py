from PIL import Image
from typing import List

def mirror(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw by reversing all the rows
    of the data.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> mirror(raw)
    >>> raw
    [[[255, 255, 255], [0, 0, 0], [233, 100, 115]],
     [[255, 255, 255], [1, 9, 0], [199, 201, 116]]]
    """
    for row in raw:
        row.reverse()
    return


def grey(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> grey(raw)
    >>> raw
    [[[149, 149, 149], [0, 0, 0], [255, 255, 255]],
     [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
    """
    for row in raw:
        for pixel in row:
            average_value = sum(pixel) // 3
            for i in range(3):
                pixel[i] = average_value


def invert(raw: List[List[List[int]]])->None:
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """
    for row in raw:
        for pixel in row:
            max_value = max(pixel)
            min_value = min(pixel)
            for i in range(3):
                if pixel[i] == max_value:
                    pixel[i] = min_value
                elif pixel[i] == min_value:
                    pixel[i] = max_value


def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    """
    Merges raw1 and raw2 into new raw image data and returns it.
    It merges them using the following rule/procedure.
    1) The new raw image data has height equal to the max height of raw1 and raw2
    2) The new raw image data has width equal to the max width of raw1 and raw2
    3) The pixel data at cell (i,j) in the new raw image data will be (in this order):
       3.1) a black pixel [255, 255, 255], if there is no pixel data in raw1 or raw2
       at cell (i,j)
       3.2) raw1[i][j] if there is no pixel data at raw2[i][j]
       3.3) raw2[i][j] if there is no pixel data at raw1[i][j]
       3.4) raw1[i][j] if i is even
       3.5) raw2[i][j] if i is odd
    """
    if len(raw1) == 0:
       return raw2
    elif len(raw2) == 0:
       return raw1
    result = []
    for i in range(max(len(raw1), len(raw2))):
        result.append([])
        for j in range(max(len(raw1[0]), len(raw2[0]))):
            result[i].append([])
    for i in range(len(result)):
        for j in range(len(result[0])):
            if (i > len(raw1) - 1 or j > len(raw1[0]) -1) and (i > len(raw2)-1 or j > len(raw2[0]) - 1):
                result[i][j] = [255,255,255]
            elif (i > len(raw1) - 1 or j > len(raw1[0]) -1):
                result[i][j] = raw2[i][j]
            elif (i > len(raw2) - 1 or j > len(raw2[0]) -1):
                result[i][j] = raw1[i][j]
            elif i % 2 == 0:
                result[i][j] = raw1[i][j]
            else:
                result[i][j] = raw2[i][j]
    return result



def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:
    """
    Compresses raw by going through the pixels and combining a pixel with
    the ones directly to the right, below and diagonally to the lower right.
    For each RGB values it takes the average of these four pixels using integer
    division. If is is a pixel on the "edge" of the image, it only takes the
    relevant pixels to average across. See the second doctest for an example of
    this.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
    >>> compress(raw)
    >>> raw
    [[[108, 77, 57], [153, 115, 26]],
     [[63, 79, 87], [191, 51, 33]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
    >>> compress(raw)
    >>> raw
    [[[108, 77, 57], [255, 177, 50]],
     [[117, 166, 80], [0, 1, 1]]]
    """
def compress(raw: List[List[List[int]]]) -> List[List[List[int]]]:
    result = []
    for i in range(len(raw)//2 + len(raw) % 2):
        result.append([])
        for j in range(len(raw[i])//2 + len(raw[i]) % 2):
            result[i].append([])
    for i in range((len(raw)//2 + len(raw) % 2)):
        for j in range((len(raw[i])//2 + len(raw[i]) % 2)):
            for k in range(3):
                if j * 2 + 1 > len(raw[0]) - 1 and i * 2 + 1 > len(raw) - 1:
                    result[i][j] = raw[i * 2][j * 2]
                elif j * 2 + 1 > len(raw[0]) - 1:
                    result[i][j].append((raw[i * 2][j * 2][k] + raw[i * 2 + 1][j * 2][k])//2)
                elif i * 2 + 1 > len(raw) - 1:
                    result[i][j].append((raw[i * 2][j * 2][k] + raw[i * 2][j * 2 + 1][k])//2)
                else:
                    result[i][j].append((raw[i * 2][j * 2][k] + raw[i * 2][j * 2 + 1][k] + raw[i * 2 + 1][j * 2][k] + raw[i * 2 + 1][j * 2 + 1][k])//4)
    return result






"""
**********************************************************

Do not worry about the code below. However, if you wish,
you can us it to read in images, modify the data, and save
new images.

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data


def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)

L = get_raw_image("assignments/assignment 2/tree.png")

mirror(L)

image_from_raw(L, "assignments/assignment 2/mirror.png")

    
