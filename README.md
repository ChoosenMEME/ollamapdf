# ollama pdf simple

## Installation (Windows):

1. [Python 3.12.4](https://www.python.org/downloads/) Installation
2. Installation von [Ollama](https://ollama.com/)
3. `ollama run llama3`
4. [Windows C++ Build Tools](https://visualstudio.microsoft.com/de/downloads/#build-tools-for-visual-studio-2022) herunterladen
5. `vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools`
6. Ordner für Dateien erstellen
7. In der Konsole zu erstelltem Pfad navigieren (cmd)\
`py -m venv venv`\
`venv\Scripts\activate.bat`\
`pip install ollama langchain langchain_community chromadb pypdf`
8. ollamapdf.py in den Ordner kopieren
9. ollamapdf.py bearbeiten und unter PDF_PATH = "HIER PFAD EINSETZEN" den Pfad zum gewünschten pdf eintragen
10. `python ollamapdf.py`
11. Anweisungen der Konsole folgen
