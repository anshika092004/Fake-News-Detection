# <img width="100" height="100" alt="fake-news" src="https://github.com/user-attachments/assets/a9733198-7921-4857-ab09-9a9667e6c283" /> Fake-News-Buster-
A machine learning-based web application that classifies news articles as **Real** or **Fake** using Natural Language Processing techniques.

## 📌 Project Description

This project aims to identify whether a news article is **fake** or **real** by analyzing its textual content. With the rise in misinformation across digital platforms, such a system can help mitigate the spread of fake news by providing a quick credibility check using machine learning.

The project includes:
- Text preprocessing and vectorization (TF-IDF)
- Model training using Logistic Regression
- Evaluation and accuracy measurement
- Deployment using Flask for a user-friendly interface

## 🚀 Features

- Clean and simple UI using HTML/CSS
- Real-time news classification
- Trained on reliable dataset from Kaggle
- Lightweight Flask backend

## 🧠 Algorithms Used

- **TF-IDF Vectorizer** for text feature extraction
- **Logistic Regression** for binary classification
- Performance metrics: Accuracy, Confusion Matrix, Precision, Recall

## 🛠️ Tech Stack

| Area            | Tools/Technologies           |
|-----------------|------------------------------|
| Programming     | Python                       |
| Libraries       | Pandas, NumPy, Scikit-learn, NLTK |
| Web Framework   | Flask                        |
| Frontend        | HTML, CSS                    |
| Deployment      | Localhost (can be hosted on Render/Heroku) |

## 📂 Folder Structure
Fake-News-Detection/
│
├── templates/
│ ├── home.html
│ ├── prediction.html
│ ├── contact.html
│
├── static/
│ ├── style.css
│
├── app.py
├── fake_news_detection.ipynb
├── requirements.txt
└── README.md

## 📊 Dataset

- **Name**: Fake and Real News Dataset  
- **Source**: [Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

## 📷 Screenshots

<img width="956" height="462" alt="image" src="https://github.com/user-attachments/assets/7148ac65-9515-445c-b437-04083181dbae" />
<img width="940" height="456" alt="image" src="https://github.com/user-attachments/assets/b3df0dc5-6a30-4170-8c48-969d9dfb0f88" />
<img width="940" height="455" alt="image" src="https://github.com/user-attachments/assets/e0a53aee-2b78-446f-8d60-c3e1d79cdda2" />
<img width="940" height="650" alt="image" src="https://github.com/user-attachments/assets/4debdfa1-234f-4cab-a3cc-d1e5d1568355" />

## ⚙️ How to Run the Project

1. **Clone the Repository**
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection
2. **Install Requirements**
   pip install -r requirements.txt
3. **Run the App**
   python app.py
4. **Open your browser**
   Visit http://127.0.0.1:5000/ in your browser to use the application.

✅ Future Improvements
- Add multiple ML models for comparison (Random Forest, XGBoost)
- Integrate a web scraper for live news detection
- Host the project online (Render/Heroku)
- Enhance frontend UI/UX

🙋‍♀️ About Me
I’m Anshika Sharma, a B.Tech IT student passionate about AI/ML and real-world applications of data science.
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anshika-sharma-20376125a/)

📄 License
This project is licensed under the MIT License.
