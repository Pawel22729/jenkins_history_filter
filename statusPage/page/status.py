from flask import Flask, render_template, request
from modules import getStingray

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status/stingray')
def stingrayStatus():
    data = getStingray.getBuildsHistory()
    return render_template('index.html', data=data)

@app.route('/status/stingray/cache')
def stingrayStatusCache():
    data =  open('/tmp/statusStingrayCache.tmp').readlines()
    return render_template('index.html', data=data)

@app.route('/status/tracker')
def trackerStatus():
    data = getStingray.getBuildsHistory()
    return render_template('index.html', data=data)

@app.route('/status/tracker/cache')
def trackerStatusCache():
    data =  open('/tmp/statusTrackerCache.tmp').readlines()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
