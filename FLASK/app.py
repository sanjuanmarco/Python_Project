from flask import Flask, redirect, url_for, render_template, request
import os
import trafilatura 
from lxml import html
from rake_nltk import Rake
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
import operator
import nltk, string

def listToString(s): 

    str1 = " " 
    
    return (str1.join(s))

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]



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
            #take content of the input link
            download = trafilatura.fetch_url(urlink)
            res = trafilatura.extract(download, include_comments=False, 
                include_tables=False, no_fallback=True, output_format='xml')

            a = str(res)

            part = a.partition("h2") #remove strings in h2
            output = part[0]

            mytree = html.fromstring(output) #transforming xml to string
            result = str(trafilatura.process_record(mytree)) #prints main content
        
            r = Rake()
            r.extract_keywords_from_text(result)
            r.get_ranked_phrases()
            result = listToString(r.get_ranked_phrases())

            if twitter in urlink or fb in urlink:
                msg = "Sorry, social media links cannot be accessed due to privacy laws. For social media posts, please copy the text and paste in the INSERT STATEMENT field."
                return render_template("wrongURL.html", msg = msg)
            elif head != None:
                #score
                load_model = pickle.load(open('FLASK\\final_model__.sav', 'rb'))
                prediction = load_model.predict([head])
                prob = load_model.predict_proba([head])

                pred = prediction[0]
                probability = prob[0][1]

                probs = round((probability*100))

                #relatedlinks
                url_article = []
                x = 0
                similarity_score = []
                for i in search(head, tld="co.in", num=5, start=1, stop=5, pause=2):
                    url_content = ""
                    url_article.append(i)

                    if fb in i or twitter in i:
                        continue
                    mylinks.append(str(i))
                    download = trafilatura.fetch_url(url_article[x])
                    res = trafilatura.extract(download, include_comments=False, 
                    include_tables=False, no_fallback=True, output_format='xml')
                    a = str(res)
                    part = a.partition("h2") #remove strings in h2
                    output = part[0]

                    mytree = html.fromstring(output) #transforming xml to string
                    url_content = str(trafilatura.process_record(mytree)) #prints main content

                    #converting it to rake
                    r1 = Rake()
                    r1.extract_keywords_from_text(url_content)
                    r1.get_ranked_phrases()
                    url_content = listToString(r1.get_ranked_phrases())
                    similarity_score.append(float("{:.5f}".format(cosine_sim(result,url_content) *100 )))
                    x = x+1


                return render_template("URLResults.html", links = urlink, rel = mylinks, pred = pred, prob = probs, head = head, sim_score = similarity_score)

            

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
        
        #Extract the important words from the input(statement)
        r = Rake()
        r.extract_keywords_from_text(state)
        r.get_ranked_phrases()
        result = listToString(r.get_ranked_phrases())

        if res < 4:
            msg = "Not enough information, please provide a longer statement."
            return render_template("wrongURL.html", msg = msg)

        else:

            #score
            load_model = pickle.load(open('FLASK\\final_model__.sav', 'rb'))
            prediction = load_model.predict([state])
            prob = load_model.predict_proba([state])

            pred = prediction[0]
            probability = prob[0][1]

            probs = round((probability*100))

            mystate = []

            #relatedlinks
            url_article = []
            x = 0
            similarity_score = []
            for i in search(state, tld="co.in", num=5, start=1, stop=5, pause=2):
                url_article.append(i)
                if fb in i or twitter in i:
                    continue
                mystate.append(str(i))
               

                download = trafilatura.fetch_url(url_article[x])
                res = trafilatura.extract(download, include_comments=False, 
                include_tables=False, no_fallback=True, output_format='xml')
                a = str(res)
                part = a.partition("h2") #remove strings in h2
                output = part[0]

                mytree = html.fromstring(output) #transforming xml to string
                url_content = str(trafilatura.process_record(mytree)) #prints main content

                #converting it to rake
                r1 = Rake()
                r1.extract_keywords_from_text(url_content)
                r1.get_ranked_phrases()
                url_content = listToString(r1.get_ranked_phrases())
                similarity_score.append(float("{:.5f}".format(cosine_sim(result,url_content) *100 )))
                x = x+1

        
            return render_template("StatementResults.html", rel = mystate, state = state, pred = pred, prob = probs,sim_score = similarity_score)

#-----------------------------------------------------------FOR IMAGE----------------------------------------------------------------

app.config["UPLOAD_PATH"] = "F:\\Programming Files\\XAMPP\\htdocs\\GitHub\\Python_Project\\FLASK\\static\\uploads"
@app.route("/ImageResults", methods = ["GET", "POST"])
def user_image():

    import easyocr
    
    
    if request.method == "POST":
        if request.files:

            img = request.files["image_upload"]

            print(img.filename)
            
            img_file = img.save(os.path.join(app.config['UPLOAD_PATH'], img.filename)) #save to local folder

            image = "FLASK\\static\\uploads\\" + img.filename #location to pass in html


            reader = easyocr.Reader(['en'], gpu=False)
            result = reader.readtext(image, detail = 0) 

            result_list = []

            for word in result:
                result_list.append(word)

            sentences = " ".join(result_list)

            #Extract the important words from the input(statement)
            r = Rake()
            r.extract_keywords_from_text(sentences)
            r.get_ranked_phrases()
            result = listToString(r.get_ranked_phrases())

            if (not sentences):
                msg = "No text detected, please check your uploaded image."
                return render_template("wrongURL.html", msg = msg)

            else:
                #score
                load_model = pickle.load(open('FLASK\\final_model__.sav', 'rb'))
                prediction = load_model.predict([sentences])
                prob = load_model.predict_proba([sentences])

                pred = prediction[0]
                probability = prob[0][1]

                probs = round((probability*100))

                mywords = []
                #relatedlinks
                url_article = []
                x = 0
                similarity_score = []
                for i in search(result, tld="co.in", num=5, start=1, stop=5, pause=2):
                    url_article.append(i)
                    if fb in i or twitter in i:
                        continue
                    mywords.append(str(i))
                    
                    download = trafilatura.fetch_url(url_article[x])
                    res = trafilatura.extract(download, include_comments=False, 
                    include_tables=False, no_fallback=True, output_format='xml')
                    a = str(res)
                    part = a.partition("h2") #remove strings in h2
                    output = part[0]

                    mytree = html.fromstring(output) #transforming xml to string
                    url_content = str(trafilatura.process_record(mytree)) #prints main content

                    #converting it to rake
                    r1 = Rake()
                    r1.extract_keywords_from_text(url_content)
                    r1.get_ranked_phrases()
                    url_content = listToString(r1.get_ranked_phrases())
                    similarity_score.append(float("{:.5f}".format(cosine_sim(result,url_content) *100 )))
                    x = x+1
        
                return render_template("ImageResults.html", image = image, sentences = sentences, rel = mywords, pred = pred, prob = probs,sim_score = similarity_score)

if __name__ == '__main__': 
    app.run(debug = True)