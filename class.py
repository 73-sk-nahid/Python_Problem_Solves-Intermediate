class MyClass:
	id = 0		# assigning value to MyClass attributes
	name = 'Null'

def Main():
	# Creating an object of my class
	# here me is the object
	me = MyClass()
	# Accessing the attribute of MyClass
	# using the dot operator
	me.id = 73
	me.name = 'Sk. Nahid'
	print(me.name + '  ' +str(me.id))

if __name__=='__main__':   

        Main() 