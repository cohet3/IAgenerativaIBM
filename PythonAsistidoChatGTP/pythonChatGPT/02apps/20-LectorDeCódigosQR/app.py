from flask import Flask, render_template, Response
import cv2
import threading

app = Flask(__name__)
camera = cv2.VideoCapture(0)

qr_code_data = None
lock = threading.Lock()


def detect_qr_code(frame):
    global qr_code_data
    qr_code_detector = cv2.QRCodeDetector()
    data, bbox, _ = qr_code_detector.detectAndDecode(frame)
    if data:
        with lock:
            qr_code_data = data


def generate_frames():
    global qr_code_data
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            detect_qr_code(frame)
            if qr_code_data:
                cv2.putText(frame, qr_code_data, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)

# Quiero crear un servicio de streaming en vivo usando mi cámara web mediante Flask y OpenCV donde se vea en la página principal la cámara. En caso de que la cámara detecte un código QR quiero mostrar un texto tanto el propio video de forma asíncrona. Es posible que se deba implementar utilizando hilos paralelos.
