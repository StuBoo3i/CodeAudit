import pickle


def serialize(data):
    """
    序列化list
    :param data: list
    :return: 序列化结果
    """
    # 序列化列表数据
    serialized_data = pickle.dumps(data)
    return serialized_data


def deserialize(data):
    """
    反序列化list
    :param data: 数据
    :return: 反序列化结果
    """
    deserialize_data = pickle.loads(data)
    print(deserialize_data)
