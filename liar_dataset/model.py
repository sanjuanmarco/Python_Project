import pickle
var = "Obama is smart."
#pickle.dump(svm_pipeline_ngram,open(model_file,'wb')) 
load_model = pickle.load(open('C:\\Users\jake\\Documents\\GitHub\\Python_Project\\liar_dataset\\final_model.sav', 'rb'))
prediction = load_model.predict([var])
prob = load_model.predict_proba([var])

print("The given statement is ",prediction[0])
print("The probability score is ",prob[0][1])
