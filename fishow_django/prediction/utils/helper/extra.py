def deserialize(field):
    data = field.split(',')
    data = [(int(data[i]), i * 3) for i in range(len(data))]
    return data

def deserialize2(field, field2):
    data = field.split(',')
    data2 = field2.split(',')
    data = [(int(data[i]), data2[i], i * 3) for i in range(len(data))]
    return data

def deserialize0(field):
    data = field.split(',')
    data = [data[i] for i in range(len(data))]
    return data