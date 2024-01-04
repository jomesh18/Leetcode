import filecmp

if open('correct_output.txt').read() != open('my_output.txt').read():
	print('WA')
	exit(0)
else:
	print('test success')
