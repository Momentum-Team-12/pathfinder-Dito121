from subprocess import CREATE_NEW_CONSOLE
from PIL import Image

class File:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        data = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].split()
                data.append([])
                for j in range(len(lines[i])):
                    data[i].append(int(lines[i][j]))
            return data

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

def create_image(file):
    pixels = get_data(file)
    Image.new('RGBA' , (600, 600), 'white')
    Image.save('file_name.png')


create_image('elevation_small.txt')


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
