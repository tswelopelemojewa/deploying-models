import pickle
import sys

with open('models/knn_regressor_rqd.pkl','rb') as f:
        rqd_model = pickle.load(f)
        print(rqd_model.predict([[sys.argv[1], sys.argv[2], sys.argv[3]]]))

