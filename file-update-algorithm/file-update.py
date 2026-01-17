#Assign 'import_file' to the name of the file
#*********For testing purposes this can be changed**************
import_file = "allow_list.txt"

#Assign remove_list to a list of IP addresses that are no longer allowed to access restricted info
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

#Opening and reading through the imported file. 
with open(import_file, "r") as file:
	#Using the .read() function to read the imported file and store it in a 
	#variable named 'ip_addresses'
	ip_addresses = file.read()
#Using the .split() function to convert 'ip_addresses' from a string -> list
ip_addresses = ip_addresses.split()

#Building an iterative statement that loops through the list of IPs 
for element in ip_addresses:
	#If the current element is in the remove list
	if element in remove_list:
		#Then the current element shhould be removed from 'ip_addresses'
		ip_addresses.remove(element)

#Convert ip_addresses back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)

#Building a with statement to rewrite the original file
with open(import_file, "w") as file:
	#Rewrite the file, replacing ints content with 'ip_addresses'.
	file.write(ip_addresses)


#Displaying 'ip_addresses'
print(ip_addresses)
