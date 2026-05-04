# 🎙 AI Voice Assistant

A modern **Voice Assistant Web App** built using HTML, CSS, Bootstrap, JavaScript, and a *Python Flask backend with OpenAI API.

This assistant can listen to voice commands, respond with speech, and perform tasks like telling time/date, searching the web, and answering queries using AI.

---

## 🚀 Features

### 🎤 Voice Interaction

* Speech recognition using Web Speech API
* Text-to-speech responses

### 🤖 Smart Commands

* Hello → Greeting response
* How are you → Smart reply
* What is your name → Assistant identity
Tell me time → Speaks current time
Tell me date → Speaks today’s date

### 🌐 Web Actions

* **"Search Python tutorials"** → Opens Google search
* **"Open YouTube"** → Opens YouTube
* **"Open Google"** → Opens Google

### 🧠 AI Integration

* Uses OpenAI API for intelligent responses
* Handles unknown queries dynamically

### 💻 UI/UX

* Modern glassmorphism design
* Chat-style interface
* Smooth and responsive layout

---

## 🛠 Tech Stack

**Frontend:**

* HTML5
* CSS3
* Bootstrap 5
* JavaScript (Web Speech API)

**Backend:**

* Python
* Flask
* OpenAI API

---

## 📁 Project Structure

```
voice-assistant/
│
├── index.html        # Frontend UI
├── app.py            # Flask backend
├── README.md         # Project documentation
```



### 2️⃣ Install Dependencies

```bash
pip install flask flask-cors openai
```

---

### 3️⃣ Add OpenAI API Key

In `app.py`, replace:

```python
openai.api_key = "your_api_key_here"
```

---

### 4️⃣ Run Backend Server

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Run Frontend

* Open `index.html` in browser
* Click 🎤 button and start speaking

---

## 📌 Example Commands

Try speaking:

* "Hello"
* "What is your name"
* "Tell me time"
* "Tell me date"
* "Search Python tutorials"
* "Open YouTube"

---

## ⚠️ Important Notes

* Works best in **Google Chrome** (Web Speech API support)
* Requires **internet connection**
* Backend must be running before using frontend
* Keep your API key secure (do NOT upload to GitHub)

---

## 🔮 Future Improvements

* Wake word detection ("Hey Assistant")
* Mobile app version
* Dark/light mode toggle
* Voice waveform animation
* Integration with APIs (weather, news, maps)

---

## 👨‍💻 Author

**Nilesh Wagh**

