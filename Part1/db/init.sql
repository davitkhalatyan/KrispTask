CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);


CREATE TABLE IF NOT EXISTS devices (
    id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS user_metrics (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    device_id VARCHAR(255),
    talked_time FLOAT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment FLOAT,
    time_recorded TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_device FOREIGN KEY (device_id)
        REFERENCES devices (id)
        ON DELETE SET NULL
);
