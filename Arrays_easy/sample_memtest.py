@profile
def mem_test(s):
	for i in range(1000):
		s += 'a'

s = ""
mem_test(s)

# @profile
# def mem_test(s):
# 	l = []
# 	for i in range(100):
# 		l.append('a')
# 	s = ''.join(l)
# 	print(s)

# s = ""
# mem_test(s)
