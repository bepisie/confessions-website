# 📝 Confessions Website

Welcome to the **Confessions Website**! This project is a simple web application where users can write anonymous confessions and view confessions submitted by others. It’s built using **Flask** and is designed to be easily hosted on **Pylexnodes**. 😄

## 🌟 Features

- **Home Page**:  
  A simple homepage with two buttons:  
  - **Write a Confession**  
  - **See Confessions**

- **Write Confessions**:  
  Users can write their anonymous confessions, which are saved in a list (or file). 🖊️

- **See Confessions**:  
  A page where users can scroll through all previously submitted confessions. 📜

## 🛠️ How to Run Locally

### 1. Clone the repository:
```bash
git clone https://github.com/bepisie/confessions-website.git
cd confessions-website
```

### 2. Install the required dependencies:
Make sure you have Python installed. Run the following command to install the necessary libraries:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app:
```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000` by default.

## 🚀 Hosting on Pylexnodes

1. Sign in to **Pylexnodes** and create a new project.
2. Upload your `app.py`, `templates/`, `static/` folders, and `requirements.txt`.
3. Start your application, and Pylexnodes will provide you with a live URL!

## 📁 File Structure

```plaintext
confessions-website/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── templates/           # HTML files (index, write, see)
├── static/              # CSS/JS files
└── README.txt           # This file!
```

## 📜 Requirements

- **Python 3.x** 🐍
- **Flask**: Web framework used for the project

## 📝 License

This project is open source! Feel free to modify and share. 🎉

---

Enjoy building and sharing your confessions!
