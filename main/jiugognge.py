import os
from PIL import Image


def wh_size(w, h):
    while w % 3 != 0:
        w += 1
    while h % 3 != 0:
        h += 1
    return w, h


def jgg_img(image, name):
    names = path + '\\Nine_GG' + '\\' + name  # 图片名称
    im = Image.open(image)  # 打开图片
    w, h = im.size  # 获取图片宽高
    width, height = wh_size(w, h)
    im = im.resize((width, height))  # 对图片宽高进行校准
    tr = int(width/100*1.3)  # 根据图片宽设置条纹宽度
    img = Image.new('RGB', (width + 2 * tr, height + 2 * tr), color='white')  # 新建图片底图
    zi = os.path.splitext(names)[0]
    if not os.path.exists(zi):  # 创建子文件夹 ！！！1
        os.mkdir(zi)  # ！！！2
    num = 0  # ！！！3
    imgtype = os.path.splitext(name)[1]  # ！！！4
    for i in range(3):
        for j in range(3):
            m = im.crop((int(width / 3) * j, int(height / 3) * i, int(width / 3) * (j + 1), int(height / 3) * (i + 1)))
            img.paste(m, (int(width / 3) * j+j*tr, int(height / 3) * i+i*tr))
            num += 1  # ！！！5
            m.save(zi+'//'+str(num)+imgtype)  # ！！！6
    img = img.resize((w, h))  # 调整图片大小
    img.save(names)  # 保存图片


if __name__ == '__main__':
    path = os.getcwd()
    print("请确保当前路径下，有相应类型的图片文件存在！")
    if not os.path.exists(path + '\\Nine_GG'):  # 判断文件夹是否创建
        os.mkdir(path + '\\Nine_GG')
    for i in os.listdir():  # 循环遍历当前工作路径下的所有文件
        if os.path.splitext(path + '\\' + i)[1] in ['.jpg', '.png', '.jpeg']:
            jgg_img(path + '\\' + i, i)
