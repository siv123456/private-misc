import subprocess

class Day2Day:

    def __init__(self):
        pass

    def restart(self):
        subprocess.call(["shutdown", "/r"])

    def logoff(self):
        subprocess.call(["shutdown", "/l"])

    def shutdown(self):
        subprocess.call(["shutdown", "/s"])

d2d = Day2Day()
a = raw_input("Please Select S/L/R: ")
if a.strip() == 's':
    d2d.shutdown()
if a.strip() == 'l':
    d2d.logoff()
if a.strip() == 'r':
    d2d.restart()

