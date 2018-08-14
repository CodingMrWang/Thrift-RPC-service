// Author: codingmrwang

include "base.thrift"

namespace py content.task

struct Task {
    # 基础字段
    1: string app_psm, # 业务方psm
    2: i16 app_task_type, # 业务方的task type
    3: string app_task_id, # 业务方的task id
    4: string task_id,

    # 更新字段
    5: required i16 status, # 状态
    6: required string next_run_time, #下次调度时间 格式: yyyy-mm-dd hh:mm:ss
}

service TaskManageService
{
    # 更新task
    base.BaseResp update_create_task(1:Task req),
}
