import test_generator
import correct_brute_force
import mine
import filecmp

for i in range(1):
	test_generator
	mine
	correct_brute_force
	print('test '+str(i))
	if not filecmp.cmp('correct_output.txt', 'my_output.txt', shallow=False):
		print("Not good")
		break