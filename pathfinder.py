from PIL import Image
import numpy as np


class TextFile:
    # file_name is name of text file with elevation data
    def __init__(self, name_txt):
        self.name_txt = name_txt
        self.name_png = self.name_txt[:-3] + 'png'
        self.set_data()

    def set_data(self):
        self.data = []

        with open(self.name_txt, 'r') as f:
            lines = f.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].split()
                self.data.append([])

                for j in range(len(lines[i])):
                    self.data[i].append(int(lines[i][j]))

        self.min_data = np.amin(self.data)
        self.max_data = np.amax(self.data)
        self.size_data = (len(self.data), len(self.data[0]))

    def txt_to_png(self):
        self.image = Image.new('RGBA', self.size_data, 'white')
        self.image.save(self.name_png)

        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                current_data_element = self.data[x][y]
                grayscale = (current_data_element - self.min_data) // ((self.max_data - self.min_data)//256 + 1)
                self.image.putpixel((y, x), (grayscale, grayscale, grayscale, 255))
        self.image.save(self.name_png)


elevation_small = TextFile('elevation_small.txt')
elevation_small.txt_to_png()


'''
def next_step(self, pixels):
    right_up = 
    right = 
    right_down = 
'''

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
