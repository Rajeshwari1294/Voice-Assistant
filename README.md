Voice-Controlled Assistant

A Python-based voice assistant that listens to your voice commands and performs useful actions like telling jokes, reading news, saving notes, and more.

1.Features

🎤 Voice Input: Speech-to-text conversion for hands-free interaction.

🧠 Command Handling: Supports multiple commands:

"Tell me a joke"
"What is the news"
"Take a note"
"What time is it"
"Open Google"
"Exit"

🔊 Spoken Responses: Uses pyttsx3 for text-to-speech output.
📓 Notes Support: Saves notes to notes.txt automatically.
🛠️ Extensible: Easy to add new commands and modules.

2. Requirements
Python 3.6+

3. Install dependencies:
pip install -r requirements.txt

4. Usage
Run the assistant:
python assistant.py

5. Then say a supported command, for example:

"Tell me a joke"
"What is the news"
"Take a note"
"What time is it"
"Open Google"
"Exit"

6. Project Structure
├── assistant.py       # Main script  
├── requirements.txt   # Dependencies  
├── notes.txt          # Saved voice notes (auto-created)  
└── README.md          # Project info  

Developed by Annamdas Rajeshwari
