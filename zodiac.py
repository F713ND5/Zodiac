import os,sys,time
import requests,json
url = "https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w"

#Warna
m = "\033[1;91m"
h = "\033[1;92m"
k = "\033[1;93m"
b = "\033[1;96m"
p = "\033[1;97m"
t = "\033[0m"

def main():
	os.system('clear')
	print(t+"--==[ "+b+"ZODIAC"+t+" ]==--"+t).center(60)
	print(t+"Source : "+h+"https://github.com/rezadkim"+t)
	print(t+"Readme : Gunakan format birthday ("+h+"dd"+t+"-"+b+"mm"+t+"-"+k+"yyyy"+t+")"+t)
	print(t+"         "+h+"D=Day "+t+"- "+b+"M=Month "+t+"- "+k+"Y=Year"+t)
	print(t+"Copyright : RezaTamvan (c) 2020.\n            All rights reserved."+t)
	print(h+45*"-")
	try:
		name = raw_input(t+"["+h+"+"+t+"] Input your full name : "+h)
		if name =="":
			print(t+"["+m+"!"+t+"] Isi goblog, jangan kosong kek otak lo")
			time.sleep(2)
			main()
		else:
			birth = raw_input(t+"["+h+"+"+t+"] Birthday : "+h)
			if birth =="":
				exit(t+"["+m+"!"+t+"] Isi goblog, jangan kosong kek otak lo")
			else:
				r = requests.get(url+"&nama="+name+"&tanggal="+birth)
				o = json.loads(r.text)
				if "error" in o['status']:
					exit(t+"["+m+"!"+t+"] Data Error")
				else:
					print(h+45*"-")
					print(t+"["+h+"="+t+"] Result> ")
					print(t+"["+h+"+"+t+"] Name : "+b+o['data']['nama'])
					print(t+"["+h+"+"+t+"] Lahir : "+b+o['data']['lahir'])
					print(t+"["+h+"+"+t+"] Usia : "+b+o['data']['usia'])
					print(t+"["+h+"+"+t+"] Birthday : "+b+o['data']['ultah'])
					print(t+"["+h+"+"+t+"] Zodiac : "+b+o['data']['zodiak'])
					raw_input(t+"\n["+m+"xx"+t+"] Enter [Exit] ")
	except:
		exit(t+"["+m+"!"+t+"] Data Error")
	
	
main()