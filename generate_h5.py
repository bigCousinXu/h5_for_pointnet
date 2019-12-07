import os
import h5py
import numpy as np

'''
readme:
        在main函数中将路径替换为你的训练集/测试集数据的路径
        （文件结构必须是：train/类别1,类别2...,每个类别下/airplane_1,airplane_2,...）
'''


def check(txt_path):
    '''
    检查每个模型采样点数是否够
    :param txt_path: 每个模型路径
    :return: 满足点数返回ture
    '''
    data = np.loadtxt(txt_path, delimiter=',')
    return data.shape[0] == 2048


def read_txt(txt_path):
    '''
    读取每个模型的数据
    :param txt_path: 单个txt格式的模型数据的路径
    :return: 2维数组（2048*3）
    '''
    data = np.loadtxt(txt_path, delimiter=',')
    return data.tolist()


def data_label_of_one_class(train_path, label_i):
    '''
    读取一个类的模型的数据
    :param train_path: 一个类别的模型路径
    :param label_i: 该类别的 label
    :return: 该类下所有模型data，label
    '''
    data = []
    label = []
    for root, _, filenames in os.walk(train_path):
        for i in range(len(filenames)):
            if filenames[i].startswith('model'):
                if check(root + filenames[i]):
                    data.append(read_txt(root + filenames[i]))
                    label.append([label_i])
    return data, label


def get_data_label(path):
    '''
    生成所有的data,label
    :param path: 数据集路径
    :return: data label
    '''
    all_class = os.listdir(path)
    # print(all_class)
    data = []
    label = []
    for i in range(len(all_class)):
        if os.path.isdir(path + all_class[i]):
            a, b = data_label_of_one_class(path + all_class[i] + '\\', i)
            data.extend(a)
            label.extend(b)
            print(all_class[i] + ' ===> get data, label finished, label is %d' % i)
    data = np.array(data)
    label = np.array(label)
    return data, label


# write data and label to H5 file
def save_h5(h5_filename, data, label, data_dtype='float32', label_dtype='uint8'):
    '''
    生成 h5 格式文件
    :param h5_filename: 想生成的 h5 文件名
    :param data: 写入的 data
    :param label: 写入的 label
    :param data_dtype: data的数据类型
    :param label_dtype: label的数据类型
    :return:
    '''
    h5_fout = h5py.File(h5_filename)
    h5_fout.create_dataset(
        'data', data=data,
        compression='gzip', compression_opts=4,
        dtype=data_dtype)
    h5_fout.create_dataset(
        'label', data=label,
        compression='gzip', compression_opts=1,
        dtype=label_dtype)
    h5_fout.close()


if __name__ == '__main__':
    data, label = get_data_label('G:\\class\\')
    print(data.shape)
    print(label.shape)


    #每个 h5 文件存放2048个模型，及其对应的label
    count = (int)(data.shape[0] / 2048)
    for i in range(count):
        start = i * 2048
        end = start + 2048
        save_h5(h5_filename='train_%d' % i + '.h5', data=data[start:end, :, :], label=label[start:end],
                data_dtype='float32', label_dtype='uint8')

    save_h5(h5_filename='train_%d' % count + '.h5', data=data[count * 2048:, :, :], label=label[count * 2048:],
            data_dtype='float32', label_dtype='uint8')
    print("generate finished!")

