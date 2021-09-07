import os
from random import randint
import requests
import multiprocessing
import json
import time
import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="player_status"
)
mycursor = mydb.cursor(buffered=True)

adel_json_api_page = 1

#
# sql = "INSERT INTO player (id, player,status) VALUES (%s, %s , %s)"
# val = (1235, "https://www.w3schools.com/python/python_mysql_insert.asp" , 0)
# mycursor.execute(sql, val)
# mydb.commit()




# pro_list = ["102.129.249.120:8080","103.83.118.10:55443","119.81.71.27:8123","128.199.202.122:8080","128.199.214.87:3128","128.199.202.122:3128","139.162.78.109:3128","138.68.60.8:8080","148.251.153.6:1080","159.8.114.34:8123","159.8.114.37:25","159.203.61.169:3128","159.8.114.37:80","159.8.114.37:8123","161.35.70.249:3128","161.202.226.194:80","161.202.226.194:8123","167.71.5.83:3128","169.57.157.146:8123","169.57.157.148:25","169.57.157.148:80","169.57.157.148:8123","176.9.119.170:3128","176.9.75.42:3128","169.57.1.84:80","191.96.42.80:3128","191.96.42.80:8080","209.97.150.167:3128","209.97.150.167:8080","46.4.96.137:3128","46.4.96.137:8080","5.252.161.48:3128","5.252.161.48:8080","88.198.24.108:3128","88.198.24.108:8080","88.198.50.103:3128","88.99.10.251:1080","88.99.10.252:1080","88.99.10.250:1080","88.99.10.253:1080","88.99.10.249:1080","88.99.10.254:1080","88.99.10.248:1080","212.200.246.24:80","102.129.249.120:3128","134.209.29.120:3128","138.68.60.8:3128","139.162.78.109:8080","139.59.1.14:3128","139.59.1.14:8080","161.35.70.249:8080","167.71.5.83:8080","176.9.119.170:8080","176.9.75.42:8080","169.57.1.85:8123","47.91.44.217:8000","88.198.50.103:8080","119.81.71.27:80","119.81.189.194:25","119.81.189.194:80","101.255.72.171:80","31.41.44.219:3128","85.15.152.39:3128","178.205.169.210:3128","103.21.163.70:6666","103.79.74.193:53879","103.81.114.182:53281","109.193.195.5:8080","134.3.255.2:8080","149.172.255.14:8080","149.172.255.8:8080","149.172.255.3:8080","149.172.255.9:8080","217.8.51.200:8080","37.49.127.227:8080","119.84.112.139:80","134.209.29.120:8080","47.75.90.57:80","119.81.189.194:8123","95.172.52.133:3128","103.47.66.154:8080","81.95.226.138:3128","91.195.156.241:3128","95.165.163.188:60103","212.95.180.50:53281","52.41.94.5:80","103.103.212.25:53281","117.131.235.198:8060","119.93.234.41:41731","150.129.151.62:6666","158.58.133.106:41258","187.216.90.46:53281","190.145.200.126:53281","218.58.193.98:8060","221.1.205.74:8060",]

