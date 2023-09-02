import pickle
import sys

with open('models/Random_Forest_regresor_rmr.pkl','rb') as f:
        rmr_model = pickle.load(f)
        print(rmr_model.predict([[sys.argv[1], sys.argv[2]]]))

