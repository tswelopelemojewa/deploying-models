import pickle

def predict_q():
    with open('models/extra_tree_q.pkl','rb') as f:
        q_model = pickle.load(f)
        print(q_model.predict([[52.00, 12, 2.0, 2.0, 0.40]]))

# q ends here
predict_q()
