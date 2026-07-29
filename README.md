# Emotion Detection Web Application

## Overview

The Emotion Detection Web Application is a Python Flask application that analyzes text entered by a user and estimates the emotions expressed in that text. The application processes user input, determines the dominant emotion, and displays the results through a simple web interface.

## Features

* Analyze emotions from user-entered text
* Detect the following emotions:

  * Joy
  * Anger
  * Fear
  * Sadness
  * Disgust
* Display the dominant emotion
* Handle invalid or blank input
* Simple web interface built with HTML, CSS, and JavaScript
* Unit tested using Python's testing framework

## Technologies Used

* Python 3
* Flask
* Requests
* HTML5
* CSS3
* JavaScript

## Project Structure

```text
emotion-detection-app/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/emotion-detection-app.git
```

2. Navigate to the project folder:

```bash
cd emotion-detection-app
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python server.py
```

Open your browser and visit:

```text
http://localhost:5000
```

## Running the Unit Tests

```bash
python -m unittest test_emotion_detection.py
```

## Future Improvements

* Integrate a machine learning emotion analysis model
* Improve emotion detection accuracy
* Add support for multiple languages
* Display confidence scores visually
* Store previous analyses in a database

## Author

Jodie Solomons

## License

This project is provided for educational purposes.
