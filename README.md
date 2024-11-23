<img src="./assets/Advanced_Interview_Responder_with_AI.png">

<!-- At first glance, the branding and messaging clearly conveys what to expect -->
<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mouafo-kamgno-keryan-gift-017403292/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mouafokeryan@gmail.com)

You can ask your questions here in my telegram group.

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+_eppACRhjXhlMjE0)
</div>
<br />

# AI Nexus: Your Advanced AI-Powered Interview Assistant

# Introduction

**Advanced_AI-Powered_Interview_Assistant** is a cutting-edge tool designed to transform the way users prepare for and navigate job interviews. In today’s competitive job market, where every detail matters, this advanced AI-powered system gives candidates a significant edge. By leveraging artificial intelligence, it provides contextually accurate, real-time responses based on the user’s resume and interview questions, ensuring they deliver confident and personalized answers.

# The Challenge of Modern Interview Preparation

Preparing for interviews in the digital age has become increasingly complex. Candidates often spend hours researching common questions, crafting tailored responses, and practicing delivery. Despite these efforts, nerves and lack of preparation can lead to awkward moments and missed opportunities during actual interviews. Balancing focus on the interviewer with recalling practiced responses can be especially challenging, creating a gap in effective communication.

# Enter AI Nexus: Your Advanced AI-Powered Interview Assistant

Advanced_Interview_Responder_with_AI addresses these challenges head-on by acting as your 24/7 AI-powered interview coach. It enables candidates to prepare effectively and perform seamlessly in live or mock interviews. With advanced technology and a teleprompter-style interface, it ensures users stay confident and well-prepared in any scenario.


---

## Features

- **Intelligent Interview Response Generation**

Real-time AI-generated answers tailored to the interview questions.

Customizable AI models (OpenAI GPT-4, Google Gemini, Meta LLaMA, and more) for diverse response styles.


- **Speech Recognition Integration**

Vosk speech recognition system for real-time question transcription.

Seamless processing of spoken queries for accurate AI response generation.


- **Teleprompter-Style Display**

Displays responses on a user-friendly teleprompter interface.

Allows users to maintain eye contact while delivering answers with confidence.


- **Resume Parsing for Contextual Answers**

Extracts key details from the user's resume in PDF format.

Enhances response relevance by aligning answers with the candidate’s experience.


- **AI-Powered Personalization**

Adjusts tone and style to fit company culture.

Ensures responses align with job descriptions and expectations.


- **Practice and Control Features**

Keyboard shortcuts(e.g Space bar) for pausing and resuming practice sessions.

Simplified command-line options for seamless interview preparation.

## 🛠️ How It Works

1. **Resume Data Extraction**: The application reads the user's resume and extracts key information to inform the response generation process.
2. **Real-Time Question Transcription**: As the interviewer asks questions, the application listens and transcribes them using speech recognition technology.
3. **Contextual Response Generation**: The AI processes the transcribed questione is displayed on the teleprompter interface, enabling the user to read the answer while engaging with the interviewer.

## 🧩 Installation

