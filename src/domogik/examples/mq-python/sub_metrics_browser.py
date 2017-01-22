#!/usr/bin/python
# -*- coding: utf-8 -*-                                                                           
"""
@api {SUB} metrics.browser Subscribe to the metrics of browsers informations
@apiVersion 0.5.0
@apiName metrics.browser
@apiGroup Metrics
@apiDescription Subscribe to the metrics of browsers informations
* Source client : Any Domogik python component : core components, plugins, ...
* Target client : n/a

@apiExample {python} Example usage:
     class Test(MQAsyncSub):
     
         def __init__(self):
             MQAsyncSub.__init__(self, zmq.Context(), 'test', ['metrics.browser'])
             IOLoop.instance().start()
     
         def on_message(self, msgid, content):
             print(u"New pub message {0}".format(msgid))
             print(u"{0}".format(content))
    
    if __name__ == "__main__":
        Test()
    
@apiSuccessExample {json} Success-Response:
[...]
"""

import zmq
from domogikmq.pubsub.subscriber import MQAsyncSub
from zmq.eventloop.ioloop import IOLoop
from domogikmq.message import MQMessage

class Test(MQAsyncSub):

    def __init__(self):
        MQAsyncSub.__init__(self, zmq.Context(), 'test', ['metrics.browser'])
        IOLoop.instance().start()

    def on_message(self, msgid, content):
        print(u"New pub message {0}".format(msgid))
        print(u"{0}".format(content))

if __name__ == "__main__":
    Test()
