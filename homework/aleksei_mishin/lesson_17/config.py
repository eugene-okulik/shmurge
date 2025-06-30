import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filepath', help='Please specify the full path to the file.')
parser.add_argument('--text', help='Please enter a keyword to search for.')
args = parser.parse_args()

FILEPATH = args.filepath
KEYWORD = args.text
