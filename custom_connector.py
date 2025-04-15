from fastapi import FastAPI,Request
import psycopg2

app = FastAPI()
def db_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",  
            user="postgres",        
            password="1234",    
            host="localhost",            
            port="5433")
    except psycopg2.Error as e:
        print(e)
    return conn

@app.post("/submit")
async def submit(request:Request):
    data = await request.json()
    name = data.get("name")
    policy_type = data.get("policy_type")
    amount = data.get("amount")
    con = db_connection()
    cursor = con.cursor()
    cursor.execute("insert into policies(name,policy_type,amount) values (%s,%s,%s)",(name,policy_type,amount))
    con.commit()
    con.close()
    return {"status":"Success"}


