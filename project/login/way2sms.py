import requests

class sms:

	def __init__(self,username,password):

		self.url='http://site24.way2sms.com/Login1.action?'

		self.cred={'username': username, 'password': password}

		self.s=requests.Session()			# Session because we want to maintain the cookies
		

		self.s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"

		self.q=self.s.post(self.url,data=self.cred)

		self.loggedIn=False				# a variable of knowing whether logged in or not

		if self.q.status_code!=200:			# http status 200 == OK

			self.loggedIn=False

		else:

			self.loggedIn=True
		self.jsid=self.s.cookies.get_dict()['JSESSIONID'][4:]	    # JSID is the main KEY as JSID are produced every time a session satrts


	def send(self,mobile_no,msg):

		self.payload={'ssaction':'ss',
				'Token':self.jsid,		
			        'mobile':mobile_no,					
       				 'message':msg,						
			        'msgLen':'129'
       			     }

		self.msg_url='http://site24.way2sms.com/smstoss.action'

		self.q=self.s.post(self.msg_url,data=self.payload)
		self.s.get('http://site24.way2sms.com/entry?ec=0080&id=dwks')

		self.s.close()								# close the Session

		self.loggedIn=False