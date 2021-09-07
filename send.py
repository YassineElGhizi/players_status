import requests
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="player_status"
)
mycursor = mydb.cursor(buffered=True)
adel_json_api_page = 2

mycursor.execute("SELECT movie_id, player_url FROM players where adel_json_api_page =" + str(adel_json_api_page))

myresult = mycursor.fetchall()

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

cnt  = 0
for x in myresult:
    r = requests.post('https://panelv3.dustreaming.com/api/v2/links/movies/',
                      data={'id': x[0] , 'link' : x[1]} , headers=headers)
    cnt += 1
    print("posting: id:" + str(x[0])+" link: " + str(x[1]))
    if cnt ==2:
        print("response: " + str(r.status_code))
        quit()
