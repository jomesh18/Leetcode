import test_generator
import correct_brute_force
import test
import filecmp

for i in range(10):
	test_generator
	test
	correct_brute_force
	# if not filecmp.cmp('correct_output.txt', 'my_output.txt', shallow=False):
	# 	print("test", i)
	# 	print("Not good")
	# 	break