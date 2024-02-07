from sql_connection_dao import get_all_connection

def get_all_unit():
   cursor = connection.cursor()
   query = ("select * from grocery_store. unit_table")
   cursor.execute(query)
   response=[]
   for (unit_id,unit_name)in cursor:
      response.append({
     'unit_id': unit_id,
     'unit_name': unit_name
   }
    )
   return response


if __name__ =='__main__':
    connection = get_all_connection()


