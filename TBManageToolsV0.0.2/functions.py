import json
from TBFunc import GetTeamBitionEvents


def add_parameter(par_switch, parameters):
    parameter_dict = {}
    parameters_list = parameters.split('\n')
    for _ in parameters_list:
        item = _.split(':')
        parameter_dict[item[0]] = item[1]
    parameter_js = open(f"data/{par_switch}.json", encoding="utf-8", mode="w")
    json.dump(parameter_dict, parameter_js)
    parameter_js.close()


def search_data(search_kind, search_content):
    try:
        tb = GetTeamBitionEvents()
        projects = {}
        if search_kind == '企业中所有项目名称及ID':
            result = tb.post_project()
            for project in result.json()['result']:
                projects[project['name']] = project['projectId']
            return projects
        elif search_kind == '项目中所有任务名称及ID（需写入项目ID）':
            tasks = {}
            projectId = search_content
            url = 'https://open.teambition.com/api/task/tqlsearch'
            params = {}
            object = {
                'tql': f'_projectId={projectId} AND isArchived = false',
                'pageSize': 4000
            }
            result = tb.general_function(url, params, object, 'post')
            for task in result.json()['result']:
                tasks[task['content']] = task['taskId']
            return tasks
        elif search_kind == '项目中所有任务类型名称及ID（需写入项目ID）':
            taskinds = {}
            projectId = search_content
            url = f'https://open.teambition.com/api/v3/project/{projectId}/scenariofieldconfig/search'
            params = {}
            object = {}
            result = tb.general_function(url, params, object, 'get')
            for taskind in result.json()['result']:
                taskinds[taskind['name']] = taskind['id']
            return taskinds
        elif search_kind == '项目中所有任务分组及ID（需写入项目ID）':
            taskgroups = {}
            projectId = search_content
            url = f'https://open.teambition.com/api/v3/project/{projectId}/tasklist/search'
            params = {}
            object = {}
            result = tb.general_function(url, params, object, 'get')
            for taskgroup in result.json()['result']:
                taskgroups[taskgroup['title']] = taskgroup['id']
            return taskgroups
    except Exception as e:
        return {"异常": str(e)}


def trans(string_list):
    dictionary = {}
    for string in string_list:
        if string == '':
            return dictionary
        pair = string.split(':')
        dictionary[pair[0]] = pair[1]
    return dictionary


def generate(api, method, user, params, object, conditions, backs):
    try:
        tb = GetTeamBitionEvents()
        results = tb.general_function(api, params, object, method, user).json()['result']
        for condition in conditions:
            data = []
            if condition == '':
                break
            condition_list = condition.split(':')
            if condition_list[1] == 'IN':
                for result in results:
                    if condition_list[0] in str(result[condition_list[2]]):
                        data.append(result)
                    else:
                        continue
            elif condition_list[1] == 'NOTIN':
                for result in results:
                    if condition_list[0] not in str(result[condition_list[2]]):
                        data.append(result)
                    else:
                        continue
            results = data
        data = []
        for result in results:
            result_dict = {}
            for back in backs:
                result_dict[back] = result[back]
            data.append(result_dict)
        return data
    except Exception as e:
        return "异常:"+str(e)


def statistic(_table, backs, data):
    for i in range(0, len(backs)):
        _table.cellAt(0, i).firstCursorPosition().insertText(backs[i])
    dict_num = 1
    for item in data:
        for i in range(0, len(backs)):
            _table.cellAt(dict_num, i).firstCursorPosition().insertText(str(item[backs[i]]))
        dict_num += 1
