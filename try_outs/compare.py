import filecmp

def main():
	return filecmp.cmp('my_output.txt', 'correct_output.txt', shallow=False)

if __name__ == main:
	main()