import uvicorn
from fastapi import FastAPI
from UserMetrics import UserMetrics
import psycopg2

app = FastAPI()

connector = psycopg2.connect(database="KrispTask", user = "postgres",
                             password = "postgres", host = "localhost", port = "5432")
cursor = connector.cursor()



@app.post("/metrics/")
async def create_metrics(metric: UserMetrics):
    db_metric = tuple(metric.model_dump().values())
    #columns = tuple(metric.model_dump().keys())
    cursor.execute(f'''INSERT INTO user_metrics 
                   (user_id, session_id, device_id, talked_time, microphone_used, speaker_used, voice_sentiment, timestamp)
                     VALUES {db_metric}''')
    connector.commit()


if __name__ == '__main__':
    uvicorn.run(app)
    cursor.close()
    connector.close()
