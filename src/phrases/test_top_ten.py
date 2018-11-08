import subprocess

test = subprocess.check_output("phrases pg2009.txt", shell=True)
test2 = subprocess.check_output("phrases pg2009.txt", shell=True)

if test2 == test:
    print("{}".format("TRUE"))
