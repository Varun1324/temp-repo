from flask import Flask,render_template,request,flash,url_for
import os
from dotenv import load_dotenv
from script import get_data,convert_image_to_base64
app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')
image_url = os.environ.get('DEFAULT_IMAGE_URL')
os.makedirs('static/images', exist_ok=True)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        img = request.files['file']
        #img.save(os.path.join('static/images',img.filename))
        data=get_data(img) #method to script
        flash(f"File {img.filename} uploaded successfully")
        #image_url = url_for('static', filename=f'images/{img.filename}')
        image_base64 = convert_image_to_base64(img)
        image_base64 = "data:image/jpeg;base64,"+image_base64
        return render_template('index.html',image_url=image_base64,data=data)
    return render_template('index.html',image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
