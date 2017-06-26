import sys
import os
import subprocess

def make_ps(username):
	print(username)
	make_f = open("make_error", "w+")
	subprocess.call(["make", "re", "-C" + username + "/push_swap"], stderr=make_f)
	make_f.close
	if (os.stat("make_error").st_size != 0):
		return (make_f)
	else:
		return (0)

def test_ps(username):
	pass


print make_ps(str(sys.argv[1]))

