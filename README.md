# Flask Project Readme

This project is a Flask web application designed to upload audios files to server and store it. It uses the Flask framework and pymongo drvier for connecting to MongoDB. 

## Installation

To install the required libraries for this project, run the following command in your terminal:

```pip install -r requirements.txt```

To run the project you need to have MongoDB installed and running on your machine. You can download it from [here](https://www.mongodb.com/try/download/community) or if you have Docker installed, you can run the following command:

```docker-compose up -d```

This will start a MongoDB instance on your machine. The default port is `27017`. You can change these values in the `docker-compose.yml` file.


## Configuration

Before running the application, you need to set the environment variables. Copy the `example.env` file to `.env` and modify the values according to your needs.


## Running the Application

To run the application, navigate to the project directory and run the following command:

```python3 app.py```


By default, the application will be available at `http://localhost:2000`.

## API Documentation

Use the http://localhost:2000/upload endpoint to upload the audio file.


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write code and tests for your feature or bug fix.
4. Submit a pull request with a clear description of your changes.
