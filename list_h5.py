import os

'''
获取所有 h5 格式文件，并写入txt
'''
TARGETPATH = 'G:\\3d_data\\my_model\\'
records = []
for root, _, filenames in os.walk(TARGETPATH):
    for i in range(len(filenames)):
        if filenames[i].endswith('.h5'):
            records.append(filenames[i])
# 将records写入.txt
txtFile = open(os.path.join(TARGETPATH, 'train.txt'), 'w')
for line in records:
    txtFile.write(line + '\n')
txtFile.close()