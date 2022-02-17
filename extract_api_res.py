import requests
import pymysql
import logging
import configparser

config = configparser.ConfigParser()
config.read("./configuration/config.ini")

def get_lat_lon():

    try:
        conn_db = pymysql.connect(host='localhost', port=3306, user=config['DB']['USERNAME'], passwd=config['DB']['PASSWORD'], db='weather', charset='utf8')
        cursor = conn_db.cursor()
    except:
        logging.error("DB Connection Issue")

    sql = "SELECT * FROM location"

    cursor.execute(sql)

    data = cursor.fetchall()

    conn_db.close()
    cursor.close()

    return data

def main():

    api_url = "https://api.openweathermap.org/data/2.5/onecall"

    data = get_lat_lon() # 위도, 경도 데이터

    for i in data:
        api_param = {
            "lat" : i[1],
            "lon" : i[2],
            "appid" : config["API"]["API_KEY"]
        }    

        res = requests.get(api_url, params = api_param)

        return res.json()
        
if __name__ == "__main__":

    main()    
