# Tasks for lab 2

## 1 Task

The main focus of the mandatory assignment is to build and test a multi-threaded server. You will
implement:

- a **server** that can simultaneously handle multiple clients.
- a **client** that will connect to the server.

### 1.1 Server

A server should keep track of the total number of clients, allow clients to send messages and broadcast
everyone. Below are some key functions you must implement:

- You should implement a function named **broadcast** to notify everyone when a client joins (except
  the client who joined).
- You should also implement a function called **game** where it will allow two clients to play rock,
  paper, scissors game.

### 1.2 Client

A client must:

- connect to the server
- receive broadcast message from a server
- send a message to the server for broadcast
- request to play a game with another client
