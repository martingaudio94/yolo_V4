import xml.etree.ElementTree as ET
from os import getcwd,scandir,path

sets=[('2007', 'train')]

classes = ['1',
           '2',
           '3',
           '4',
           '5',]


def convert_annotation(year, image_id, list_file):
    in_file = open(r'C:\Users\Usuario1\Desktop\demo_vialidad\XLMS\{}.xml'.format(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()
image_id=scandir(r'C:\Users\Usuario1\Desktop\demo_vialidad\imgs')
with open(r'C:\Users\Usuario1\Desktop\demo_vialidad\train.txt','a') as file:
    for i in image_id:
        if 'Thumb' not in i.name:
            file.write(i.name[:len(i.name)-4])
            file.write('\n')
        
image_ids = open(r'C:\Users\Usuario1\Desktop\demo_vialidad\train.txt').read().strip().split()
list_file = open('train.txt', 'w')
for image_id in image_ids:
    try:
        if 'Thumb' not in image_id:
            
            list_file.write(r'C:\Users\Usuario1\Desktop\demo_vialidad\imgs\{}.jpg'.format(image_id))
            convert_annotation(str(2020), image_id, list_file)
            list_file.write('\n')
    except Exception as e:
        print(e)
        continue
        
list_file.close()

