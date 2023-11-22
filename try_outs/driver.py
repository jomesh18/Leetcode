import test_generator
import correct_brute_force
import test
import filecmp

for i in range(100000):

	test_generator
	correct_brute_force
	test
	print('Test '+str(i))
	if not filecmp.cmp('correct.txt', 'my_out.txt', shallow=False):
		print("Not good")
		break