try:
	import sys,requests,os,mechanize
	from bs4 import BeautifulSoup as bs
except Exception as E:
	print ("Warning(ERROR): %s"%(E))
	sys.exit()
class sms:
	def __init__(self):
		self.br=mechanize.Browser()
		self.br.addheaders=[("Connection", "keep-alive"),
		("Pragma","no-cache"),
		("Cache-Control", "max-age=0"),
		("Origin", "http://sms.payuterus.biz/alpha/"),
		("Upgrade-Insecure-Requests", "1"),
		("Content-Type", "application/x-www-form-urlencoded"),
		("User-Agent", "Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36"),
		("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"),
		("Referer", "http://sms.payuterus.biz/alpha/"),
		("Accept-Encoding", "gzip, deflate, br"),
		("Accept-Language", "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"),
		("Cookie", "PHPSESSID=33d1fdc8a2402fa66af7dafcf7e7b130; TawkConnectionTime=0; __tawkuuid=e::sms-gratis.xyz::qZv66ac2OqmFl7oOZz7jEwYnjOsSJFw20AamndIekFhi2rfbRxkAwi/aSSkp0bY0::2; c_popup=lFnGIuNXMC")]
		self.u="http://sms.payuterus.biz/alpha/"
#		self.server=self.cek_server()
		server=self.cek_server()
		self.banner(server)
		self.settings()
	def cek_server(self):
		r=requests.get(self.u)
		b=bs(r.content,"html.parser")
#		f=b.findAll(id="container")
		f=b.findAll("font")
		rp=str(f).replace('[<font color="red">','').replace("</font>]","").replace('[<font color="green">','').replace("</font>]","")
		return str(rp)
	def banner(self,server):
		print ("""
     ╔═╗╔╦╗╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦╔═╗
     ╚═╗║║║╚═╗  ║ ╦╠╦╝╠═╣ ║ ║╚═╗
     ╚═╝╩ ╩╚═╝  ╚═╝╩╚═╩ ╩ ╩ ╩╚═╝
  {C}odded        : Billal
  {V}ersion       : 0.1
  {G}ithub        : https://github.com/billal1412
  {S}tatus        : ON
  {K}ode Keamanan : x = kali
                  : + = tambah
                  : - = kurang
                  : / = bagi""")
	def settings(self):
		try:
			print ("\n Nomor HP Target ")
			self.no=int(input("  root@smsgratis/nomor#> "))
		except ValueError:
			print ("  Warning(ERROR): isi dengan nomor HP")
			sys.exit()
		print ("\n Pesan ")
		pesan=str(input("   root@smsgratis/pesan#> "))
		r=self.br.open(self.u)
		b=bs(r,"html.parser")
		for f in b.findAll("span"):
			print ("\n Kode Keamanan "+str(f).replace("['","").replace("']","").replace("<span>","").replace("</span>",""))
		jawab=input("   root@smsgratis/jawaban#> ")
		msg="%s | BL4CK DR460N"%(pesan)
		self.br.select_form(nr=0)
		self.br.form["nohp"]=str(self.no)
		self.br.form["pesan"]=msg
		self.br.form["captcha"]=jawab
		submit=self.br.submit().read()
		if 'SMS Berhasil Dikirim' in str(submit) or "SMS Gratis Telah Dikirim" in str(submit):
			print ("  Warning(INFO): SMS berhasil di kirim")
			sys.exit()
		elif "Maaf Layanan ini Tidak Dapat Mengirim SMS Premium" in str(submit):
			print ("  Warning(INFO): SMS Tidak Terkirim")
			sys.exit()
os.system("clear")
sms()
