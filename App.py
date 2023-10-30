
import streamlit as st
import cv2
import face_recognition
import pickle

st.title("Face Recognition App")

# Ask user for their name
input_name = st.text_input("Please enter your name:")
"""
It recognizes only three faces:
1. PSX_Ashish
2. Arin
3. Ronak
"""

def authenticate():
    """
    This function takes a picture of the user and compares it with the known faces.
    """
    # take a picture of the user in the app and show it to the user
    with st.spinner("Please wait for the camera to load....."):
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        # convert bgr color to rgb color
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite("unknown.jpg", frame)
        # display the image to the user
        st.image(frame, caption="Your Picture", width = 300)
        video_capture.release()

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
                st.success("The face is authenticated.")
            else:
                st.error("The face is not authenticated.")
            st.success(f"The face is {name}.")

if input_name:  # Check if the name is not empty
    button = st.button("Authenticate")

    if button:
        authenticate()
    
    # Start over
    if st.button("Start Over"):
        st.experimental_rerun()
else:
    st.write("Please enter your name before authenticating.")