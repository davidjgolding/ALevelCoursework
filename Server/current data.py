import urllib.request
from datetime import datetime
import json
import ssl
import mysql.connector
import time


class Database(object):
    @classmethod
    def table_csusers(cls):
        cls.cursor.execute("USE csnea1")
        cls.cursor.execute("SHOW TABLES")
        cls.cursor.execute("select * from current_data")

    def __new__(cls):
        cls.myDB = mysql.connector.connect(host="mysql6.gear.host", port=3306, user="csnea1", passwd="Je501b!k33C~",
                                           db="csnea1")
        cls.cursor = cls.myDB.cursor(buffered=True)
        cls.table_csusers()


Database()
valid =  ['EUR,USD', 'USD,JPY', 'GBP,USD', 'USD,CHF', 'EUR,CHF', 'AUD,USD', 'USD,CAD', 'NZD,USD', 'EUR,GBP', 'EUR,JPY', 'GBP,JPY', 'CHF,JPY', 'GBP,CHF', 'EUR,AUD', 'EUR,CAD', 'AUD,CAD', 'AUD,JPY', 'CAD,JPY', 'NZD,JPY', 'GBP,CAD', 'GBP,NZD', 'GBP,AUD', 'AUD,NZD', 'USD,SEK', 'EUR,SEK', 'EUR,NOK', 'USD,NOK',  'AUD,CHF', 'EUR,NZD', 'USD,ZAR', 'ZAR,JPY', 'USD,TRY', 'EUR,TRY', 'NZD,CHF', 'CAD,CHF', 'NZD,CAD', 'TRY,JPY', 'USD,EUR', 'USD,GBP', 'USD,AUD', 'USD,NZD',  'EUR,ZAR', 'JPY,USD', 'JPY,EUR', 'JPY,GBP', 'JPY,CHF', 'JPY,AUD', 'JPY,CAD', 'JPY,NZD', 'JPY,SEK', 'JPY,NOK',  'JPY,ZAR', 'JPY,TRY',    'GBP,EUR', 'GBP,SEK', 'GBP,NOK',  'GBP,ZAR', 'GBP,TRY',  'CHF,USD', 'CHF,EUR', 'CHF,GBP', 'CHF,AUD', 'CHF,CAD', 'CHF,NZD', 'CHF,SEK', 'CHF,NOK', 'CHF,ZAR', 'CHF,TRY',  'AUD,EUR', 'AUD,GBP', 'AUD,SEK', 'AUD,NOK', 'AUD,ZAR', 'AUD,TRY','CAD,USD', 'CAD,EUR', 'CAD,GBP', 'CAD,AUD', 'CAD,NZD', 'CAD,SEK', 'CAD,NOK', 'CAD,ZAR', 'CAD,TRY',   'NZD,EUR', 'NZD,GBP', 'NZD,AUD', 'NZD,SEK', 'NZD,NOK',  'NZD,ZAR', 'NZD,TRY',   'SEK,USD', 'SEK,EUR', 'SEK,JPY', 'SEK,GBP', 'SEK,CHF', 'SEK,AUD', 'SEK,CAD', 'SEK,NZD', 'SEK,NOK',  'SEK,ZAR', 'SEK,TRY',   'NOK,USD', 'NOK,EUR', 'NOK,JPY', 'NOK,GBP', 'NOK,CHF', 'NOK,AUD', 'NOK,CAD', 'NOK,NZD', 'NOK,SEK', 'NOK,ZAR', 'NOK,TRY',   'ZAR,USD', 'ZAR,EUR', 'ZAR,GBP', 'ZAR,CHF', 'ZAR,AUD', 'ZAR,CAD', 'ZAR,NZD', 'ZAR,SEK', 'ZAR,NOK',  'ZAR,TRY',   'TRY,USD', 'TRY,EUR', 'TRY,GBP', 'TRY,CHF', 'TRY,AUD', 'TRY,CAD', 'TRY,NZD', 'TRY,SEK', 'TRY,NOK', 'TRY,ZAR', 'TRY,CNH']


for a in valid:
    print(a)
    try:
        Database.cursor.execute("ALTER TABLE current_data ADD COLUMN " + str(a[:3]+a[4:]) + " VARCHAR(45);")
        Database.myDB.commit()
    except mysql.connector.errors.ProgrammingError:
        pass
