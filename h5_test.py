# coding=utf-8
import h5py  # 导入工具包
import os
import numpy as np

# HDF5的写入：
# imgData = np.zeros((30, 3, 128, 256))
# f = h5py.File('HDF5_FILE.h5', 'w')  # 创建一个h5文件，文件指针是f
# f['data'] = imgData  # 将数据写入文件的主键data下面
# f['labels'] = range(100)  # 将数据写入文件的主键labels下面
# f.close()  # 关闭文件

# HDF5的读取：
# f = h5py.File('G:/3d_data/modelnet40_ply_hdf5_2048/ply_data_train0.h5', 'r')  # 打开h5文件
f = h5py.File('train_4.h5', 'r')  # 打开h5文件
f.keys()  # 可以查看所有的主键
print(f.keys())
n = []
for key in f.keys():
    print('---------------------------------------')
    print(f[key].name)
    print(f[key].shape)
    print(f[key].dtype)
    print(f[key][0:2])
    print('---------------------------------------')
    print('\n')
f.close()