CREATE TABLE IF NOT EXISTS user_metrics (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    session_id VARCHAR(255) NOT NULL,
    device_id VARCHAR(255),
    talked_time FLOAT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment FLOAT,
    timestamp TIMESTAMP NOT NULL
);
