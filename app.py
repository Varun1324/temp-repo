from flask import Flask,render_template,request,flash,url_for
import os
from dotenv import load_dotenv
from script import get_data
app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')
os.makedirs('static/images', exist_ok=True)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        img = request.files['file']
        img.save(os.path.join('static/images',img.filename))
        data=get_data(img) #method to script
        flash(f"File {img.filename} uploaded successfully")
        image_url = url_for('static', filename=f'images/{img.filename}')
        return render_template('index.html',image_url=image_url,data=data)
    return render_template('index.html',image_url="https://res.cloudinary.com/durc5ydxo/image/upload/v1720244864/upload-icon_kb99jl.png")

if __name__ == '__main__':
    app.run(debug=False,host=0.0.0.0)
