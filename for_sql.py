from my_parser import crypto_parser, currency_parser
from config import *
import psycopg2


def insert_info():
    try:
        conn = psycopg2.connect(
            host=hostname,
            password=password,
            port=port_id,
            user=username,
            dbname=db)
        data_currency = currency_parser(cb_url)
        data_crypto = crypto_parser(crypto_url)
        print(data_crypto)
        with conn.cursor() as cur:
            for currency in data_currency:
                query = f'''INSERT INTO currency(num_code, word_code, units, cur_name, rub_cost) 
                VALUES({currency[0]}, '{currency[1]}', {currency[2]}, '{currency[3]}', {currency[4]})'''
                cur.execute(query)
            for crypto in data_crypto:
                query = f'''INSERT INTO crypto(word_code, cru_name, dol_cost) 
                VALUES('{crypto[0]}', '{crypto[1]}', {crypto[2]})'''
                cur.execute(query)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
