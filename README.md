# Concurrent Echo Server with Python 

## Overview of Application

This application combines concepts from concurrency and socket programming to create a concurrent echo server in Python. The server is capable of handling multiple client connections simultaneously, echoing back any messages it receives from the clients.

## Tools and Technology Used
- Programming Language: Python
- Python Libraries which include: socket and threading
- Version Control: Git 
- Program testing: CMD (Any command based terminal) 

## Required knowledge
- Basic knowledge of Python programming
- Understanding of TCP servers, threading, etc to develop a fully working server and clients
- Git installed and configured for version control

## Getting Started

1. Clone the repository using the command in cmd
```bash
git clone https://github.com/KabeerH/BTP405-Activity5
```
2. Change to the directory where you have cloned the project
```bash
cd directory
```
3. Start the server.py file
```bash 
python server.py
```
4. Connect client.py with the server on another command based terminal (for each client)
```bash 
python client.py
```
5. To disconnect the client from the server
```bash
message: 'quit' or force keyboard 'C'
```

Once the application is started, you can send messages to the server from one or multiple clients

## Contributors 

- Kabeer Harjani | https://github.com/KabeerH
