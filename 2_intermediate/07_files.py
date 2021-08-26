'''
R -> Read
W -> Write (overwrite current content)
A -> Add (new content at the end of the file)

  with open("./path/to/file.txt", "r") as file:
'''


def read():
	numbers = []
	with open("./test_files/numbers.txt", "r", encoding="utf-8") as file:
		for line in file:
			numbers.append(int(line))
	print(numbers)

def write():
	names = ["David", "Juan", "Miguel", "Lucía", "Alex"]
	with open("./test_files/names.txt", "w", encoding="utf-8") as file:
		for name in names:
			file.write(name)
			file.write("\n")

def run():
	write()

if __name__ == '__main__':
	run()