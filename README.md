# Chat Application

This chat application allows users to register, log in, join specific chat rooms, and communicate with others in real-time. It is built using Flask, Flask-Login, Socket.IO, and MongoDB Atlas.

## Features

- User registration and login
- Real-time messaging in chat rooms
- Multiple chat rooms support

## Setup Instructions

### Prerequisites

- Python 3.x
- Virtual environment tool (venv or virtualenv)
- MongoDB Atlas account

### Steps

1. **Clone the repository and navigate to the project directory**

```bash
   git clone https://github.com/amine-el-amrani/flask-chat-app.git && cd flask-chat-app
```

2. **Create a virtual environment**

```bash
   python3 -m venv venv
```

3. **Activate the virtual environment**

```bash
   source venv/bin/activate
```

4. **Install the required packages**

```bash
   pip install -r requirements.txt
```

5. **Setup MongoDB Atlas**

- Go to MongoDB Atlas and create an account.
- Create a new project and then a new cluster.
- Create a database named ChatDB and a collection named users.
- Click on the "Connect" button and follow the instructions to get your MongoDB URI.

6. **Create a .env file**

Create a .env file in the root directory of the project and add your MongoDB URI:
```bash
   MONGODB_URI=your_mongodb_uri
```

6. **Run the application**

```bash
   python3 app.py
```
Open your web browser and go to http://127.0.0.1:5000

## Usage

- Register a new account.
- Log in with your credentials.
- Enter a chat room by providing a room name.
- Start chatting with others in the same room.

## Technologies Used

- Flask
- Flask-Login
- Flask-SocketIO
- MongoDB Atlas