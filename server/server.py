#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'codingmrwang'
import sys
sys.path.append('../')

import helper
from gen_py.content.task import TaskManageService
from gen_py.base import ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

__HOST = 'localhost'
__PORT = 8080

class TaskManager(object):
    def update_create_task(self, data):
        result, code = helper.update_or_create(data)
        return ttypes.BaseResp(StatusMessage=result, StatusCode=code)


if __name__ == '__main__':
    handler = TaskManager()

    processor = TaskManageService.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor,transport, tfactory, pfactory)

    print('Starting the rpc server at', __HOST,':', __PORT)
    rpcServer.serve()
