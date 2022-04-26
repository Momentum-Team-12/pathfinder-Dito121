class ShortestPath:

    file = 'elevation_test.txt'

    def get_data():
        data = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].split()
                data.append([])
                for j in range(len(lines[i])):
                    data[i].append(int(lines[i][j]))
            return data


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
