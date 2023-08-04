<h1 align="center">PocketDB</h1>

<p align="center">
  Minimal and in-memory datastore for performant data storage and retrieval.
</p>

## Table of Contents

- [Flow Diagram](#flow-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Flow Diagram
![Flow Diagram](https://ik.imagekit.io/5jrct2yttdr/pocketdb_WUIqhwFEB.png?updatedAt=1691185101806)

## Installation

1. Docker
    ```
    docker build -t datastore:latest -f Dockerfile .
    docker run -it -d --name datastore -p 8080:8080 datastore:latest
    ```

2. Local
    ```
    python -m install -r requirements.txt
    ```

**To start client, run** `python client.py`

## Usage
* Client
    ```
    SET 1 APPLE
    None
    GET 1
    APPLE
    ```
* Server
    ```
    [I 230331 23:26:51 main:6] Starting server
    [W 230331 23:26:51 server:62] Listening on 127.0.0.1:65432
    [W 230331 23:27:17 server:17] Accepted connection from 127.0.0.1:38958
    [D 230331 23:28:27 controller:25] Key not found: 'A'
    [D 230331 23:28:32 controller:25] Key not found: 2
    [D 230331 23:29:06 controller:42] Seting 1 -> APPLE
    ```

## License

[The MIT License](https://choosealicense.com/licenses/mit/)
