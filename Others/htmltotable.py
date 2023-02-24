a="""templateId
string
任务类型 ID
tasklistId
string
任务列表 ID
taskgroupId
string
任务分组 ID
content
string
任务内容
executorId
string
执行者的用户 ID
statusId
string
工作流状态 ID
sprintId
string
迭代 ID
startDate
string
开始时间
dueDate
string
截止日期
note
string
任务备注
priority
integer
优先级：0：普通（默认值） 1：紧急 2：非常紧急
visible
string
可见性：participants：任务参与者可见 projectMembers：项目成员可见（默认值
parentTaskId
string
父任务 ID
ancestorIds
array[string]
所有祖先任务，ancestorIds[0] 为直接父任务，ancestorIds[1] 为父任务的父任务，以此类推
participants
array[string]
参与者的用户 ID 列表
orgId
string
企业 ID
accomplishDate
string
实际完成时间
isDone
integer
是否完成
tagIds
array[string]
标签 ID 列表
customfields
array[object]
自定义字段列表
creatorId
string
创建者 id
modifierId
string
最近一次执行更新操作的用户 ID
updated
string
最近一次更新时间
created
string
任务创建时间
uniqueId
string
任务唯一id
code
number
响应状态码
errorMessage
string
异常错误信息"""
a_list=a.split('\n')
i=0
title='| 名称          | 类型   | 描述             |\n| ------------- | ------ | ---------------- |\n'
test=a_list[0]
while i<len(a_list):
    title=title+f'| {a_list[i]} | {a_list[i+1]} | {a_list[i+2]} |\n'
    i=i+3
print(title)