# Datastore
Socket based key value data store, just like Redis, but not quite there yet. 

## Installation
```
docker build -t datastore:latest -f Dockerfile .
docker run -it -d --name datastore -p 8080:8080 datastore:latest
```

### To start client
```
python3 client.py
```

## Sample output

### Server
```
[I 230331 23:26:51 main:6] Starting server
[W 230331 23:26:51 server:62] Listening on 127.0.0.1:65432
[W 230331 23:27:17 server:17] Accepted connection from 127.0.0.1:38958
[D 230331 23:28:27 controller:25] Key not found: 'A'
[D 230331 23:28:32 controller:25] Key not found: 2
[D 230331 23:29:06 controller:42] Seting 1 -> APPLE
```

### Client
```
SET 1 APPLE
None
GET 1
APPLE
```
