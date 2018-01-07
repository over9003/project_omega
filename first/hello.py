class Test(object):

	@staticmethod
	def FirstMethod():
		print "this is the first method"
	
	@staticmethod
	def SecondMethod():
		print "this is the second method"

	@staticmethod
	def ThirdMethod():
		print "this is the thidr method"
	
if '__init__' == '__main__':
	Test.FirstMethod()
	Test.SecondMethod()
	Test.ThirdMethod()
