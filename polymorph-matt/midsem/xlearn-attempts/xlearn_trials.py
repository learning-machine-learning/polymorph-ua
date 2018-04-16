import sys
import os
import xlearn as xl

def ffm(trainfile, testfile):
    ffm_model = xl.create_ffm()
    ffm_model.setTrain("data/" + trainfile)
    test = "data/" + testfile
    ffm_model.setValidate(test)
    param = {'task': 'binary', 'lr': 0.2, 'lambda': 0.002}
    ffm_model.fit(param, "./model.out")
    ffm_model.setTest(test)
    ffm_model.predict("./model.out", "./output.txt")

if __name__ == "__main__":
    ffm(sys.argv[1], sys.argv[2])
