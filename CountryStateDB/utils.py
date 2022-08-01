import mysql.connector

"""Connect to MYSQL and get data
   
This function connects to mySQL database and executes SQL queries as per
the "action" paramater.
"""
def connect_db(id, action):
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Simjay3#",
          database="countrydb",
          auth_plugin='mysql_native_password'
        )
        mydb.set_character_set_name("utf8")
        cursor = mydb.cursor(dictionary=True)
        results ={}
        if action == "states":
            sql = """Select state_id, name, state_code, latitude, longitude, type, country_id 
                  from countrystatedb_state where country_id = '%s' order by name""" % (id)

            cursor.execute(sql)
            results = cursor.fetchall()

        elif action == "cities":
            sql = """Select city_id, name, latitude, longitude, country_id, state_id 
                         from countrystatedb_city where state_id = '%s' order by name """ % (id)

            cursor.execute(sql)
            results = cursor.fetchall()

        elif action == "country_details":
            results_tz = {}
            results_trans = {}
            sql_country = """SELECT * FROM countrystatedb_country where country_id = '%s'""" % (id)
            sql_tz = """SELECT * FROM countrystatedb_timezones where country_id = '%s'""" % (id)
            sql_trans = """SELECT * FROM countrystatedb_translations where country_id = '%s'""" % (id)

            cursor.execute(sql_country)
            results = cursor.fetchall()

            cursor.execute(sql_tz)
            results_tz = cursor.fetchall()
            results_tz[0].pop("country_id")
            results[0]["timezones"] = results_tz

            cursor.execute(sql_trans)
            results_trans = cursor.fetchall()
            results_trans[0].pop("country_id")
            results[0]["translations"] = results_trans

        elif action == "state_details":
            sql = """SELECT s.*,c.name as country_name,c.iso2 as country_code 
                    FROM countrydb.countrystatedb_state s
                    JOIN countrydb.countrystatedb_country c on
                    s.country_id = c.country_id where state_id= '%s'""" % (id)

            cursor.execute(sql)
            results = cursor.fetchall()

        elif action == "city_details":
            sql = """SELECT c.*, co.name as country_name,co.iso2 as country_code,
                     s.name as state_name, s.state_code FROM 
                     countrydb.countrystatedb_city c
                     JOIN countrydb.countrystatedb_country co
                     JOIN countrydb.countrystatedb_state s
                     ON c.country_id = co.country_id
                     AND c.country_id = s.country_id
                     AND c.state_id = s.state_id
                     WHERE c.city_id = '%s'""" % (id)

            cursor.execute(sql)
            results = cursor.fetchall()

        return results
    except Exception as e:
        prrint(e)
    finally:
        cursor.close()
        mydb.close()
