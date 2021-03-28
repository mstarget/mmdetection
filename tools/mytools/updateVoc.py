from lxml import etree
import os

def update_file(dir_name):
    files = os.listdir(dir_name)
    new_path = "D:/资料/CV/video/update_VOCdevkit/VOCdevkit/VOC2007/Annotations/"

    for file_name in files:
        with open(dir_name+file_name, encoding='UTF-8') as fid:
            xml_str = fid.read()
            new_xml_str = xml_str.replace('trolley casew', 'trolley case')

        with open(new_path+file_name, 'w', encoding='UTF-8') as fid:
            fid.write(new_xml_str)









if __name__ == '__main__':

    update_file("D:/资料/CV/video/VOCdevkit/VOC2007/Annotations/")


