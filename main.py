import cv2

arqCasc = 'C:/Users/di056649/Documents/OpenCV/haarcascade_frontalface_alt_tree.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

webcam = cv2.VideoCapture(0)

while True:
    s, imagem = webcam.read()
    imagem = cv2.flip(imagem, 180)

    faces = faceCascade.detectMultiScale(imagem, minNeighbors=1, minSize=(30, 30), maxSize=(200, 200))

    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite('screenshot.jpg', imagem)

    cv2.imshow('Video', imagem)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
exec(open("DeepFace.py").read())
