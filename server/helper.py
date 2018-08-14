#! /usr/bin/env python
# -*- coding: utf-8 -*-

import django
import sys

sys.path.append('../')


os.environ['DJANGO_SETTINGS_MODULE'] = 'djangosite.settings'
from gen_py.base import ttypes
from djangosite.models.cheetah import Task

django.setup()


def update_or_create(req):
    if not req.status and req.next_run_time:
        return ttypes.BaseResp(StatusMessage='Need input status and next_run_time', StatusCode=400)
    info = {
        'status': req.status,
        'next_run_time': req.next_run_time
    }
    logging.info(str(info))
    try:
        if req.task_id and req.app_psm and req.app_task_type and req.app_task_id:
            if Task.objects.filter(task_id=req.task_id).exists():
                Task.objects.update_or_create(task_id=req.task_id, defaults=info)
                return ttypes.BaseResp(StatusMessage='Successfully update task', StatusCode=200)
            else:
                info['app_psm'] = req.app_psm
                info['app_task_type'] = req.app_task_type
                info['app_task_id'] = req.app_task_id
                Task.objects.update_or_create(task_id=req.task_id, defaults=info)
                return ttypes.BaseResp(StatusMessage='Successfully create task', StatusCode=200)
        elif req.task_id:
            if Task.objects.filter(task_id=req.task_id).exists():
                Task.objects.update_or_create(task_id=req.task_id, defaults=info)
                return ttypes.BaseResp(StatusMessage='Successfully update task', StatusCode=200)
            else:
                return ttypes.BaseResp(StatusMessage='No task exists in the database', StatusCode=400)
        elif req.app_psm and req.app_task_type and req.app_task_id:
            if Task.objects.filter(app_psm=req.app_psm, app_task_type=req.app_task_type, app_task_id=req.app_task_id).exists():
                Task.objects.update_or_create(app_psm=req.app_psm, app_task_type=req.app_task_type, app_task_id=req.app_task_id, defaults=info)
                return ttypes.BaseResp(StatusMessage='Successfully update task', StatusCode=200)
            else:
                return ttypes.BaseResp(StatusMessage='No task exists in the database', StatusCode=400)
        else:
            return ttypes.BaseResp(StatusMessage='need input task_id or app info', StatusCode=400)
    except Exception as e:
        return ttypes.BaseResp(StatusMessage=e.message, StatusCode=400)
