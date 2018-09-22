import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import os
import collect_data


train_data_list = os.listdir('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/')
#
#
# for training_array in train_data_list:
#     print(training_array)
#     training_array = np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/' + training_array)
#     for data in training_array:
#         img = data[0]
#         choice = data[1]
#         cv2.imshow('test', img)
#         print(choice)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break

lefts = []
rights = []
backs = []
forwards = []
forlef = []
forrig = []
baclef = []
bacrig = []
attack = []
rollf = []
rollb = []
rolll = []
rollr = []
lokon = []
rolfr = []
rolfl = []
rolbr = []
rolbl = []


for training_array in train_data_list:
    training_array = np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/' + training_array)
    for data in training_array:
        img = data[0]
        choice = data[1]

        if choice == collect_data.key_map['A']:
            lefts.append([img, choice])
        elif choice == collect_data.key_map['W']:
            forwards.append([img, choice])
        elif choice == collect_data.key_map['D']:
            rights.append([img, choice])
        elif choice == collect_data.key_map['S']:
            backs.append([img, choice])
        elif choice == collect_data.key_map['WA']:
            forlef.append([img, choice])
        elif choice == collect_data.key_map['WD']:
            forrig.append([img, choice])
        elif choice == collect_data.key_map['SA']:
            baclef.append([img, choice])
        elif choice == collect_data.key_map['SD']:
            bacrig.append([img, choice])
        elif choice == collect_data.key_map['J']:
            attack.append([img, choice])
        elif choice == collect_data.key_map['WK']:
            rollf.append([img, choice])
        elif choice == collect_data.key_map['SK']:
            rollb.append([img, choice])
        elif choice == collect_data.key_map['AK']:
            rolll.append([img, choice])
        elif choice == collect_data.key_map['DK']:
            rollr.append([img, choice])
        elif choice == collect_data.key_map['U']:
            lokon.append([img, choice])
        elif choice == collect_data.key_map['WDK']:
            rolfr.append([img, choice])
        elif choice == collect_data.key_map['WAK']:
            rolfl.append([img, choice])
        elif choice == collect_data.key_map['SDK']:
            rolbr.append([img, choice])
        elif choice == collect_data.key_map['SAK']:
            rolbl.append([img, choice])
        else:
            print('no matches')


# forwards = forwards[:len(lefts)][:len(rights)][:len(backs)][:len(forlef)][:len(forrig)][:len(baclef)][:len(bacrig)][:len(attack)][:len(rollf)][:len(rollb)][:len(rolll)][:len(rollr)][:len(lokon)][:len(rolfr)][:len(rolfl)][:len(rolbr)][:len(rolbl)]
# lefts = lefts[:len(forwards)]
# rights = rights[:len(forwards)]
# backs = backs[:len(forwards)]
# forlef = forlef[:len(forwards)]
# forrig = forrig[:len(forwards)]
# baclef = baclef[:len(forwards)]
# bacrig = bacrig[:len(forwards)]
# attack = attack[:len(forwards)]
# rollf = rollf[:len(forwards)]
# rollb = rollb[:len(forwards)]
# rolll = rolll[:len(forwards)]
# rollr = rollr[:len(forwards)]
# lokon = lokon[:len(forwards)]
# rolfr = rolfr[:len(forwards)]
# rolfl = rolfl[:len(forwards)]
# rolbr = rolbr[:len(forwards)]
# rolbl = rolbl[:len(forwards)]

final_data = forwards + lefts + rights + backs + forlef + forrig + baclef + bacrig + attack + rollf + rollb + rolll + rollr + lokon + rolfl + rolfr + rolbr + rolbl
shuffle(final_data)
x=0
for dataset in final_data:
    x += 1
    np.save('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data2/training_data_' + str(x) +'_v2.npy', dataset)