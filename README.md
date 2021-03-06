[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![TODOs](https://badgen.net/https/api.tickgit.com/badgen/github.com/aroshanineshat/uMQ)](https://www.tickgit.com/browse?repo=github.com/aroshanineshat/uMQ)

<p align="center">
  <img src="https://github.com/aroshanineshat/uMQ/blob/master/img/logo.png?raw=true" alt="uMQ logo"/>
</p>

# uMQ: A minimal and reliable JSON MQ library!
uMQ is a minimal package derived from my main research project to achieve reliable and fast JSON communication.

## The story:
I'm developing a full-fledged hardware+software product as my research project and I needed to instanciate IPC communication between two(or several) python processes. After looking around, found packages with extreme capabilities. 0MQ(https://zeromq.org/) and RabbitMQ are just a couple of examples. My specific application didn't need to use all those features and I didn't see the necessity of going through their steep learning curves so I decided to write my own code.

As a hardware engineer, I deal with state machines all the time. I have used state machines in this code to reliably convert bytes to JSON packets.

## Development:
My goal is to keep this packege easy to use. You only need to learn one class and three functions to start a JSON communication. My main focus is currently to fix bugs and improve the performance.

Please feel free to contribute, add features or request them.


# Usage

## Installing

To install the package you can simply do:

    $ pip install uMQ

## Starting the communication

On the server side, run:
    
```python
    uMQIntance = uMQ_Socket()
    uMQIntance.server("localhost", 5008)
    while (True):
        uMQIntance.hold()
        while (uMQIntance.data_available()):
            data = uMQIntance.get_next_pkt()
            ## do something with the data
        uMQIntance.Clear()
```

This will create a uMQ_Socket which is listening on localhost and port 5008.

on the client side do:

```python
    data = {"Sample Data": "DEADBEEF"}
    uMQIntance = uMQ_Socket()
    uMQIntance.connect("localhost", 5008)
    uMQIntance.send_all (json.dumps(data))
```

For the complete test scripts. Refer to the "tests" directory.
