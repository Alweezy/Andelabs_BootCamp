def string_length(my_string):
 	res = []
 	if type(my_string) == str:
  		str_length = len(my_string)
  		res.append(str_length)
  	elif type(my_string)== list:
  		for item in range(len(my_string)):
  			res.append(len(my_string[item]))
	return res



print string_length(["michael", "william","smith"])
