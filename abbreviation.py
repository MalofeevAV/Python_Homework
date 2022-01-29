import sys
import re


def main():
	with open(sys.argv[1], "r", encoding="utf-8") as f:
		text = f.read()

	pattern = r'(?:[А-ЯA-Z]{2,}\s)+'
	result = re.findall(pattern, text)
	return result

if __name__ == '__main__':
	[print(i) for i in main()]