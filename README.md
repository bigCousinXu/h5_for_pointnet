# h5_for_pointnet
## generate h5 for pointnet

### Steps:
    1. obj采样生成txt(只用来分类的话，采三通道就可以)
    2. 将txt按原类别归类（classify.py）
    3. 生成h5（generate_h5.py）
    4. 查看生成的h5是否符合要求（test_h5.py）
