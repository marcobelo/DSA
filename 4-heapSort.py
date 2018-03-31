def left_right_son(father_index):
    left_son = ((father_index + 1) * 2) - 1
    right_son = ((father_index + 1) * 2)
    return left_son, right_son


def heapDo(data, index):
    left_son, right_son = left_right_son(index)
    last_son = len(data)
    if left_son < last_son and right_son < last_son:
        if data[index] < data[left_son] or data[index] < data[right_son]:
            if data[right_son] < data[left_son]:
                data[index], data[left_son] = data[left_son], data[index]
            else:
                data[index], data[right_son] = data[right_son], data[index]
        heapDo(data, left_son + 1)
        heapDo(data, right_son + 1)
    else:
        if left_son < last_son:
            if data[index] < data[left_son]:
                data[index], data[left_son] = data[left_son], data[index]
            heapDo(data, left_son + 1)
        elif right_son < last_son:
            if data[index] < data[right_son]:
                data[index], data[right_son] = data[right_son], data[index]
            heapDo(data, right_son + 1)


def heapCheck(data):
    heap_condition = False
    last_son = len(data)
    while not heap_condition:
        aux = 0
        for index in range(0, last_son//2):
            left_son, right_son = left_right_son(index)
            if left_son < last_son and right_son < last_son:
                if data[index] < data[left_son]:
                    aux = 1
                    heapDo(data, index)
                elif data[index] < data[right_son]:
                    aux = 1
                    heapDo(data, index)
            else:
                if left_son < last_son:
                    if data[index] < data[left_son]:
                        aux = 1
                        heapDo(data, index)
                elif right_son < last_son:
                    if data[index] < data[right_son]:
                        aux = 1
                        heapDo(data, index)
        print(data)
        if aux == 0:
            heap_condition = True


def heapSort(data):
    heapCheck(data)
    return data


input = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
result = heapSort(input)
print(result)
