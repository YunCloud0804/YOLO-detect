import cv2
import os
import math
import shutil


# 根据任务要求，定义一个caijian函数
def caijian(path, path_out, size_w=256, size_h=256, step=256):  # step为步长，设置为256即相邻图片重叠50%
    ims_list = os.listdir(path)  # 在此例中调用时，ims_list为['image.png', 'label.png']

    for im_list in ims_list:
        number = 0
        name = im_list[:-4]  # 去除“.png”后缀
        img = cv2.imread(path + im_list)  # 读取要切割的图片
        size = img.shape
        i = 0
        if size[0]<512:
            size_h=size[0]

        if size[1]<512:
            size_w=size[1]

        for h in range(0, size[0], step):
            star_h = h  # star_h表示起始高度，从0以步长step=256开始循环
            for w in range(0, size[1], step):
                star_w = w  # star_w表示起始宽度，从0以步长step=256开始循环
                end_h = star_h + size_h  # end_h是终止高度

                if end_h > size[0]:  # 如果边缘位置不够512的列
                    # 以倒数512形成裁剪区域
                    star_h = size[0] - size_h
                    end_h = star_h + size_h
                    i = i - 1
                end_w = star_w + size_w  # end_w是中止宽度
                if end_w > size[1]:  # 如果边缘位置不够512的行
                    # 以倒数512形成裁剪区域
                    star_w = size[1] - size_w
                    end_w = star_w + size_w
                    i = i - 1

                cropped = img[star_h:end_h, star_w:end_w]  # 执行裁剪操作
                i = i + 1
                name_img = name + '_' + str(star_h) + '_' + str(star_w)  # 用起始坐标来命名切割得到的图像，为的是方便后续标签数据抓取
                #                 name_img = name + str(i)
                cv2.imwrite('{}/{}.jpg'.format(path_out, name_img), cropped)  # 将切割得到的小图片存在path_out路径下
    print("已成功执行！")


# 将完整的图像划分为小块
if __name__ == '__main__':
    ims_path = 'C:/Users/Cloud/Desktop/SCH/'  # 图像数据集的路径
    # 在result文件夹下，创建一个label_s文件夹，用于存放label切割的结果
    path = 'C:/Users/Cloud/Desktop/256/'  # 切割得到的数据集存放路径，当caijian函数执行后label_s文件夹下，存放的是image和label切割的结果
    if not os.path.exists(path):
        os.makedirs(path)
    caijian(ims_path, path, size_w=512, size_h=512, step=512)  # 调用caijian函数，如果相邻图片不想有重叠部分，则将step设置为512，即与裁剪的尺寸一致
