import pickle

def inputPredict(input):

    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([input])
    prob = load_model.predict_proba([input])


    print("<b>Label:</b>",prediction[0])
    print("<br><b>Probability score:</b>",prob[0][1])