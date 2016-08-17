class PrimeChecker(object):
	def __init__(self,number=""):
		self.number=number
	def is_prime(self):
		if self.number=="":
			return False
		else:
			self.number=int(self.number)
			if self.number==1:
				return False
			else:
				for value in range(2,int(self.number**0.5)+1):
					if self.number%value==0:
						return False
				return True
