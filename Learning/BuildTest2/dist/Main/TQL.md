# TQL

#### 请求

| 基础信息 | 内容                                           |
| -------- | ---------------------------------------------- |
| URL      | https://open.teambition.com/api/task/tqlsearch |
| Method   | **POST**                                       |
| 权限     | tb-core:task:get                               |

#### 请求头

| 名称          | 类型   | 必填 | 描述             |
| ------------- | ------ | ---- | ---------------- |
| Authorization | string | 1    | app_access_token |
| X-Tenant-Type | string | 1    | organization     |
| X-Tenant-Id   | string | 1    | 企业ID           |

#### 请求体

| 名称                       | 类型    | 必填 | 描述                                                         |
| -------------------------- | ------- | ---- | ------------------------------------------------------------ |
| tql                        | string  | 0    | 查询语句；参见文档[TQL](https://thoughts.teambition.com/share/6233d89c89630f0041a381a1#title=TQL介绍) |
| remainProjectCustomfieldId | string  | 0    | 兼容企业自定义字段参数                                       |
| orderBy                    | string  | 0    | 排序字段;支持（dueDate/priority....）                        |
| pageToken                  | string  | 0    | 分页 token，首次获取数据时为空                               |
| pageSize                   | integer | 0    | 返回结果数量，默认 30，最大 1000                             |




#### TQL 最佳实践

建议查询范围**限制在项目内**，这样可以得到最优的查询效率

在原 TQL 后用 **AND** 符号增加 **_projectId** 查询条件

- 单个可以用 **_projectId = 项目 ID** 

- 例如`_projectId = 632d1f89d7242f0444627abd `

- 多个可以用 **_projectId IN (项目 ID1， 项目 ID2)** 

- 例如`_projectId IN (632d1f89d7242f0444627abd, 632d1f89d7242f0444627abe)`

#### 支持的关键字

注: 所有的关键字名的下划线都可以省略, 如_id可以写为id

提醒：**操作符必须全部大写**（IN、AND 等）

| 关键字                 | 支持的操作符     | 说明                             |
| ---------------------- | ---------------- | -------------------------------- |
| content                | ~                | 模糊查询标题                     |
| note                   | ~                | 模糊查询备注                     |
| _id                    | =, IN            | 按照任务id查询                   |
| _appId                 | =, IN            | 限定任务所属app                  |
| _organizationId        | =, IN            | 限定任务所属企业                 |
| _projectId             | =, IN            | 限定任务所属项目                 |
| _tasklistId            | =, IN            | 限定任务所属分组                 |
| _stageId               | =, IN            | 限定任务所属列表                 |
| _scenariofieldconfigId | =, IN            | 限定任务所属任务类型             |
| _sprintId              | =, IN            | 限定任务所属迭代                 |
| ancestorIds            | =, IN            | 限定任务所属祖先                 |
| _parentId              | =, IN            | 限定任务所属父任务               |
| _executorId            | =, IN, !=, NOTIN | 限定任务执行者                   |
| _creatorId             | =, IN            | 限定任务创建者                   |
| _tagId                 | =, IN            | 限定任务含有特定标签             |
| involveMember          | =, IN            | 限定任务含有特定参与者           |
| isDone                 | =                | 限定任务完成状态                 |
| accomplished           | =, >, >=, <, <=  | 限定任务完成时间                 |
| startDate              | =, >, >=, <, <=  | 限定任务开始时间                 |
| dueDate                | =, >, >=, <, <=  | 限定任务截止时间                 |
| created                | =, >, >=, <, <=  | 限定任务创建时间                 |
| updated                | =, >, >=, <, <=  | 限定任务更新时间                 |
| priority               | =, IN            | 限定任务优先级                   |
| isArchived             | =                | 限定任务归档状态                 |
| onlyChildren           | =                | 只查询子孙任务, 仅值为true时有效 |
| onlyTopTask            | =                | 只查询顶级任务, 仅值为true时有效 |