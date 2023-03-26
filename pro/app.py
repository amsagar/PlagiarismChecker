from flask import Flask, render_template, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')
@app.route("/mainpag", methods=["POST", "GET"])
def mainpage():
    return render_template('main.html')

@app.route('/txtsim', methods=['GET', 'POST'])
def getdata1():
    content1 = request.form['content1']
    content2 = request.form['content2']
    similarity = SequenceMatcher(None, content1, content2).ratio()
    similarity = similarity * 100
    similarity = int(similarity)
    sim = str(similarity)
    return render_template('main.html', res='RESULT' + ':' + "Your Data Is Measured To Be Nearly " + sim + "% Matchable")


@app.route('/filesim', methods=['GET', 'POST'])
def getdata2():
    content1 = request.form['file1']
    content2 = request.form['file2']
    similarity = SequenceMatcher(None, content1, content2).ratio()
    similarity = similarity * 100
    similarity = int(similarity)
    sim = str(similarity)
    return render_template('main.html', res='RESULT' + ':' + "Your Data Is Measured To Be Nearly " + sim + "% Matchable")

if __name__ == '__main__':
    app.run(debug=True, port=3400)
