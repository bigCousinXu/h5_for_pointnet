# h5_for_pointnet
generate h5 for pointnet

Steps:
    1. obj采样生成txt(只用来分类的话，采三通道就可以)
    2. 将txt按原类别归类（classify.py）
    3. 生成h5（generate_h5.py）
    4. 查看生成的h5是否符合要求（test_h5.py）
    
obj格式模型的文件组织结构：
obj
  |___ airplane
  |          |__ airplane_001.obj
  |          |__ airplane_002.obj
  |          |         ...
  |          |__ airplane_030.obj
  |
  |___ bowl
  |          |__ bowl_001.obj
  |          |__ bowl_002.obj
  |          |     ...
  |          |__ bowl_009.obj
  |
  |     .......
