import os, io
import random
from flask import Flask, request, jsonify, send_file, abort, render_template
from werkzeug import secure_filename
import functions

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def hello():
    return "bye"

@app.route("/analyse", methods=['POST'])
def analyse():
    data = request.files.get('file', '')
    if data:
        filename = secure_filename(data.filename)
        in_memory_file = io.BytesIO()
        data.save(in_memory_file)
        data = data.read()
        text = ''.join(chr(i) for i in data)
        value = []
        t = text.split("\n")
        t = t[0:len(t)-1]
        for line in t:
            if line:
                value.append(float(line))
        
        return str(len(value))
    else:
        abort(404)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
