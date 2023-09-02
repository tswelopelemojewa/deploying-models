import pickle
import sys


with open('models/gradient_boosting_ucsvsr.pkl','rb') as f:
        ucsvsr_model = pickle.load(f)
        print(ucsvsr_model.predict([[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]]))
