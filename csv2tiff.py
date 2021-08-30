import pandas as pd
import numpy as np
import torch
import tifffile as tiff


def main():
    fake_fingerprint = pd.read_csv('fake_fingerprint.csv',header=None)
    results = pd.read_csv('results.csv',header=None)
    targetData = pd.read_csv('targetData.csv',header=None)
    fake_fingerprint = np.array(fake_fingerprint)
    results = np.array(results)
    targetData = np.array(targetData)
    for i in range(fake_fingerprint.shape[0]):
        print(i)
        tiff_img = np.reshape(fake_fingerprint[i],(8,8,2))
        tiff.imwrite('./fake_fingerprint/'+str(i)+'.tiff',tiff_img)
    for i in range(results.shape[0]):
        print(i)
        tiff_img = np.reshape(results[i],(8,8,2))
        tiff.imwrite('./results/'+str(i)+'.tiff',tiff_img)
    for i in range(targetData.shape[0]):
        print(i)
        tiff_img = np.reshape(targetData[i],(8,8,2))
        tiff.imwrite('./targetData/'+str(i)+'.tiff',tiff_img)

if __name__ == '__main__':
    main()