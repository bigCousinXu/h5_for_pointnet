import os
import shutil


# 注意：所有文件夹路径结尾都写上加上\\，否则报错

def pcd2txt(pcd_path, txt_path):
    '''
    将后缀名pcd改为txt
    :param pcd_path: pcd格式数据路径
    :param txt_path: 你想存放txt格式数据的路径
    :return:
    '''
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)
    for root, _, filenames in os.walk(pcd_path):
        for i in range(len(filenames)):
            if filenames[i].endswith('.pcd'):
                newname = os.path.splitext(filenames[i])[0] + '.txt'
                os.rename(root + filenames[i], txt_path + newname)


def classify_one_class(obj_path, txt_path, target_path):
    '''
    将属于同一类的模型归类到一个文件夹里
    :param obj_path:一类模型文件夹路径 如：".../airplane/(文件夹里是airplane_001.obj,airplane_002.obj,...)"
    :param txt_path: txt格式数据的路径
    :param target_path: 分好类的文件 如：".../airplane/(文件夹里是airplane_001.pcd,airplane_002.pcd,...)"
    :return:
    '''
    list = []
    for root, _, filenames in os.walk(obj_path):
        for i in range(len(filenames)):
            if filenames[i].endswith('.obj'):
                list.append(os.path.splitext(filenames[i])[0])

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for root, _, filenames in os.walk(txt_path):
        for i in range(len(filenames)):
            if filenames[i].endswith('.txt'):
                if os.path.splitext(filenames[i])[0] in list:
                    shutil.copy(root + filenames[i], target_path)


def classify_txt(class_path, txt_path, target_path):
    '''
    根据原分类情况，将模型放到各自类别里
    :param class_path: 该路径下应该包含所有类别（路径下只能有只有各类别文件夹）
    :param txt_path: txt格式数据的路径
    :param target_path: 你想存放的分类好的txt数据路径
    :return:
    '''
    list = os.listdir(class_path)
    print('共%s' % len(list) + '个类')
    print(list)
    for i in range(len(list)):
        classify_one_class(obj_path=class_path + list[i] + '\\', txt_path=txt_path,
                           target_path=target_path + list[i] + '\\')
        print(list[i] + ' ==> finished')
    print('全部分类完成！')


if __name__ == '__main__':
    pcd2txt(pcd_path='H:\\dataset_mtl\\train_pcd\\', txt_path='H:\\temp_txt\\')
    classify_txt(class_path='H:\\dataset_mtl\\train\\', txt_path='H:\\temp_txt\\', target_path='H:\\class\\')
