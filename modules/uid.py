import os

def run (**args):
	print "[+] In UID Module."
	return str(os.geteuid())
