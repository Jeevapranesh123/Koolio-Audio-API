from flask import *
import os
from lib import File
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return "Call the /upload endpoint to upload a file"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename.split('.')[1] not in ['mp3','wav']:
            return render_template('upload.html',error="Invalid file type")
        f = File.FileUpload()
        data = f.upload(file)
        return render_template('upload.html',data=data)
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2000,debug=True)