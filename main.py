import numpy as np
import rosbag
import cv2

if __name__ == '__main__':
    bag_path = "xx"
    img_dir = "xx"

    bag = rosbag.Bag(bag_path) # 读取Bag
    info = bag.get_type_and_topic_info() # 获取bag中包含的信息
    print(info) # 看看topic名称

    topics = 'xx' # 选择想要提取的topic
    index = 0
    for topic, msg, t in bag.read_messages(topics):# 读取特定的topic
        data = msg.data
        img = np.frombuffer(data, dtype=np.uint8)
        img = img.reshape(msg.height, msg.width)
        cv2.imwrite(img_dir+"{:0>5d}.jpg".format(index), img)  # 保存图片
        index += 1
