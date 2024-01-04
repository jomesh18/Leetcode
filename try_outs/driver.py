import os

for i in range(100):
	os.system('test_generator.py > input.txt')
	os.system('correct_brute_force.py < input.txt > correct_output.txt')
	os.system('test.py < input.txt > my_output.txt')
	if open('correct_output.txt').read() != open('my_output.txt').read():
		print('WA', i)
		exit(0)
	else:
		print('test success', i)
