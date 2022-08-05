import json
import mysql.connector

""" Country Class

Initialize Country variables
Insert Country data
"""
class Country:

     def __init__(self,country):
        self.country_id = country["id"]
        self.country_name = country["name"]
        self.iso3         = country["iso3"]
        self.iso2        = country["iso2"]
        self.numeric_code = country["numeric_code"]
        self.phone_code  = country["phone_code"]
        self.capital = country["capital"]
        self.currency = country["currency"]
        self.currency_name = country["currency_name"]
        self.currency_symbol = country["currency_symbol"]
        self.tld = country["tld"]
        self.native = country["native"]
        self.region = country["region"]
        self.sub_region = country["subregion"]
        self.latitude = country["latitude"]
        self.longitude = country["longitude"]
        self.emoji = country["emoji"]
        self.emojiU = country["emojiU"]

     def insert_country(self):
         try:
             sql = """INSERT INTO countrystatedb_country (country_id,name,iso3,iso2,numeric_code,phone_code,
                               capital,currency,currency_name,currency_symbol,tld,native,
                               region,sub_region,latitude,longitude,emoji,emojiU)
                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

             val = (self.country_id,self.country_name,self.iso3,self.iso2,self.numeric_code,
                   self.phone_code,self.capital,self.currency,self.currency_name,
                   self.currency_symbol,self.tld,self.native,self.region,self.sub_region,
                   self.latitude,self.longitude,self.emoji,self.emojiU)

             cursor.execute(sql, val)
         except Exception as e:
             print(self.country_id)

""" TimeZones Class

Initialize TimeZones variables
Insert TimeZones data
"""
class TimeZones:

    def __init__(self, timezone_dict, country_id):
        self.zone_name = timezone_dict["zoneName"]
        self.gmt_offset = timezone_dict["gmtOffset"]
        self.gmt_offset_name = timezone_dict["gmtOffsetName"]
        self.abbreviation = timezone_dict["abbreviation"]
        self.tz_name = timezone_dict["tzName"]
        self.country_id = country_id

    def insert_time_zone(self):
        try:
            sql = """INSERT INTO countrystatedb_timezones (gmt_offset,gmt_offset_name,abreviation,tz_name,
                                       country_id,zone_name)
                                       VALUES (%s,%s,%s,%s,%s,%s)"""

            val = (self.gmt_offset, self.gmt_offset_name, self.abbreviation, self.tz_name,
                   self.country_id, self.zone_name)
            cursor.execute(sql, val)
        except Exception as e:
            print(self.country_id)

""" Translations Class

Initialize Translations variables
Insert Translations data
"""
class Translations:

    def __init__(self, translations_dict, country_id):
        self.kr = translations_dict.get("kr")
        self.br = translations_dict.get("br")
        self.pt = translations_dict.get("pt")
        self.nl = translations_dict.get("nl")
        self.hr = translations_dict.get("hr")
        self.fa = translations_dict.get("fa")
        self.de = translations_dict.get("de")
        self.es = translations_dict.get("es")
        self.fr = translations_dict.get("fr")
        self.ja = translations_dict.get("ja")
        self.it = translations_dict.get("it")
        self.cn = translations_dict.get("cn")
        self.tr = translations_dict.get("tr")
        self.country_id = country_id

    def insert_translations(self):
        try:
            sql = """INSERT INTO countrystatedb_translations(kr,br,pt,nl,hr,fa,de,es,fr,ja,it,cn,tr,country_id)
                                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            val = (self.kr, self.br, self.pt,self.nl, self.hr, self.fa, self.de, self.es,
                   self.fr, self.ja, self.it, self.cn, self.tr, self.country_id)

            cursor.execute(sql, val)

        except Exception as e:
            print(self.country_id)

""" State Class

Initialize State variables
Insert State data
"""
class State:
    def __init__(self, state_dict, country_id):
        self.state_id = state_dict["id"]
        self.state_name = state_dict["name"]
        self.state_code = state_dict["state_code"]
        self.state_latitude = state_dict["latitude"]
        self.state_longitude = state_dict["longitude"]
        self.state_type = state_dict["type"]
        self.country_id = country_id

    def insert_state(self):
        try:
            sql = """INSERT INTO countrystatedb_state (state_id,name,state_code,latitude,longitude,type,country_id)
                                                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            val = (self.state_id, self.state_name, self.state_code, self.state_latitude,
                   self.state_longitude, self.state_type, self.country_id)
            cursor.execute(sql, val)

        except Exception as e:
            print(self.country_id, self.state_id)

""" City Class

Initialize City variables
Insert City data
"""
class City:

    def __init__(self, city_dict, country_id, state_id):
        self.city_id = city_dict["id"]
        self.city_name = city_dict["name"]
        self.city_latitude = city_dict["latitude"]
        self.city_longitude = city_dict["longitude"]
        self.country_id = country_id
        self.state_id = state_id

    def insert_city(self):
        try:
            sql = """INSERT INTO countrystatedb_city (city_id,name,state_id,country_id,latitude,longitude)
                              VALUES (%s,%s,%s,%s,%s,%s)"""
            val = (self.city_id, self.city_name, self.state_id, self.country_id,
                   self.city_latitude, self.city_longitude)
            cursor.execute(sql, val)

        except Exception as e:
            print(self.country_id, self.state_id,self.city_id)

# Script Begins

# Reads the JSON file and Connects to MYSQL database
data = open("countries_states_cities.json",encoding="utf8").read()
json_data = json.loads(data)

# Connect Database
mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="123456",
  database="countrydb",
  auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

"""Read JSON file and insert data into MYSQL

This part o the code loops through the dictionary and divides them into country,
state and city. The classes are instantiated with the read data and data is inserted
into the respective MYSQL table.
"""
for country_dict in json_data:

# Insert Country data
    obj_country = Country(country_dict)
    obj_country.insert_country()
    
    country_id = country_dict["id"]

# Loop through the timezones for the country and Insert Timezone data
    for timezone_dict in country_dict["timezones"]:
        obj_timezone = TimeZones(timezone_dict, country_id)
        obj_timezone.insert_time_zone()

# Get Translations for the country and insert the data
    obj_translations = Translations(country_dict["translations"],country_id)
    obj_translations.insert_translations()

# Loop through the states inside the country and save the state data
    for state_dict in country_dict["states"]:
        state_id = state_dict["id"]
        obj_state = State(state_dict, country_id)
        obj_state.insert_state()

# Loop through the cities inside the state and save te city data
        for city_dict in state_dict["cities"]:
            obj_city = City(city_dict, country_id, state_id)
            obj_city.insert_city()

mydb.commit()
mydb.close()
