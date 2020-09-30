def deserialize(field):
    data = field.split(',')
    data = [(data[i], i * 3) for i in range(len(data))]
    return data
