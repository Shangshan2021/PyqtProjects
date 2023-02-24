import pickle


def init_data():
    data={
        'API':[{
            '默认':'https://open.teambition.com/api/task/tqlsearch',
            'TQL':'https://open.teambition.com/api/task/tqlsearch',
        }],
        'User':[{
            '默认':'63310bc0b2b7b2cf2ca8a3b2',
            '鄢宇航':'63310bc0b2b7b2cf2ca8a3b2',
        }],
        'method':[{
            'Get':'get',
            'Post':'post',
            'Put':'put',
            'Del':'del',
        }]
    }
    with open('config.json', 'wb') as f:
        pickle.dump(data, f)


def checkin_data(data):
    with open('config.json', 'wb') as f:
        pickle.dump(data, f)



def init_qt():
    with open('config.json', 'rb') as f:
        data = pickle.load(f)
    return data
