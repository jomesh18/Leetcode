import test_generator
import correct_brute_force
import mine
import filecmp

for i in range(1000):

	test_generator
	correct_brute_force
	mine
	print('Test '+str(i))
	if not filecmp.cmp('correct.txt', 'my_out.txt', shallow=False):
		print("Not good")
		break