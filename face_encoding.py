import pickle
import face_recognition
import os

folder_path = r"D:\face-recognition\face-recognition\known_faces"
file_names = os.listdir(folder_path)

known_faces = {}

for i in file_names:
    image = face_recognition.load_image_file(folder_path + "\\" + i)
    name = i.split(".")[0]
    encoding = face_recognition.face_encodings(image)[0]
    known_faces[name] = encoding

with open("known_faces_encodings.pkl", "wb") as f:
    pickle.dump(known_faces, f)
