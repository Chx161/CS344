import random
import string

# create filenam strings
file_1 = "output_1"
file_2 = "output_2"
file_3 = "output_3"

# Generate a string of 10 chars, end it with newline char
def create_string():
	output_string = ""
	for i in range(10):
		char_py = random.choice(string.ascii_lowercase)
		output_string = "%s%c"%(output_string, char_py)
	char_py = '\n'
	output_string = "%s%c"%(output_string, char_py)
	return output_string

# Create a file with filename, write to the file and open to read
def write_to_file(filename):
	# create a file and write a string
	f = open(filename, "w")
	string_py = create_string()
	f.write(string_py)
	f.close()
	#open and read the file after the writing:
	f = open(filename, "r")
	print(f.read(), end = "")

write_to_file(file_1)
write_to_file(file_2)
write_to_file(file_3)

def random_num():
	return random.randint(1, 42)

num_1 = random_num()
num_2 = random_num()
print(num_1)
print(num_2)
print(num_1*num_2)
