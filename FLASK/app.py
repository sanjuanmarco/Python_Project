from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)



@app.route("/")
def home():
    
    return render_template("index.html")

#-----------------------------------------------------------FOR URL----------------------------------------------------------------
import pickle
import requests
from newsplease import NewsPlease
from googlesearch import search 

@app.route("/URLResults", methods = ["GET", "POST"])
def user():
    if request.method == "POST":
        urlink = str(request.form.get("link"))

        try:
            response = requests.get(urlink)
            article = NewsPlease.from_url(urlink)
            head = article.title

            mylinks = []
            twitter = "https://twitter.com"
            fb = "https://www.facebook.com"
            mfb = "https://m.facebook.com"

            if twitter in urlink or fb in urlink:
                msg = "Sorry, social media links cannot be accessed due to privacy laws. For social media posts, please copy the text and paste in the INSERT STATEMENT field."
                return render_template("wrongURL.html", msg = msg)
            elif head != None:
                #score
                load_model = pickle.load(open('final_model.sav', 'rb'))
                prediction = load_model.predict([head])
                prob = load_model.predict_proba([head])

                pred = prediction[0]
                probability = prob[0][1]

                probs = round((probability*100))

                #relatedlinks
                for i in search(head, tld="co.in", num=5, start=1, stop=5, pause=2):
                    if fb in i or mfb in i:
                        continue
                    mylinks.append(str(i))

                return render_template("URLResults.html", links = urlink, rel = mylinks, pred = pred, prob = probs, head =head)

        except requests.ConnectionError as exception:
            msg = "URL does not exist, please make sure to provide a valid URL."
            return render_template("wrongURL.html", msg = msg)

        except requests.exceptions.MissingSchema:
            msg = "URL not detected, please make sure to provide a valid URL."
            return render_template("wrongURL.html", msg = msg)
        


    

#-----------------------------------------------------------FOR URL----------------------------------------------------------------




if __name__ == '__main__': 
    app.run(debug = True)