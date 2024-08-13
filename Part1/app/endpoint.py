import uvicorn
from fastapi import FastAPI
from UserMetrics import UserMetrics
import psycopg2

app = FastAPI()

connector = psycopg2.connect(database="KrispTask", user = "postgres",
                             password = "postgres", host = "db", port = "5432")
cursor = connector.cursor()


@app.post("/metrics/")
async def create_metrics(metric: UserMetrics):
    db_metric = tuple(metric.model_dump().values())
    try:
        cursor.execute(f'''INSERT INTO user_metrics 
                    (user_id, device_id, talked_time, microphone_used, speaker_used, voice_sentiment, time_recorded)
                        VALUES {db_metric}''')
        connector.commit()
        return {'message': 'Data inserted successfully'}
    except psycopg2.errors.InFailedSqlTransaction:
        connector.rollback()
        return {'message': 'Transaction stopped...'}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost')
    #cursor.close()
    #connector.close()
