
### Blizzard: Current Date & Time Application
##### Author: Drew Hearin

#### Instructions
To run, simply clone this repo, while in this directory issue a:
```sh
docker-compose up -d 
```

This will build and launch two containers: **test-app** and **web-app**.

To stop both containers:
```sh
docker stop web-app && docker stop test-app
```


#### Description:


**web-app.py**

The purpose of this application is to return the current date and time in JSON, it was built using the lightweight Flask framework.

Once up and running, the endpoint to view this can be found at:
http://127.0.0.1:5000 or http://localhost:5000

a sample of that page will look something like this:
```json
{"Current DateTime ": "2020-04-06T21:02:32.271297"}
```

To view requests from the web-app point of view, we can tail the logs like so: 
```sh
docker logs -f web-app 
```
```sh
172.19.0.2 - - [06/Apr/2020 20:01:13] "GET / HTTP/1.1" 200 -
172.19.0.2 - - [06/Apr/2020 20:01:13] "GET / HTTP/1.1" 200 -
172.19.0.2 - - [06/Apr/2020 20:01:14] "GET / HTTP/1.1" 200 -
172.19.0.2 - - [06/Apr/2020 20:01:14] "GET / HTTP/1.1" 200 -
172.19.0.2 - - [06/Apr/2020 20:01:14] "GET / HTTP/1.1" 200 -
172.19.0.2 - - [06/Apr/2020 20:01:14] "GET / HTTP/1.1" 200 -
```

**test-app.py**

This is a simple test application that performs GET requests against our web-app container, it uses the python requests library.

It has a built in logger that will write to requests.log. Its currently defaulted at ERROR as to not create too large of a log file at this time.  If you wish to write the requests to that file, simply change the logging level from ERROR to DEBUG.

app-test.py (line 8) 
```py
requests_log.setLevel(logging.ERROR)
```
If we issue a:
```sh
docker logs -f test-app 
```
You will see the Success / Failure / Time to Last Byte currently being requested from our "api" at a rate of 4x per second.

app-test sample output against our endpoint:
```sh
Succesful connection, Time to Last Byte: 0.0033
Succesful connection, Time to Last Byte: 0.003114
Succesful connection, Time to Last Byte: 0.003166
Succesful connection, Time to Last Byte: 0.004014
Succesful connection, Time to Last Byte: 0.00319
Succesful connection, Time to Last Byte: 0.004326
Succesful connection, Time to Last Byte: 0.00314
```

a sample of a unsuccessful request might look like:

```sh
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
404 Client Error: NOT FOUND for url: http://httpbin.org/status/404
```
