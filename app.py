from flask import Flask, render_template, request, redirect
from model import solution
import json
import PyPDF2
import io

with open('congig.json', 'r') as f:
  config=json.load(f)

model=config['MODEL_NAME']

app=Flask(__name__)

@app.route('/',methods=['GET'])
def run():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf_file']
    pdf_reader = PyPDF2.PdfReader(file)
    question = request.form.get('text_box')
    a=solution(pdf_reader, question, model)
    #print(a)
    if len(a)>1:
        a=a.split('\n')
    return render_template('upload.html', answer=a)


if __name__ == "__main__":
    app.run(debug=True)

