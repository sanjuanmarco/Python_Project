from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)

twitter = "twitter"
fb = "facebook"


@app.route("/")
def home():
    
    return render_template("index.html")

#-----------------------------------------------------------FOR URL----------------------------------------------------------------
import pickle

from googlesearch import search 

@app.route("/URLResults", methods = ["GET", "POST"])
def user():
    import requests
    from newsplease import NewsPlease

    if request.method == "POST":
        urlink = str(request.form.get("link"))

        try:
            response = requests.get(urlink)
            article = NewsPlease.from_url(urlink)
            head = article.title

            mylinks = []
            

            if twitter in urlink or fb in urlink:
                msg = "Sorry, social media links cannot be accessed due to privacy laws. For social media posts, please copy the text and paste in the INSERT STATEMENT field."
                return render_template("wrongURL.html", msg = msg)
            elif head != None:
                #score
                load_model = pickle.load(open('final_model__.sav', 'rb'))
                prediction = load_model.predict([head])
                prob = load_model.predict_proba([head])

                pred = prediction[0]
                probability = prob[0][1]

                probs = round((probability*100))

                #relatedlinks
                for i in search(head, tld="co.in", num=5, start=1, stop=5, pause=2):
                    if fb in i or twitter in i:
                        continue
                    mylinks.append(str(i))

                return render_template("URLResults.html", links = urlink, rel = mylinks, pred = pred, prob = probs, head = head)

            

        except requests.ConnectionError as exception:
            msg = "URL does not exist, please make sure to provide a valid URL."
            return render_template("wrongURL.html", msg = msg)

        except Exception:
            msg = "URL not detected, please make sure to provide a valid URL."
            return render_template("wrongURL.html", msg = msg)
        


    

#-----------------------------------------------------------FOR STATEMENT----------------------------------------------------------------



@app.route("/StatementResults", methods = ["GET", "POST"])
def user_statement():
    
    if request.method == "POST":

        state = str(request.form.get("state"))

        res = len(state.split())

        if res < 4:
            msg = "Not enough information, please provide a longer statement."
            return render_template("wrongURL.html", msg = msg)

        else:

            #score
            load_model = pickle.load(open('final_model__.sav', 'rb'))
            prediction = load_model.predict([state])
            prob = load_model.predict_proba([state])

            pred = prediction[0]
            probability = prob[0][1]

            probs = round((probability*100))

            mystate = []
            #relatedlinks
            for i in search(state, tld="co.in", num=5, start=1, stop=5, pause=2):
                if fb in i or twitter in i:
                    continue
                mystate.append(str(i))
        
            return render_template("StatementResults.html", rel = mystate, state = state, pred = pred, prob = probs)

#-----------------------------------------------------------FOR IMAGE----------------------------------------------------------------

app.config["UPLOAD_PATH"] = "C:/Users/Kyle/Documents/SVM/static/uploads"
@app.route("/ImageResults", methods = ["GET", "POST"])
def user_image():

    import easyocr
    
    
    if request.method == "POST":
        if request.files:

            img = request.files["image_upload"]

            print(img.filename)
            
            img_file = img.save(os.path.join(app.config['UPLOAD_PATH'], img.filename)) #save to local folder

            image = "static/uploads/" + img.filename #location to pass in html


            reader = easyocr.Reader(['en'], gpu=False)
            result = reader.readtext(image, detail = 0) 

            result_list = []

            for word in result:
                result_list.append(word)

            sentences = " ".join(result_list)

            if (not sentences):
                msg = "No text detected, please check your uploaded image."
                return render_template("wrongURL.html", msg = msg)

            else:
                #score
                load_model = pickle.load(open('final_model__.sav', 'rb'))
                prediction = load_model.predict([sentences])
                prob = load_model.predict_proba([sentences])

                pred = prediction[0]
                probability = prob[0][1]

                probs = round((probability*100))

                mywords = []
                #relatedlinks
                for i in search(sentences, tld="co.in", num=5, start=1, stop=5, pause=2):
                    if fb in i or twitter in i:
                        continue
                    mywords.append(str(i))
        
                return render_template("ImageResults.html", image = image, sentences = sentences, rel = mywords, pred = pred, prob = probs)

if __name__ == '__main__': 
    app.run(debug = True)