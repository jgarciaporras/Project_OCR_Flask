#app.py
import subprocess
from urllib import response
from charset_normalizer import detect
from flask import Flask, flash, request, redirect, url_for, render_template, send_file,make_response , Response 
import urllib.request
import os
from pandas import read_csv
#import sys
from surprise import Prediction
from werkzeug.utils import secure_filename
from utils.general import methods
import csv

 
#TEMPLATE_DIR = os.path.abspath('../templates')
#STATIC_DIR = os.path.abspath('../static')
app = Flask(__name__, template_folder='templates')


 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed prediction below')
        #subprocess.run("ls")
        subprocess.run(['python', 'detect.py', '--source', os.path.join(app.config['UPLOAD_FOLDER'], filename),'--weight','best.pt','--img','416','--save-txt','--save-conf'])
        

        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>', methods=['GET'])
def display_image(filename):
    #print('display_image filename: ' + filename)
    #obj = request.args.get('obj')
        #rint(obj)
    #loc = os.path.join("runs/detect/exp", obj) 
    #print(loc)
    #try:
    #    return render_template('index.html', filename=send_file(os.path.join("runs/detect/exp", obj)))
    #except Exception as e:
    #   return str(e)


    return redirect(url_for('static', filename='runs/detect/exp/' + filename), code=301)


@app.route('/csv')
def download_csv():
    with open("out_csv/cust_ocr5.csv") as fp:
        csv_file = fp.read()
    return Response(
        csv_file,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myfile.csv"})
    #
    #response.headers['Content-Disposition'] = cd 
    #response.mimetype='text/csv'
    #return response
 
if __name__ == "__main__":
    app.run()
