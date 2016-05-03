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

@app.route("/fft", methods=['POST'])
def fft():
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
        peak = []
        peak = functions.peaks(value)
        peaks = []
        peaks.append(0)
        for i in peak[1:len(peak)-1]:
            peaks.append(i)
        arrPeak = []
        arrPeak = functions.diffarr(peak)
        arrPeaks = []
        arrPeaks.append(peak[2]-peak[1])
        for i in arrPeak[1:len(arrPeak)-1]:
            arrPeaks.append(i)
        for i in range(len(peaks)):
            peaks[i] = peaks[i]/500
        inter = []
        i=peaks[0]
        while i <= peaks[len(peaks)-1]:
            inter.append(i)
            i = i+0.25
        k=0
        for i in inter:
            if i == peaks[k]:
                inter.remove(i)
                k = k+1
        arr_inerpolate = []
        #arr_interpolate = interpolate.spline(peaks,arrPeaks,inter,order=3,kind='smoothest',conds=None)
        #ps = np.abs(np.fft.fft(arr_interpolate))**2
        time_step = 1/4
        #freqs = np.fft.fftfreq(arr_interpolate.size,time_step)
        #idx = np.argsort(freqs)
        return str([len(peaks),len(arrPeaks)])  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# and allowed_file(file.filename)
