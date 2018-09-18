import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

train_data_list = [
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1058.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1059.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1060.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1061.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1062.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1063.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1064.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1065.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1066.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1067.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1068.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1069.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1070.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1071.npy'),
    np.load('C:/Users/IyaJe/PycharmProjects/gundyrtrain/data/training_data-1072.npy')]



for training_array in train_data_list:
    for data in training_array:
        img = data[0]
        choice = data[1]
        cv2.imshow('test', img)
        print(choice)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
