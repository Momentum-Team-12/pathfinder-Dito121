from PIL import Image
from PIL import ImageColor
import numpy as np
import random

list_of_paths = []
class TopoMap:
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

        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                current_data_element = self.data[row][col]
                grayscale = (current_data_element - self.min_data) // ((self.max_data - self.min_data)//256 + 1)
                self.image.putpixel((col, row), (grayscale, grayscale, grayscale, 255))
        self.image.save(self.name_png)

    def find_greedy_path(self, starting_row):
        row = starting_row
        col = 0
        self.path = []
        current = self.data[row][col]
        self.path.append((col, row))

        while col < len(self.data[row])-1:
            right = self.data[row][col+1]

            if row-1 < 0:
                right_up = right
            else:
                right_up = self.data[row-1][col+1]

            if row+1 >= len(self.data):
                right_down = right
            else:
                right_down = self.data[row+1][col+1]

            diffs = [abs(current-right), abs(current-right_down), abs(current-right_up)]
            min_diff = min(diffs)

            if min_diff == diffs[0]:
                current = right
            elif diffs[1] == diffs[2] == min_diff:
                current = diffs[random.randint(1,2)]
                if current == right_down:
                    row += 1
                else:
                    row -= 1
            elif min_diff == diffs[1]:
                current = right_down
                row += 1
            elif min_diff == diffs[2]:
                current = right_up
                row -= 1

            col += 1
            self.path.append((col, row))
        list_of_paths.append(self.path)

    def chart_greedy_path(self):
        for i in range(len(list_of_paths)):
            for j in range(len(list_of_paths[i])):
                self.image.putpixel(list_of_paths[i][j], ImageColor.getcolor('red', 'RGBA'))
        self.image.save(self.name_png)

'''
elevation_large = TopoMap('elevation_large.txt')
elevation_large.txt_to_png()

for i in range(len(elevation_large.data)):
    elevation_large.find_greedy_path(i)

elevation_large.chart_greedy_path()
'''

'''
elevation_small = TopoMap('elevation_small.txt')
elevation_small.txt_to_png()

for i in range(len(elevation_small.data)):
    elevation_small.find_greedy_path(i)

elevation_small.chart_greedy_path()
'''

'''
elevation_test = TopoMap('elevation_test.txt')
elevation_test.txt_to_png()
elevation_test.find_greedy_path(6)
elevation_test.chart_greedy_path()
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