pro_list = ["63.141.241.98:16001", "161.202.226.194:80" ,"161.202.226.194:8123" , "169.57.157.148:8123" , "119.81.71.27:8123" , "159.8.114.34:8123"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166'}

def proxy_changer():
    global pro_list
    PROXY = pro_list[randint(0 , len(pro_list)-1)]
    proxyDict = {"http"  :"http://"+PROXY}
    return proxyDict
    # PROXY = "http://63.141.241.98:16001"
    # proxyDict = {"http"  : PROXY,}
    # return  proxyDict

##########file.py
def upvid(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "deleted 404" in tmp.text:
                print("upvid is down")
                # tmp.close()
                # save_dead_link(id ,link, "upvid")
                db_writer(id,link)
                return False
            else:
                print("upvid is up ")
                # tmp.close()
                # save_up_link(id,link, "upvid")
                # db_writer(id,link,1)
                return True
        except:
            # print("upvid is up ")
            # save_up_link(id, link, "upvid")
            # db_writer(id,link,1)
            return True


def mixdrop(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "WE ARE SORRY" in tmp.text:
                print("mixdrop is down")
                # tmp.close()
                # save_dead_link(id ,link, "mix")
                db_writer(id,link)
                return False
            else:
                print("mixdrop is up")
                # tmp.close()
                # save_up_link(id,link, "mix")
                # db_writer(id,link,1)
                return True
        except:
            # print("mixdrop.get() err : " + str(link))
            # db_writer(id, link)
            return True

def vudeo(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "has been deleted" in tmp.text:
                print("vudeo is down")
                # tmp.close()
                # save_dead_link(id ,link , "vudeo")
                db_writer(id,link)
                return False
            else:
                print("vudeo is up")
                # tmp.close()
                # save_up_link(id ,link , "vudeo")
                # db_writer(id,link,1)
                return True
        except:
#             # print("vudeo.get() err"  + str(link))
            return True

def ninjastream(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "jw-error-msg" in tmp.text:
                print("ninjastream is down")
                # tmp.close()
                # save_dead_link(id ,link, "ninja")
                db_writer(id,link)
                return False
            elif "File not found" in tmp.text:
                print("ninjastream is down")
                # tmp.close()
                # save_dead_link(id ,link, "ninja")
                db_writer(id,link)
                return False
            else:
                print("ninjastream is up")
                # tmp.close()
                # save_up_link(id,link, "ninja")
                # db_writer(id,link,1)
                return True
        except:
#             # print("ninjastream.get() err"  + str(link))
            return True

def vidoza(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "File was deleted" in tmp.text:
                print("vidoza is down ")
                # tmp.close()
                # save_dead_link(id ,link, "vidoza")
                db_writer(id,link)
                return False
            else:
                print("vidoza is up ")
                # tmp.close()
                # save_up_link(id,link, "vidoza")
                # db_writer(id,link,1)
                return True
        except:
            # print("vidoza.get() err"  + str(link))
            return True

def streamtape(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "Sorry, something went wrong!" in tmp.text:
                print("streamtape is down ")
                # tmp.close()
                # save_dead_link(id ,link, "streamtape")
                db_writer(id,link)
                return False
            else:
                print("streamtape is up")
                # tmp.close()
                # save_up_link(id,link, "streamtape")
                # db_writer(id,link,1)
                return True
        except:
            # print("streamtape.get() err"  + str(link))
            return  True

def fembed_aka_dutrag(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if  "video does not exis" in tmp.text:
                print("fembed_aka_dutrag is down ")
                # tmp.close()
                # save_dead_link(id ,link, "fembed_aka_dutrag")
                db_writer(id,link)
                return False
            elif "Sorry this video is unavailable: DMCA Takedown" in tmp.text:
                print("fembed_aka_dutrag is down ")
                # tmp.close()
                # save_dead_link(id ,link, "fembed_aka_dutrag")
                db_writer(id,link)
                return False
            elif "Sorry this video is unavailable: Conversion failed!" in tmp.text:
                print("fembed_aka_dutrag is down ")
                # tmp.close()
                # save_dead_link(id ,link, "fembed_aka_dutrag")
                db_writer(id,link)
                return False
            else:
                print("fembed_aka_dutrag is up")
                # tmp.close()
                # save_up_link(id,link, "fembed_aka_dutrag")
                # db_writer(id,link,1)
                return True
        except:
            print("fembed_aka_dutrag is down ")
            # save_dead_link(id, link, "fembed_aka_dutrag")
            db_writer(id,link)
            return False

def upstream(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "Not Found" in tmp.text:
                print("upstream is down 00")
                # tmp.close()
                # save_dead_link(id ,link, "upstream")
                db_writer(id,link)
                return False
            elif "image-404.png" in tmp.text:
                print("upstream is down 01")
                # tmp.close()
                # save_dead_link(id ,link, "upstream")
                db_writer(id,link)
                return False

            else:
                print("upstream is up")
                # tmp.close()
                # save_up_link(id,link, "upstream")
                # db_writer(id,link,1)
                return True
        except:
#             # print("upstream.get() err" + str(link))
            return True

def jetload(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer() , timeout = (3 , 3))
            if "HLS.js error: networkError" in tmp.text:
                print("jetload is down ")
                # tmp.close()
                # save_dead_link(id ,link, "jetload")
                db_writer(id,link)
                return False
            else:
                print("jetload is up")
                # tmp.close()
                # save_up_link(id,link, "jetload")
                # db_writer(id,link,1)
                return True
        except:
            print("jetload is down ")
            # save_dead_link(id, link, "jetload")
            db_writer(id,link)
            return False

def mystream(link , id):
    try:
        print(link)
        tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
        print("mystream is probably up")
        # tmp.close()
        # save_up_link(id,link, "mystream")
        # db_writer(id,link,1)
        return True
    except:
        print("mystream is dow")
        # save_dead_link(id ,link, "mystream")
        db_writer(id,link)
        return False

def uptostream(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "File not found" in tmp.text:
                print("uptostream is down ")
                # tmp.close()
                # save_dead_link(id ,link, "uptostream")
                db_writer(id,link)
                return False
            elif "The video player could not be loaded" in tmp.text:
                print("uptostream is down ")
                # tmp.close()
                # save_dead_link(id ,link, "uptostream")
                db_writer(id,link)
                return False
            else:
                print("uptostream is up")
                # tmp.close()
                # save_up_link(id,link, "uptostream")
                # db_writer(id,link,1)
                return True
        except Exception as e:
            # print(e)
#             # print("uptostream.get() err" + str(link))
            return True

def ok(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "The video has been blocked" in tmp.text:
                print("ok is down ")
                # tmp.close()
                # save_dead_link(id ,link, "ok")
                db_writer(id,link)
                return False
            elif "Видео заблокировано по требованию правообладателя" in tmp.text:
                print("ok is down ")
                # tmp.close()
                # save_dead_link(id ,link, "ok")
                db_writer(id,link)
                return False
            else:
                print("ok is up")
                # tmp.close()
                # save_up_link(id,link, "ok")
                # db_writer(id,link,1)
                return True
        except:
            print("ok is up")
            # save_up_link(id, link, "ok")
            # db_writer(id,link,1)
            return True

def uqload(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "File was deleted" in tmp.text:
                print("uqload is down ")
                # tmp.close()
                # save_dead_link(id ,link, "uqload")
                db_writer(id,link)
                return False
            else:
                print("uqload is up")
                # tmp.close()
                # save_up_link(id,link, "uqload")
                # db_writer(id,link,1)
                return True
        except:
#             # print("uqload.get() err" + str(link))
            return True

def uploaded(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "Error: 404" in tmp.text:
                print("uploaded is down ")
                # tmp.close()
                # save_dead_link(id ,link, "uploaded")
                db_writer(id,link)
                return False
            else:
                print("uploaded is up")
                # tmp.close()
                # save_up_link(id,link, "uploaded")
                # db_writer(id,link,1)
                return True
        except:
            # print("uploaded.get() err" + str(link))
            return  True

def rapidgator(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "404 File not found" in tmp.text:
                print("rapidgator is down ")
                # tmp.close()
                # save_dead_link(id ,link, "rapidgator")
                db_writer(id,link)
                return False
            else:
                print("rapidgator is up")
                # tmp.close()
                # save_up_link(id,link, "rapidgator")
                # db_writer(id,link,1)
                return True
        except:
            return True
            # print("rapidgator.get() err" + str(link))

def videomega(link , id):
    try:
        print(link)
        tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
        print("videomega is probably up")
        # tmp.close()
        # save_up_link(id,link, "videomega")
        # db_writer(id,link,1)
        return True
    except:
        print("videomega is down")
        # save_dead_link(id ,link, "videomega")
        db_writer(id,link)
        return False

def flashx(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "deleted!" in tmp.text:
                print("flashx is down ")
                # tmp.close()
                # save_dead_link(id ,link, "flashx")
                db_writer(id,link)
                return False
            else:
                print("flashx is up")
                # tmp.close()
                # save_up_link(id,link, "flashx")
                # db_writer(id,link,1)
                return True
        except:
            print("flashx is down ")
            # tmp.close()
            # save_dead_link(id, link, "flashx")
            db_writer(id,link)
            return False

def gounlimited(link ,id):
    while True:
        try:
            print(link)
            print("gounlimited is down ")
            # save_dead_link(id ,link, "gounlimited")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("gounlimited is down ")
            # save_dead_link(id ,link, "gounlimited")
            db_writer(id,link)
            return False

def vidfast(link ,id):
    while True:
        try:
            print(link)
            print("vidfast is down ")
            # save_dead_link(id ,link, "vidfast")
            db_writer(id,link)
            return False
        except:
            return True
            # print("vidfast.get() err" + str(link))

def vidlox(link ,id):
    while True:
        try:
            print(link)
            print("vidlox is down ")
            # save_dead_link(id ,link, "vidlox")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("vidlox is down ")
            # save_dead_link(id, link, "vidlox")
            db_writer(id,link)
            return False

def ffsplayer(link ,id):
    while True:
        try:
            print(link)
            print("ffsplayer is down ")
            # save_dead_link(id ,link, "ffsplayer")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("ffsplayer is down ")
            # save_dead_link(id, link, "ffsplayer")
            db_writer(id,link)
            return False

def cloudvid(link , id):
    while True:
        try:
            print(link)
            print("cloudvid is down ")
            # save_dead_link(id ,link, "cloudvid")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("cloudvid is down ")
            # save_dead_link(id, link, "cloudvid")
            db_writer(id,link)
            return False

def vidtodoo(link , id):
    while True:
        try:
            print(link)
            print("vidtodoo is down ")
            # save_dead_link(id ,link, "vidtodoo")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("vidtodoo is down ")
            # save_dead_link(id, link, "vidtodoo")
            db_writer(id,link)
            return False

def papystreaming(link , id):
    while True:
        try:
            print(link)
            print("papystreaming is down ")
            # save_dead_link(id ,link, "papystreaming")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("papystreaming is down ")
            # save_dead_link(id, link, "papystreaming")
            db_writer(id,link)
            return False

def clipwatching(link , id):
    while True:
        try:
            print(link)
            print("clipwatching is down ")
            # save_dead_link(id ,link, "clipwatching")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("clipwatching is down ")
            # save_dead_link(id, link, "clipwatching")
            db_writer(id,link)
            return False

def vidhd(link , id):
    while True:
        try:
            print(link)
            print("vidhd is down ")
            # save_dead_link(id ,link, "vidhd")
            db_writer(id,link)
            return False
        except:
            print(link)
            print("vidhd is down ")
            # save_dead_link(id, link, "vidhd")
            db_writer(id,link)
            return False


def x(link , id):
    while True:
        try:
            print(link)
            tmp = requests.get(link , 'html.parser' ,headers=headers,proxies=proxy_changer())
            if "404" or "deleted" or "unavaible" or "Error" in tmp.text:
                print("x is down ")
                # tmp.close()
                # save_dead_link(id ,link, "x")
                db_writer(id,link)
                return False
            else:
                print("x is up")
                # tmp.close()
                # save_up_link(id,link, "x")
                # db_writer(id,link,1)
                return True
        except:
            # print("x.get() err" + str(link))
            return True
#====================================================================
# def save_dead_link(id , link , player):
#     with open( "./" + str(player) + "/down/down.txt", 'a') as f:
#         f.write(str(id) +"  " + link + "\n")
#
# def save_up_link(id ,link , player):
#     with open( "./" + str(player) + "/up/up.txt", 'a') as f:
#         f.write(str(id) + "  " + link + "\n")


def check_upvid(l):
    for num ,i in enumerate(l):
        print("upvid :" + str(num))
        upvid(i["link"] , i["id"])
    print("----------->upvid  finished <------------------")


def check_ninja(l):
    for num ,i in enumerate(l):
        print("ninja :" + str(num))
        ninjastream(i["link"] , i["id"])
    print("----------->ninja  finished <------------------")


def check_mixdrop(l):
    for num ,i in enumerate(l):
        print("mixdrop :" + str(num))
        mixdrop(i["link"] , i["id"])
    print("----------->mixdrop finished <------------------")


def check_vudeo(l):
    for num ,i in enumerate(l):
        print("vudeo :" + str(num))
        vudeo(i["link"] , i["id"])
    print("----------->vudeo  finished <------------------")


def check_vidoza(l):
    for num ,i in enumerate(l):
        print("vidoza :" + str(num))
        vidoza(i["link"] , i["id"])
    print("----------->vidoza  finished <------------------")


def check_streamtape(l):
    for num ,i in enumerate(l):
        print("streamtape :" + str(num))
        streamtape(i["link"] , i["id"])
    print("----------->streamtape  finished <------------------")


def check_fembed_aka_dutrag(l):
    for num ,i in enumerate(l):
        print("fembed_aka_dutrag :" + str(num))
        fembed_aka_dutrag(i["link"] , i["id"])
    print("----------->fembed_aka_dutrag  finished <------------------")


def check_upstream(l):
    for num ,i in enumerate(l):
        print("upstream :" + str(num))
        upstream(i["link"] , i["id"])
    print("----------->upstream  finished <------------------")


def check_jetload(l):
    for num ,i in enumerate(l):
        print("jetload :" + str(num))
        jetload(i["link"] , i["id"])
    print("----------->jetload  finished <------------------")


def check_mystream(l):
    for num ,i in enumerate(l):
        print("mystream :" + str(num))
        mystream(i["link"] , i["id"])
    print("----------->mystream  finished <------------------")


def check_uptostream(l):
    for num ,i in enumerate(l):
        print("uptostream :" + str(num))
        uptostream(i["link"] , i["id"])
    print("----------->uptostream  finished <------------------")


def check_ok(l):
    for num ,i in enumerate(l):
        print("ok :" + str(num))
        ok(i["link"] , i["id"])
    print("----------->ok  finished <------------------")


def check_uqload(l):
    for num ,i in enumerate(l):
        print("uqload :" + str(num))
        uqload(i["link"] , i["id"])
    print("----------->uqload finished <------------------")


def check_uploaded(l):
    for num ,i in enumerate(l):
        print("uploaded :" + str(num))
        uploaded(i["link"] , i["id"])
    print("----------->uploaded  finished <------------------")


def check_rapidgator(l):
    for num ,i in enumerate(l):
        print("rapidgator :" + str(num))
        rapidgator(i["link"] , i["id"])
    print("----------->rapidgator  finished <------------------")


def check_videomega(l):
    for num ,i in enumerate(l):
        print("videomega :" + str(num))
        videomega(i["link"] , i["id"])
    print("----------->videomega  finished <------------------")


def check_flashx(l):
    for num ,i in enumerate(l):
        print("flashx :" + str(num))
        flashx(i["link"] , i["id"])
    print("----------->flashx  finished <------------------")

def check_gounlimited(l):
    for num ,i in enumerate(l):
        print("gounlimited :" + str(num))
        gounlimited(i["link"] , i["id"])
    print("----------->gounlimited  finished <------------------")

def check_vidfast(l):
    for num ,i in enumerate(l):
        print("vidfast :" + str(num))
        vidfast(i["link"] , i["id"])
    print("----------->vidfast  finished <------------------")

def check_vidlox(l):
    for num ,i in enumerate(l):
        print("vidlox :" + str(num))
        vidlox(i["link"] , i["id"])
    print("----------->vidlox  finished <------------------")

def check_ffsplayer(l):
    for num ,i in enumerate(l):
        print("ffsplayer :" + str(num))
        ffsplayer(i["link"] , i["id"])
    print("----------->ffsplayer  finished <------------------")

def check_cloudvid(l):
    for num ,i in enumerate(l):
        print("cloudvid :" + str(num))
        cloudvid(i["link"] , i["id"])
    print("----------->cloudvid  finished <------------------")

def check_vidtodoo(l):
    for num ,i in enumerate(l):
        print("vidtodoo :" + str(num))
        vidtodoo(i["link"] , i["id"])
    print("----------->vidtodoo  finished <------------------")

def check_papystreaming(l):
    for num ,i in enumerate(l):
        print("papystreaming :" + str(num))
        papystreaming(i["link"] , i["id"])
    print("----------->papystreaming  finished <------------------")

def check_clipwatching(l):
    for num ,i in enumerate(l):
        print("clipwatching :" + str(num))
        clipwatching(i["link"] , i["id"])
    print("----------->clipwatching  finished <------------------")

def check_vidhd(l):
    for num ,i in enumerate(l):
        print("vidhd :" + str(num))
        vidhd(i["link"] , i["id"])
    print("----------->vidhd  finished <------------------")


def check_x(l):
    for num ,i in enumerate(l):
        print("x :" + str(num))
        videomega(i["link"] , i["id"])
    print("----------->x  finished <------------------")


# def init():
#     if not os.path.isdir("./clipwatching"):
#         os.mkdir("./clipwatching")
#         os.mkdir("./clipwatching/down")
#         os.mkdir("./clipwatching/up")
#     if not os.path.isdir("./cloudvid"):
#         os.mkdir("./cloudvid")
#         os.mkdir("./cloudvid/down")
#         os.mkdir("./cloudvid/up")
#     if not os.path.isdir("./fembed_aka_dutrag"):
#         os.mkdir("./fembed_aka_dutrag")
#         os.mkdir("./fembed_aka_dutrag/down")
#         os.mkdir("./fembed_aka_dutrag/up")
#     if not os.path.isdir("./ffsplayer"):
#         os.mkdir("./ffsplayer")
#         os.mkdir("./ffsplayer/down")
#         os.mkdir("./ffsplayer/up")
#     if not os.path.isdir("./flashx"):
#         os.mkdir("./flashx")
#         os.mkdir("./flashx/down")
#         os.mkdir("./flashx/up")
#     if not os.path.isdir("./gounlimited"):
#         os.mkdir("./gounlimited")
#         os.mkdir("./gounlimited/down")
#         os.mkdir("./gounlimited/up")
#     if not os.path.isdir("./jetload"):
#         os.mkdir("./jetload")
#         os.mkdir("./jetload/down")
#         os.mkdir("./jetload/up")
#     if not os.path.isdir("./mix"):
#         os.mkdir("./mix")
#         os.mkdir("./mix/down")
#         os.mkdir("./mix/up")
#     if not os.path.isdir("./mystream"):
#         os.mkdir("./mystream")
#         os.mkdir("./mystream/down")
#         os.mkdir("./mystream/up")
#     if not os.path.isdir("./ninja"):
#         os.mkdir("./ninja")
#         os.mkdir("./ninja/down")
#         os.mkdir("./ninja/up")
#     if not os.path.isdir("./ok"):
#         os.mkdir("./ok")
#         os.mkdir("./ok/down")
#         os.mkdir("./ok/up")
#     if not os.path.isdir("./papystreaming"):
#         os.mkdir("./papystreaming")
#         os.mkdir("./papystreaming/down")
#         os.mkdir("./papystreaming/up")
#     if not os.path.isdir("./rapidgator"):
#         os.mkdir("./rapidgator")
#         os.mkdir("./rapidgator/down")
#         os.mkdir("./rapidgator/up")
#     if not os.path.isdir("./streamtape"):
#         os.mkdir("./streamtape")
#         os.mkdir("./streamtape/down")
#         os.mkdir("./streamtape/up")
#     if not os.path.isdir("./uploaded"):
#         os.mkdir("./uploaded")
#         os.mkdir("./uploaded/down")
#         os.mkdir("./uploaded/up")
#     if not os.path.isdir("./upstream"):
#         os.mkdir("./upstream")
#         os.mkdir("./upstream/down")
#         os.mkdir("./upstream/up")
#     if not os.path.isdir("./uptostream"):
#         os.mkdir("./uptostream")
#         os.mkdir("./uptostream/down")
#         os.mkdir("./uptostream/up")
#     if not os.path.isdir("./upvid"):
#         os.mkdir("./upvid")
#         os.mkdir("./upvid/down")
#         os.mkdir("./upvid/up")
#     if not os.path.isdir("./uqload"):
#         os.mkdir("./uqload")
#         os.mkdir("./uqload/down")
#         os.mkdir("./uqload/up")
#     if not os.path.isdir("./videomega"):
#         os.mkdir("./videomega")
#         os.mkdir("./videomega/down")
#         os.mkdir("./videomega/up")
#     if not os.path.isdir("./vidhd"):
#         os.mkdir("./vidhd")
#         os.mkdir("./vidhd/down")
#         os.mkdir("./vidhd/up")
#     if not os.path.isdir("./vidfast"):
#         os.mkdir("./vidfast")
#         os.mkdir("./vidfast/down")
#         os.mkdir("./vidfast/up")
#     if not os.path.isdir("./vidlox"):
#         os.mkdir("./vidlox")
#         os.mkdir("./vidlox/down")
#         os.mkdir("./vidlox/up")
#     if not os.path.isdir("./vidoza"):
#         os.mkdir("./vidoza")
#         os.mkdir("./vidoza/down")
#         os.mkdir("./vidoza/up")
#     if not os.path.isdir("./vidtodoo"):
#         os.mkdir("./vidtodoo")
#         os.mkdir("./vidtodoo/down")
#         os.mkdir("./vidtodoo/up")
#     if not os.path.isdir("./vudeo"):
#         os.mkdir("./vudeo")
#         os.mkdir("./vudeo/down")
#         os.mkdir("./vudeo/up")
#     if not os.path.isdir("./x"):
#         os.mkdir("./x")
#         os.mkdir("./x/down")
#         os.mkdir("./x/up")


###$######Fin file.py

def db_writer(movie_id , player_url):
    global adel_json_api_page
    mycursor = mydb.cursor(buffered=True)
    sql = "INSERT INTO players (movie_id, player_url ,adel_json_api_page) VALUES (%s, %s ,%s)"
    val = (movie_id , player_url , adel_json_api_page)
    mycursor.execute(sql, val)
    mydb.commit()

if __name__ == "__main__":

    start_time = time.time()
    # init()
    if adel_json_api_page == 1:
        json_url = 'https://panelv2.dustreaming.com/api/v2/movies'
    else:
        json_url = 'https://panelv2.dustreaming.com/api/v2/movies?page=' + str(adel_json_api_page)

    req = requests.get(json_url, 'html.parser' , headers=headers,proxies=proxy_changer())

    my_json = json.loads(req.text)

    jetload_list = []
    upvid_list = []
    mixdrop_list = []
    vudeo_list = []
    vidoza_list = []
    ninja_list = []
    fembed_list = []
    streamtape_list = []
    upstream_list = []
    mystream_list = []
    uptostream_list = []
    uqload_list = []
    ok_list = []
    uploaded_list = []
    rapidgator_list = []
    videomega_list = []
    flashx_list = []
    gounlimited_list = []
    vidfast_list = []
    vidlox_list = []
    ffsplayer_list = []
    cloudvid_list = []
    vidtodoo_list = []
    papystreaming_list = []
    clipwatching_list = []
    vidhd_list = []

    x_list = []

    cnt = 0
    ##A
    big_list = []
    for i in my_json["data"]:
        if i["links_json"] is None:
            with open("./abnormality.txt", 'a') as f:
                f.write(str(i["id"]) +"   " +str(i["imdb_id"])+ "\n")
                f.close()
        else:
            for li in i["links_json"]:
                if type(li) == dict and li["link"] != "":
                    big_list.append(
                        {
                            "id": i["id"],
                            "link": li["link"]
                        }
                    )



    ##FinA
    # for i in my_json["data"]:
    #     for li in i["links_json"]:
    for x in big_list:
        cnt += 1
        # if type(li) == dict:
        if "jetload" in x["link"]:
            jetload_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "upvid" in x["link"]:
            upvid_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "mixdrop" in x["link"]:
            mixdrop_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "ninja" in x["link"]:
            ninja_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "vudeo" in x["link"]:
            vudeo_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "vidoza" in x["link"]:
            vidoza_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "fembed" or "femax20" in x["link"]:
            fembed_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "streamtape" in x["link"]:
            streamtape_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "upstream" in x["link"]:
            upstream_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "mystream" in x["link"]:
            mystream_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "uptostream" in x["link"]:
            uptostream_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "ok.ru" in x["link"]:
            ok_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "uqload" in x["link"]:
            uqload_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "uploaded" in x["link"]:
            uploaded_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "rapidgator" in x["link"]:
            rapidgator_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "flashx" in x["link"]:
            flashx_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )
        elif "gounlimited" in x["link"]:
            gounlimited_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "videomega" in x["link"]:
            videomega_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "vidfast" in x["link"]:
            vidfast_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "vidlox" in x["link"]:
            vidlox_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "ffsplayer" in x["link"]:
            ffsplayer_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "cloudvid" in x["link"]:
            cloudvid_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "vidtodoo" in x["link"]:
            vidtodoo_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "papystreaming" in x["link"]:
            papystreaming_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "clipwatching" in x["link"]:
            clipwatching_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        elif "vidhd" in x["link"]:
            vidhd_list.append(
                {
                    "id": x["id"],
                    "link": x["link"]
                }
            )
        else:
            print("New==============>  x:" + x["link"])
            print("his id =" + str(x["id"]))
            x_list.append(
                {
                    "id":x["id"],
                    "link":x["link"]
                }
            )


    print("cnt =" + str(cnt))
    print("jetload :" + str(len(jetload_list)))
    print("upvid :" + str(len(upvid_list)))
    print("mixdrop :" + str(len(mixdrop_list)))
    print("vudeo :" + str(len(vudeo_list)))
    print("vidoza :" + str(len(vidoza_list)))
    print("ninja :" + str(len(ninja_list)))
    print("fembed :" + str(len(fembed_list)))
    print("streamtape :" + str(len(streamtape_list)))
    print("upstream :" + str(len(upstream_list)))
    print("mystream :" + str(len(mystream_list)))
    print("uptostream :" + str(len(uptostream_list)))
    print("ok.ru :" + str(len(ok_list)))
    print("uploaded :" + str(len(uploaded_list)))
    print("uqload :" + str(len(uqload_list)))
    print("rapidgator :" + str(len(rapidgator_list)))
    print("videomega :" + str(len(videomega_list)))
    print("gounlimited :" + str(len(gounlimited_list)))
    print("vidfast :" + str(len(vidfast_list)))
    print("vidlox :" + str(len(vidlox_list)))
    print("flashx :" + str(len(flashx_list)))
    print("ffsplayer :" + str(len(ffsplayer_list)))
    print("vidtodoo :" + str(len(vidtodoo_list)))
    print("cloudvid :" + str(len(cloudvid_list)))
    print("clipwatching :" + str(len(clipwatching_list)))
    print("clipwatching :" + str(len(vidhd_list)))
    print("papystreaming :" + str(len(papystreaming_list)))


    print("others = " + str(cnt - (len(jetload_list)
                                   +len(upvid_list)
                                   +len(mixdrop_list)
                                   +len(vudeo_list)
                                   +len(vidoza_list)
                                   +len(ninja_list)
                                   +len(fembed_list)
                                   +len(streamtape_list)
                                   +len(upstream_list)
                                   +len(mystream_list)
                                   +len(uptostream_list)
                                   +len(uqload_list)
                                   +len(uploaded_list)
                                   +len(rapidgator_list)
                                   +len(videomega_list)
                                   +len(flashx_list)
                                   +len(gounlimited_list)
                                   +len(vidfast_list)
                                   +len(vidlox_list)
                                   +len(ffsplayer_list)
                                   +len(vidtodoo_list)
                                   +len(cloudvid_list)
                                   +len(papystreaming_list)
                                   +len(clipwatching_list)
                                   +len(vidhd_list)
                                   +len(ok_list))))



    print("===================================================")
    t1 = multiprocessing.Process(target=check_upvid, args=(upvid_list,))
    t2 = multiprocessing.Process(target=check_ninja, args=(ninja_list,))
    t3 = multiprocessing.Process(target=check_mixdrop, args=(mixdrop_list,))
    t4 = multiprocessing.Process(target=check_vudeo, args=(vudeo_list,))
    t5 = multiprocessing.Process(target=check_vidoza, args=(vidoza_list,))
    t6 = multiprocessing.Process(target=check_streamtape, args=(streamtape_list,))
    t7 = multiprocessing.Process(target=check_fembed_aka_dutrag, args=(fembed_list,))
    t8 = multiprocessing.Process(target=check_upstream, args=(upstream_list,))
    t9 = multiprocessing.Process(target=check_jetload, args=(jetload_list,))
    t10 = multiprocessing.Process(target=check_mystream, args=(mystream_list,))
    t11 = multiprocessing.Process(target=check_uptostream, args=(uptostream_list,))
    t12 = multiprocessing.Process(target=check_ok, args=(ok_list,))
    t13 = multiprocessing.Process(target=check_uqload, args=(uqload_list,))
    t14 = multiprocessing.Process(target=check_uploaded, args=(uploaded_list,))
    t15 = multiprocessing.Process(target=check_rapidgator, args=(rapidgator_list,))
    t16 = multiprocessing.Process(target=check_videomega, args=(videomega_list,))
    t17 = multiprocessing.Process(target=check_flashx, args=(flashx_list,))
    t18 = multiprocessing.Process(target=check_gounlimited, args=(gounlimited_list,))
    t19 = multiprocessing.Process(target=check_vidfast, args=(vidfast_list,))
    t20 = multiprocessing.Process(target=check_vidlox, args=(vidlox_list,))
    t21 = multiprocessing.Process(target=check_ffsplayer, args=(ffsplayer_list,))
    t22 = multiprocessing.Process(target=check_cloudvid, args=(cloudvid_list,))
    t23 = multiprocessing.Process(target=check_vidtodoo, args=(vidtodoo_list,))
    t24 = multiprocessing.Process(target=check_papystreaming, args=(papystreaming_list,))
    t25 = multiprocessing.Process(target=check_clipwatching, args=(clipwatching_list,))
    t26 = multiprocessing.Process(target=check_vidhd, args=(vidhd_list,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    print("===================================================")


    print("finished in : " + str((time.time() - start_time) / 60) + " min")