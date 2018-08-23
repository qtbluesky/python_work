#
#try:
#	s = raw_input("enter something.....: \n")
#except EOFError:
#	print "This is a EOFError..."
#else:
#	print("The content you input is:\n" + s)
#	
#
try:
	s = raw_input("enter something.....: \n")
except Exception,e:
	print "This is a error:"+str(e)
else:
	print "The content you input is:\n" + s
	

