The database consists of three tables users, devices and user_metrics. The table users stores information about the users
(id, name, age). The table devices has columns id, type and name. These tables are important to have consistent information for
user_metrics tablewhere the insertions from the endpoint will be made. The user_metrics columns are id, user_id, device_id,
talked_time showing how long in seconds the recording is, microphone used and speaker_used boolean fields showing whether 
speaker or microphone were used. The column voice_sentiment is a float numerically showing the sentiment of the user. The
column time_recorded is a timestamp showing when the recording was made. 

The project is designed to ingest a stream of user metrics—such as talked_time, microphone_used,
 speaker_used, and voice_sentiment—into a PostgreSQL database. The solution ensures efficient ingestion and storage,
 with the ability to handle high data volumes while maintaining performance and data integrity.


Two Docker containers are used:

Application Container: Runs the FastAPI application to process and ingest metrics.
Database Container: Hosts the PostgreSQL instance to store the ingested metrics.


The project structure is as follows:

Part1
|
|-- db 
|   |-- init.sql
|   |-- synthetic_data.sql
|-- app
|   |-- UserMetrics.py
|   |-- endpoint.py
|   |-- Dockerfile
|   |-- docker-compose.yaml
|   |-- requirements.txt
|
|-- README.txt


Dockerfile: Defines the environment and dependencies for the application container.
docker-compose.yaml: Manages the orchestration of the application and database containers.
init.sql: SQL script to initialize the PostgreSQL database with necessary tables and indices.
synthetic_data.sql: SQL script to insert synthetic data into the database
UserMetrics.py: Python file where a class UserMetrics is defined for the endpoint function
endpoint.py: Pyhton file containing the web service
requirements.txt: Text file with dependencies for docker


The database schema written in init.sql is as follows:
    Tables:
	users (
	    id: identification for the user,
	    name: full name of the user,
	    age: age of the user
	    )
	devices (
	    id: identification for the device,
	    type: the type of the device(windows desktop, android phone, etc.)
	    name: the model of the device(Iphone 13, Samsung Galaxy A50, etc.)
	    )
	user_metrics(
	    id: Primary key,
	    user_id: identifier for the user (foreign key),
	    device_id: identifier for the device (foreign key),
	    talked_time: float showing the how long the recording is in seconds,
	    microphone_used: boolean value showing if microphone was used,
	    speaker_used: boolean value showing if speaker was used,
	    voice_sentiment: float value showing the sentiment of the user,
	    time_recorded: timestamp showing when the recording was made
	    )

Docker setup:
    1) Download the repository from https://github.com/davitkhalatyan/KrispTask.
    2) Open Docker Desktop.
    3) Open the terminal with the button at the bottom right.
    4) Change the directory to app using cd <your_directory>/KrispTask/Part1/app
    5) Create the containers writing in the terminal: docker-compose up -d 
    6) Once the containers start running change directory to db with cd ../db
    7) Copy the directory into the container's working directory using docker cp . <db_container_id>:/
    8) Initialize the tables in db by docker exec -it <db_container_id> psql -U postgres -d KrispTask -f /init.sql
    9) Insert data using the same command as in step 8 but use synthetic_data.sql instead of init.sql
    10) Click on the link of the app container to open the endpoint.

The system expects specific format of inputs from the users which can be improved by adding more options to the users
and parsing the input data. The current solution is only registering user recordings but can be enlarged to register more
users and more devices.
Logging can be implemented for better observability for future improvements.

