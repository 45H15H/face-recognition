## Face Recognition App
#####  This is a face recognition app that authenticates the user using face recognition and then displays the user's details.

## Demo Link
If you have a working demo of the project, provide the link so that readers can see your project in action.

## Table of Contents

- [Libraries Used](#libraries-used)
- [Setup](#setup)
- [Project Status](#project-status)
- [Contact](#contact)

## Libraries Used

- face-recognition - version 1.3.0
- opencv-python - version 4.8.1.78

## Setup

- Clone the repository and install the required libraries using `pip3 install -r requirements.txt`
- Create a folder of known faces and add the images of the people you want to recognize.
- In face_encoding.py file, change the path of the known faces folder.
```diff
-- folder_path = r"D:\face-recognition\face-recognition\known_faces"
++ folder_path = r"your path"
```
- Run the face_encoding.py file using `python face_encoding.py`. This will create a pickle file of the known faces containing their encodings.
- In App.py file, change the path of the pickle file.
```diff
-- with open(r"D:\face-recognition\face-recognition\known_faces_encodings.pkl", "rb") as f:
++ with open(r"your path", "rb") as f:
```
- Run the app.py file using `streamlit run app.py`

## Project Status 

Project is: _completed_

## Contact

Created by [Ashish Singh](https://www.linkedin.com/in/45h15h/) - feel free to contact me!
