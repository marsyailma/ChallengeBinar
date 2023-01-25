import pandas as pd
from collections import Counter
from libs.nlp import preprocess_tweets, preprocess_file
from services import AppServiceProject
from io import BytesIO
from fastapi.responses import StreamingResponse
import io
import sqlite3
 
class CleansingServices(AppServiceProject):
    async def cleansing(self, type, text):
        try:
            if type == "text":
                preprocess = preprocess_tweets(text)
 
                data = {
                "data": preprocess
                }
 
                return self.success_response(data)
            else:
                preprocess = preprocess_file(text)
                #TODO-1 Import SQLite
                #TODO-2 Create New Connection to db
                #TODO-3 Create New Tables w/ columns based on 'preprocess' data
                #TODO-4 Convert df to sql
            
        
                #TASK 1
                conn = sqlite3.connect("data/data.db")
                conn.execute('''create table twitter(tweet varchar(255), HS tinyint, Abusive tinyint, HS_Individual tinyint, HS_Group tinyint, HS_Religion tinyint, HS_Race tinyint, HS_Physical tinyint, HS_Gender tinyint, HS_Other tinyint, HS_Weak tinyint, HS_Moderate tinyint, HS_Strong tinyint  ''')
                preprocess.to_sql('twitter',conn, if_exists='replace', index=False)
                conn.commit()
                conn.close()
                stream = io.StringIO()
                preprocess.to_csv(stream, index = False)
                response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv"
                            )
                response.headers["Content-Disposition"] = "attachment; filename=export.csv"
 
                return response            
        except Exception as e:
            return self.error_response(e)