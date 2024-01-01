from tabulate import tabulate
import csv
import sys

def main():
    check()

    try:
        with open(sys.argv[1], 'r') as f:
            reader=csv.reader(f)
            for row in reader:
                print(row)


    except FileNotFoundError:
        sys.exit('file is not present')


def check():
    
    if len(sys.argv) > 2:
        sys.exit('Too many arguments')
    
    if len(sys.argv) < 2:
        sys.exit('Too few arguments')
    
    if ".csv" not in sys.argv[1]:
        sys.exit('not a csv file.')

if __name__ == "__main__":
    main()
    