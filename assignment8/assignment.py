import os
import pandas as pan
import json
import pickle
import cv2


def persist_data(data, filename):
    with open(filename, 'w') as file:
            file.write(data)

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        print(data)

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def delete_file(filename):
    os.remove(filename)

def overwrite_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def append_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)

def write_binary_file(filename, data):
    with open(filename, "wb") as file:
        file.write(data)

def read_image_file(filename):
    image = cv2.imread(filename)
    cv2.imshow("Input Image", image)

def read_csv_file(filename):
    with open(filename,'r'):
        df = pan.read_csv(filename)
        print(df)

def write_csv_file(filename, df):
    with open(filename,'w'):
        df.to_csv(filename, index=False)

def read_json_file(filename):
    with open(filename, 'r'):
        data = json.load(filename)
        print(data)

def write_json_file(filename, data):
    with open(filename, 'w'):
        json.dump(data, filename)

def write_pickle_file(filename, data):
    with open("data.pkl", "wb") as file:
        pickle.dump(data, filename)

def read_pickle_file(filename):
    with open(filename,'rb'):
        data = pickle.load(filename)
        print(data)