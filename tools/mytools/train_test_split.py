import os
import random

trainval_percent = 0.8

TRAIN_PERCENT = 0.6 #2790张
TEST_PERCENT = 0.3 #1395张
VAL_PERCENT = 0.1#465张


xmlfilepath = 'D:/资料/CV/video/VOCdevkit/VOC2007/Annotations'
total_xml = os.listdir(xmlfilepath)

market_xml=[]
station_xml=[]
metro_xml=[]
street_xml=[]
street_night_xml=[]

for xml in total_xml:
    if 'market' in xml:
        market_xml.append(xml)

    elif 'station' in xml:
        station_xml.append(xml)

    elif 'metro' in xml:
        metro_xml.append(xml)

    elif 'street_night' in xml:
        street_night_xml.append(xml)

    elif 'street' in xml:
        street_xml.append(xml)

from  sklearn.model_selection import train_test_split

market_trainval, market_test = train_test_split(market_xml, test_size=0.1, random_state=42)
station_trainval, station_test = train_test_split(station_xml, test_size=0.1, random_state=42)
metro_trainval, metro_test = train_test_split(metro_xml, test_size=0.1, random_state=42)
street_night_trainval, street_night_test = train_test_split(street_night_xml, test_size=0.1, random_state=42)
street_trainval, street_test = train_test_split(street_xml, test_size=0.1, random_state=42)


market_train, market_val = train_test_split(market_trainval, test_size=0.33, random_state=42)
station_train, station_val = train_test_split(station_trainval, test_size=0.33, random_state=42)
street_night_train, street_night_val = train_test_split(metro_trainval, test_size=0.33, random_state=42)
metro_train, metro_val = train_test_split(street_night_trainval, test_size=0.33, random_state=42)
street_train, street_val = train_test_split(street_trainval, test_size=0.33, random_state=42)

train_xmls=market_train+station_train+street_night_train+metro_train+street_train
test_xmls = market_test+ station_test+ metro_test+ street_night_test+ street_test
val_xmls = market_val+station_val+ street_night_val+ metro_val+ street_val




ftest = open('D:/资料/CV/video/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('D:/资料/CV/video/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('D:/资料/CV/video/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')



for train_xml in train_xmls:
    name = train_xml[:-4] + '\n'
    ftrain.write(name)

for val_xml in val_xmls:
    name = val_xml[:-4] + '\n'
    fval.write(name)


for test_xml in test_xmls:
    name = test_xml[:-4] + '\n'
    ftest.write(name)

ftrain.close()
fval.close()
ftest.close()