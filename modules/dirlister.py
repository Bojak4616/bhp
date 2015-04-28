import os

def run(**args):
	print "[+] In dirlister Module"
	files = os.listdir(".")
	
	return str(files)