[watch my YouTube video on how to setup](https://youtu.be/WN9aiMDKxFw?si=LWV4OSmOn5myTUAU) And detailed explanation.
### 📋 Prerequisites

- [Python 3.12.4 AND ABOVE](https://www.python.org/downloads/) installed on your system
- An [OpenAI API key](https://platform.openai.com/account/api-keys) (replace `"your_openai_api_key_here"` in the code with your actual API key)
### 🔐 Set Up AI Model APIs

#### **OpenAI GPT-4**

1. Sign up at [OpenAI](https://openai.com/) and obtain your API key.
2. Replace `"your_openai_api_key_here"` in the script with your actual API key.

#### **Google Gemini**

1. **Note:** As of my knowledge cutoff in September 2021, Google’s Gemini model details might be updated. Ensure you have access and obtain the necessary API keys or endpoints from [Google Cloud](https://cloud.google.com/).
2. Replace `"your_gemini_api_key_here"` and `"https://gemini-api.google.com/v1/generate"` with the actual API key and endpoint.

#### **Meta LLaMA**

1. Obtain access to **Meta's LLaMA** and set up the API endpoint as per [Meta's documentation](https://ai.facebook.com/blog/large-language-models-llama-meta-ai/).
2. Replace `"http://your_llama_api_endpoint_here"` with your actual LLaMA API endpoint.

#### **Anthropic Claude**

1. Sign up at [Anthropic](https://www.anthropic.com/) and obtain your API key.
2. Replace `"your_anthropic_api_key_here"` and `"https://api.anthropic.com/v1/complete"` with your actual API key and endpoint.

#### **Ollama**

1. Install **Ollama** by following the [Ollama Installation Guide](https://ollama.com/docs/installation).
2. Start the Ollama server to access the API. By default, Ollama runs on `http://localhost:11434`.
3. Replace `"http://localhost:11434/v1/chat/completions"` with your Ollama API endpoint if different.
- Vosk speech recognition model (download from [Vosk Models](https://alphacephei.com/vosk/models)
- Here’s a list of Vosk English speech recognition models and their system requirements:

### 1. **Lightweight English Models**
   - **Model size**: ~50 MB
   - **System requirements**:
     - **RAM**: Minimum 1 GB
     - **CPU**: Mid-range CPU (equivalent to Raspberry Pi or Android devices)
     - **Performance**: Suitable for real-time offline speech recognition on constrained devices【7†source】【8†source】.

### 2. **Large English Models for Quality listening**
   - **Model size**: 1.4 GB to 4.4 GB
   - **System requirements**:
     - **RAM**: 4 GB or more recommended
     - **CPU**: Multi-core processors
     - **Performance**: Designed for server environments with better accuracy but higher resource consumption【8†source】【9†source】.


## 🔧 Configuration

1. Open the `main.py` script in your preferred code editor.
2. Update the API keys and endpoints for each AI model as outlined in the [Installation](#installation) section.
3. Ensure the `vosk_model_path` is correctly set to the location of your downloaded Vosk model.
4. Place your resume in PDF format and update the `resume_path` variable in the `main.py` script to point to your resume file.
5. 
### 📦 Libraries

The application requires the following libraries:

- **Vosk**: For speech recognition
- **PyAudio**: For audio input and processing
- **OpenAI**: For interacting with the OpenAI API
- **PyPDF2**: For reading PDF files
- **Requests**: HTTP requests for API interactions
- **Tkinter**: For creating the GUI (included with Python)
- **Keyboard**: For detecting keyboard events

### 📄 Requirements File

The required libraries and their versions are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
vosk==0.3.45
pyaudio==0.2.14
openai==1.37.1
PyPDF2==3.0.1
keyboard==0.13.5
```

### ▶️ Running the Application

[watch my YouTube video on how to setup](https://youtu.be/WN9aiMDKxFw?si=LWV4OSmOn5myTUAU) and detailed explanation.

You can run the application using one of the following methods:

#### 🔧 Method 1: Using a Virtual Environment

Creating a virtual environment is recommended to manage dependencies separately from your global Python installation.

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Gamingpro237/Advanced_Interview_responder_with_AI.git
   cd Advanced_Interview_responder_with_AI
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Libraries**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Download and Specify the Path for the Vosk Model**.

6. **Run the Application**:

   ```bash
   python main.py
   ```

7. **Deactivate the Virtual Environment** (after you're done):

   ```bash
   deactivate
   ```

#### ⚙️ Method 2: Normal Setup (Without Virtual Environment)

If you prefer to install the dependencies globally without using a virtual environment, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Gamingpro237/Advanced_Interview_responder_with_AI.git
   cd Advanced_Interview_responder_with_AI
   ```

2. **Install the Required Libraries**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download and Specify the Path for the Vosk Model**.

4. **Run the Application**:

   ```bash
   python main.py
   ```
## 🤝 Contributing

Contributions are welcome! Whether it's improving documentation, suggesting new features, or fixing bugs, your input is valuable.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 🩷 Donations
Your donation will support the development of this powerful resource, ensuring that everyone has access to the preparation and tools they need to succeed, regardless of their background. Together, we can help individuals unlock their potential, secure their dream jobs, and build brighter futures. Every contribution brings us closer to transforming lives through technology. Thank you for your support!

[Donate🩷](https://www.paypal.com/donate/?hosted_button_id=HNTPMBU7MDXHS)

## 💼 Applications

The Advanced Interview Responder can be utilized in various scenarios, including:

- **💼 Job Interviews**: Candidates can practice with the AI to prepare for real interviews, receiving tailored answers based on their resumes.
- **💻 Virtual Meetings**: During online meetings or webinars, users can ask questions and get immediate AI-generated responses to enhance their presentations.
- **🎤 Public Speaking**: Individuals can practice speeches and receive feedback on their delivery by reading AI-generated content.
- **🏢 Corporate Training**: New employees can use the tool for onboarding, helping them prepare for real-world interactions and interviews.

## 📝 Conclusion

The Advanced Interview Responder with AI is a valuable tool for anyone looking to enhance their interview skills and communication abilities. By combining AI-generated responses with a teleprompter interface, it provides users with a unique and effective way to prepare for and navigate interviews confidently.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
