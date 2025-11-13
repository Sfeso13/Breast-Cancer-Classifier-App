# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Balance%20Scale.png" alt="Balance Scale" width="25" height="25" /> Breast Cancer Classifier App

<!-- <div align="center">
<img src="images/app_demo.png" width="600"/>
</div> -->

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

A simple **web-based image classification app** built with **Flask** and **Keras**.  
It allows users to upload an image, processes it with a trained CNN model, and returns the predicted class — all through an intuitive web interface.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bookmark%20Tabs.png" alt="Bookmark Tabs" width="25" height="25" /> Table of Contents

- [About](#-about)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Usage](#-usage)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Film%20Projector.png" alt="Film Projector" width="25" height="25" /> About

This project integrates a **Convolutional Neural Network (CNN)** model, and precisely the VGG19 model (I might change it in the future since this model is kinda overkill for this use case), with a **Flask** backend to classify images in real-time.  
It’s designed as a minimal full-stack machine learning application — a foundation for deploying deep learning models as web services.

### **Key Components:**
- 2 trained **Keras** models (`vgg19.h5` and `sequential_model_cnn.h5`)
- A **Flask API** for serving predictions
- File upload and image preprocessing via **OpenCV** and **NumPy**
- Optional **CORS** setup for cross-origin frontend requests

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Control%20Knobs.png" alt="Control Knobs" width="25" height="25" /> Features

- ✅ Upload any image through a browser or API request  
- ✅ Preprocess image input using OpenCV (resize, normalize, reshape)  
- ✅ Predict class probabilities with trained Keras models  
- ✅ Return results as clean JSON or HTML  
- ✅ Modular and easy to expand for other models or categories  
- ✅ Runs locally with or without GPU (TensorFlow handles fallback)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="25" height="25" /> Project Structure

<details>
  <summary>Click to expand</summary>

  ```
  cnn_app/
  ├── app.py
  ├── models/
  │ ├── sequential_model_cnn.h5
  │ └── vgg19.h5
  ├── templates/
  │ ├── predictions.html
  │ └── index.html
  ├── requirements.txt
  └── README.md
  ```

</details>

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" alt="Gear" width="25" height="25" /> Setup

**NOTE:** This repo uses **Git LFS** to store large model files. Make sure you have Git LFS installed:
1. **Clone the repository**
```bash
git lfs install
git clone https://github.com/Sfeso13/Breast-Cancer-Classification-App.git
```
If you already cloned without LFS:
```bash
git lfs pull
```

2. **Create and activate a virtual environment**
```bash
cd Breast-Cancer-Classification-App
python3 -m venv venv
```
Linux/macos
```bash
source venv/bin/activate
```
or windows
```bash
venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Abacus.png" alt="Abacus" width="25" height="25" /> Usage
1. **Run the app**
```bash
python app.py
```
Now you can visit 
```
http://127.0.0.1:5000
```
And upload an image to get its classification


