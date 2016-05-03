import os, io
import random
import numpy as np
from scipy import interpolate
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
     return render_template('index.php')

@app.route("/analyse", methods=['POST'])
def analyse():
    data = request.files.get('file', '')
    if data:
        filename = secure_filename(data.filename)
        in_memory_file = io.BytesIO()
        data.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        text = ''.join(chr(i) for i in data)
        value = []
        t = text.split("\n")
        t = t[0:len(t)-1]
        for line in t:
            if line:
                value.append(float(line))
        result = functions.getAnalysed(value)
        return jsonify({"mean":round(result['mean'],2),"Heart Rate":round(result['Heart Rate'],2),"std_dev":round(result['std_dev'],2),"variance":round(result['variance'],2),"cv":round(result['cv'],2),"std_dev_diff":round(result['std_dev_diff'],2),"rms_diff":round(result['rms_diff'],2)})
    else:
        abort(404)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# and allowed_file(file.filename)
