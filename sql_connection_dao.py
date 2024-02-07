import mysql.connector

__cnx = None
def get_all_connection():
  global __cnx
  if __cnx is None:
     __cnx = mysql.connector.connect(user='root',password='Swarna@660',database='grocery_store')

  return __cnx