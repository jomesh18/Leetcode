import test_generator
import correct_brute_force
import test
import filecmp
import compare
import sys

for i in range(1):
	test_generator
	test
	correct_brute_force
	if compare:
		sys.stdout.write('not good '+str(i))
		break
