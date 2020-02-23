import logging
import speech_recognition as sr
import sys

from flask import Flask, render_template, request

app = Flask(__name__) #template_folder='C:\Users\sdimos\comp110-17f\UmLikeApp\templates'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/record')
def record():
    render_template("index.html")
    filename = input("Enter your text file name: ")

    r1 = sr.Recognizer()
    r1.energy_threshold = 2000
    r1.pause_threshold = 3

    print ("Say something!")

    while True:
        with sr.Microphone() as source:
            audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
            print(text)
        except:
            print("Could not dictate.")
            sys.exit()
        
    print("Done!")
    file = open("textfiles/" + filename, "a+")
    file.write(text)
    likeCount = countLikes(text)
    print("You said 'like' " + str(likeCount) + " times!")
    return 'hello world'

def countLikes(text):
    count = 0
    words = text.split(" ")
    for w in words:
        w = w.lower()
        if (w == "like"):
            count += 1
    return count

def commonWords(text):
    map = dict()
    count = 0
    words = text.split(" ")
    for w in words:
        map.update({w: ++count})
    for key in map:
        print(key, '->', map[key])


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)


