from flask import Flask, render_template, Response
from Cam import Camera
import time
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return render_template('index.html')

def gen(camera):
    print('gen')
    
    frames = camera.get_frame()
    for frame in frames:
        #print(frame)
        #cv2.imshow("img",frame)
        try:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.013)   
        except:
            continue

@app.route('/video_feed')
def video_feed():
    print('video_feed')
    return Response(gen(ca),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    ca=Camera()
    app.run(host='0.0.0.0', debug=True,threaded=True)