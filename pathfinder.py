from PIL import Image
from PIL import ImageColor
import numpy as np


def get_data(file):
    elevation_data = []

    with open(file, 'r') as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].split()
            elevation_data.append([])

            for j in range(len(lines[i])):
                elevation_data[i].append(int(lines[i][j]))
        return elevation_data


'''
class Pixel:
    def __init__(self, pixels):
        self.data = data

    def get_rgba(self, pixels):
        for i in range(len(pixels)):


    def next_step(self, pixels):
        right_up = 
        right = 
        right_down = 
'''

file = 'elevation_small.txt'


def create_image(file, size=(600,600)):
    elevation_data = get_data(file)
    new_image = Image.new('RGBA' , size, 'white')
    new_image.save('elevation_small.png')
    return elevation_data, new_image


def modify_image():
    elevation_data, new_image = create_image(file)
    max_elevation = np.amax(elevation_data)
    min_elevation = np.amin(elevation_data)

    for x in range(len(elevation_data)):
        for y in range(len(elevation_data[x])):
            current_elevation = elevation_data[x][y]
            A = (current_elevation - min_elevation) // ((max_elevation - min_elevation)//256 + 1)
            new_image.getpixel((0, 0))
            new_image.putpixel((x, y), (255-A, 255-A, 255-A))


modify_image()

'''
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='Read elevations from a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        get_data(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
'''
