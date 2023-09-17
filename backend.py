from flask import Flask, render_template, request
from hotelfinder import HotelFinder

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['text_input']
        hf = HotelFinder(inText=input_text)
        result = hf.getNBestScorers(5)
    return render_template('index.html', result=result, prev=input_text)

if __name__ == '__main__':
    app.run(debug=True)