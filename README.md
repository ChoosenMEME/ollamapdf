# ollama pdf simple

## Installation (Windows):

1. [Python 3.12.4](https://www.python.org/downloads/) Installation
2. Installation von [Ollama](https://ollama.com/)
3. `ollama run llama3`
4. [Windows C++ Build Tools](https://visualstudio.microsoft.com/de/downloads/#build-tools-for-visual-studio-2022] installieren)
5. Ordner für Dateien erstellen
6. In der Konsole zu erstelltem Pfad navigieren (cmd)\
`python -m venv venv`\
`venv\Scripts\activate.bat`\
`pip install ollama langchain langchain_community chromadb pypdf`
7. ollamapdf.py in den Ordner kopieren
8. ollamapdf.py bearbeiten und unter PDF_PATH = "HIER PFAD EINSETZEN" den Pfad zum gewünschten pdf eintragen
9. `python ollamapdf.py`
