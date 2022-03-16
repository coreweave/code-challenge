# Elevator Server

The goal of this challenge is to write a basic elevator server. This is meant to be very open ended so you may spend as much/little time as desired. There are no right or wrong design decisions as long as you can justify potential tradeoffs. After getting your elevator server to a decent working MVP, prepare ideas on how to improve it further. You are encouraged to:
* create and organize new files as desired
* write tests if you feel they are beneficial
* use any third party dependencies

The server should have at least one RESTful HTTP endpoint that clients can submit a desired floor number for the elevator to move to. Clients should be able to submit any floor numbers in any time and any order (like elevator buttons) and the server should determine where the elevator should move next. The server should print a log of all elevator activies and decisions or elevator state. For example:

```
elevator started
at floor 1 and moving IDLE
requested floor 4
INFO:     127.0.0.1:37898 - "POST /floor/4 HTTP/1.1" 200 OK
at floor 1 and moving IDLE
going up!
approaching floor 2
at floor 2 and moving UP
approaching floor 3
at floor 3 and moving UP
approaching floor 4
at floor 4 and moving UP
at floor 4 and doors open
at floor 4 and moving IDLE
requested floor 8
INFO:     127.0.0.1:37900 - "POST /floor/8 HTTP/1.1" 200 OK
at floor 4 and moving IDLE
going up!
approaching floor 5
requested floor 7
INFO:     127.0.0.1:37902 - "POST /floor/7 HTTP/1.1" 200 OK
at floor 5 and moving UP
approaching floor 6
at floor 6 and moving UP
approaching floor 7
at floor 7 and moving UP
at floor 7 and doors open
at floor 7 and moving UP
approaching floor 8
at floor 8 and moving UP
at floor 8 and doors open
at floor 8 and moving IDLE
```

Different elevator algorithms exist to optimize for different use cases. The typical elevator has a button or two outside to fetch the elevator, and separate floor buttons inside. Some systems allow fetching the elevator and requesting a floor at the same time. Feel free to conceptualize whichever style of elevator you find fun.
