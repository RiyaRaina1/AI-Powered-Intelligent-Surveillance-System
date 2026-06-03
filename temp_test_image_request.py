import cv2
import numpy as np
import http.client
import uuid
path = 'temp_test_image.jpg'
img = np.zeros((200,300,3), dtype=np.uint8)
cv2.rectangle(img, (60,40), (120,180), (255,255,255), -1)
cv2.rectangle(img, (180,40), (240,180), (255,255,255), -1)
cv2.imwrite(path, img)
boundary = '----WebKitFormBoundary' + uuid.uuid4().hex
body = []
body.append(f'--{boundary}')
body.append('Content-Disposition: form-data; name="file"; filename="test.jpg"')
body.append('Content-Type: image/jpeg\r\n')
with open(path, 'rb') as f:
    imgdata = f.read()
body_bytes = '\r\n'.join(body).encode('utf-8') + b'\r\n' + imgdata + b'\r\n' + f'--{boundary}--\r\n'.encode('utf-8')
conn = http.client.HTTPConnection('127.0.0.1', 8000, timeout=10)
conn.request('POST', '/api/analyze-image', body_bytes, {
    'Content-Type': f'multipart/form-data; boundary={boundary}',
    'Content-Length': str(len(body_bytes))
})
res = conn.getresponse()
print('status', res.status)
print(res.read().decode('utf-8', 'replace'))
