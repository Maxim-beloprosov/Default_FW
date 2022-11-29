import allure
import psycopg2 as psycopg2
import pyodbc as pyodbc

from fw.fw_base import FWBase


class SQLBase(FWBase):

    @allure.step('sql_query')
    def sql_query(self, SQL_query, gandiva_lvl='G1'):

        if gandiva_lvl == 'G1':
            SQL_SERVER = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['SQL_SERVER']
        else:
            SQL_SERVER = self.manager.settings.GLOBAL[self.manager.settings.branch]['SQL_SERVER']

        if SQL_SERVER['TypeSQL'] == 'SQL_Server':
            connect_string = 'DRIVER=' + SQL_SERVER['DRIVER'] +\
                             ';SERVER=' + SQL_SERVER['SERVER'] +\
                             ';DATABASE=' + SQL_SERVER['DATABASE'] +\
                             ';UID=' + SQL_SERVER['login'] +\
                             ';PWD=' + SQL_SERVER['password']
            conn = pyodbc.connect(connect_string)
            cur = conn.cursor()
            try:
                conn.commit()
                cur.execute(SQL_query)
                data = cur.fetchall()
                return data
            except psycopg2.Error as err:
                print(f"Connection error: {err}")
            except pyodbc.ProgrammingError as e:
                print(f"ProgrammingError: {e}")
            finally:
                cur.close()
                conn.close()
        if SQL_SERVER['TypeSQL'] == 'PostgreSQL':
            conn = psycopg2.connect(dbname=SQL_SERVER['DATABASE'],
                                    user=SQL_SERVER['login'],
                                    password=SQL_SERVER['password'],
                                    host=SQL_SERVER['SERVER'],
                                    port=SQL_SERVER['PORT'])
            cursor = conn.cursor()
            try:
                conn.commit()
                cursor.execute(SQL_query)
                data = cursor.fetchall()
                return data
            except psycopg2.Error as err:
                print(f"Connection error: {err}")
            except pyodbc.ProgrammingError as e:
                print(f"ProgrammingError: {e}")
            finally:
                cursor.close()
                conn.close()

    @allure.step('SQL_query_INSERT')
    def sql_query_INSERT(self, SQL_query, gandiva_lvl='G1'):

        if gandiva_lvl == 'G1':
            SQL_SERVER = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['SQL_SERVER']
        else:
            SQL_SERVER = self.manager.settings.GLOBAL[self.manager.settings.branch]['SQL_SERVER']

        if SQL_SERVER['TypeSQL'] == 'SQL_Server':
            SQL_query = SQL_query + '; COMMIT'
            connect_string = 'DRIVER=' + SQL_SERVER['DRIVER'] + \
                             ';SERVER=' + SQL_SERVER['SERVER'] + \
                             ';DATABASE=' + SQL_SERVER['DATABASE'] + \
                             ';UID=' + SQL_SERVER['login'] + \
                             ';PWD=' + SQL_SERVER['password']

            conn = pyodbc.connect(connect_string)
            cur = conn.cursor()
            try:
                cur.execute(SQL_query)
            except psycopg2.Error as err:
                print(f"Connection error: {err}")
            except pyodbc.ProgrammingError as e:
                print(f"ProgrammingError: {e}")
            finally:
                cur.close()
                conn.close()
        if SQL_SERVER['TypeSQL'] == 'PostgreSQL':
            conn = psycopg2.connect(dbname=SQL_SERVER['DATABASE'],
                                    user=SQL_SERVER['login'],
                                    password=SQL_SERVER['password'],
                                    host=SQL_SERVER['SERVER'],
                                    port=SQL_SERVER['PORT'])
            cursor = conn.cursor()
            try:
                conn.commit()
                cursor.execute(SQL_query)
            except psycopg2.Error as err:
                print(f"Connection error: {err}")
            except pyodbc.ProgrammingError as e:
                print(f"ProgrammingError: {e}")
            finally:
                cursor.close()
                conn.close()
