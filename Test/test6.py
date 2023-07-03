import pickle

data = [[('a', 2, 17), ('b', 2, 24), ('c', 3, 13)],
        [('c', 4, 9), ('a', 4, 13), ('b', 4, 17), ('c', 6, 16)],
        [('c', 6, 16)]]

# 序列化列表数据
serialized_data = pickle.dumps(data)
print(serialized_data)
data = pickle.loads(serialized_data)
print(data)
