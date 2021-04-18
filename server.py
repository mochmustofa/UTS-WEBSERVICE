from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/api/test', methods=['POST'])
def test():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    response = {'message': 'image received. size={}{}'.format(img.shape[1], img.shape[0])}
    response_picked = jsonpickle.encode(response)

    return Response(response=response_picked, status=200, mimetype="application/json")


app.run(host="0.0.0.0", port=5000);