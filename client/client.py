#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from gen_py.content.task.TaskManageService import Client
from gen_py.content.task.ttypes import Task

__HOST = 'localhost'
__PORT = 8080

tsocket = TSocket.TSocket(__HOST, __PORT)
transport = TTransport.TBufferedTransport(tsocket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Client(protocol)

task = Task(app_psm='coveragedb', app_task_type=1, app_task_id='12311432423', status=1, next_run_time='2018-09-01 08:00:00')
transport.open()

rps = client.update_create_task(task)
print(rps)
