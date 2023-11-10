
import streamlit as st
import cv2
import face_recognition
import pickle
import numpy as np

st.title(":violet[Face Recognition App]")

st.divider()

# Ask user for their name
st.text("Please enter your name to authenticate")
input_name = st.text_input("Name", label_visibility="collapsed" )

st.text("Take a picture to authenticate")
img_file_buffer = st.camera_input("Take a picture", disabled=not input_name, label_visibility="collapsed")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("unknown.jpg", cv2_img)

# load the known faces saved
with open(r"D:\face-recognition\face-recognition\known_faces_encodings.pkl", "rb") as f:
    known_faces = pickle.load(f)

# assosiate the known names with the known encodings
known_names = list(known_faces.keys())
known_faces = list(known_faces.values())
# load the image taken from the webcam
unknown_image = face_recognition.load_image_file("unknown.jpg")
# find the face encodings for the unknown image
unknown_face_encodings = face_recognition.face_encodings(unknown_image)
# consider only one face in the image
if len(unknown_face_encodings) > 1:
    st.error("Multiple faces found in the image. Please upload an image with only one face.")
elif len(unknown_face_encodings) == 0:
    st.error("No faces found in the image. Please upload an image with a face.")
else:
    # find the distance between the unknown face and all the known faces
    face_distances = face_recognition.face_distance(known_faces, unknown_face_encodings[0])
    # find the face with the minimum distance
    min_distance = min(face_distances)
    min_distance_index = face_distances.argmin()
    # if the minimum distance is greater than 0.6, consider it as unknown face
    if min_distance > 0.6:
        st.error("The face is not in the database. Please try with another image.")
    else:
        # get the name corrosponding to the face
        name = known_names[min_distance_index]
        # display the name
        if name == input_name:
            st.success("The face is authenticated", icon = "✅")
        else:
            st.warning("Enter a name to authenticate", icon = "⚠️")
        st.success(f"The face is {name}.")