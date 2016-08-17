def find_missing(array_1,array_2):
	if len (array_1) is 0 and len (array_2) is 0:
		return 0
	if len(array_1)> len(array_2):
		for item in array_1:
			if item in array_2:
				continue
			else:
				return item
	else:
		for item in array_2:
			if item in array_1:
				continue
			else:
				return item
	return 0