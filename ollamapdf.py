# Bibliotheken importieren
# KI-Modell Bibliothek importieren
import ollama
# PDF-Loader Bibliothek importieren
from langchain_community.document_loaders import PyPDFLoader
# ChromaDB Vektordatenbank Bibliothek importieren
from langchain_community.vectorstores import Chroma
# Ollama-Embeddings Bibliothek importieren
from langchain_community.embeddings import OllamaEmbeddings

# Pfad zu Datei setzen
# mit / statt mit \ z.B. "C:/Users/test/Desktop/test.pdf"
PDF_PATH = "HIER PFAD EINSETZEN"
# Heruntergeladenes Model auswählen
MODEL = 'llama3'

# PDF-Datei laden
loader = PyPDFLoader(PDF_PATH)
# PDF-Datei in Abschnitte aufteilen
splits = loader.load_and_split()
# Ollama-Embeddings laden
embeddings = OllamaEmbeddings(model=MODEL)
# aufgeteilte Pdf Inhalte anhand von Originalem Embedding in Vektoren umwandeln Vektordatenbank speichern
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
# Vektordatenbank als Retriever speichern
retriever = vectorstore.as_retriever()

# Solange auf Fragen warten und diese beantworten bis Programm beendet wird
while True:
    # Benutzerfrage eingeben
    text = input("\nHier die Fragen zum pdf eingeben: ")
    # Antworten in Vektordatenbank suchen (Seiten und Abschnitte)
    retrieved_docs = retriever.invoke(text)
    # Mögliche Antwort Vektoren kombinieren
    combine_docs = "\n\n".join(doc.page_content for doc in retrieved_docs)
    # Kontext/Antwortmöglichkeiten für die Frage erstellen (Frage: ... Kontext/Antwortmöglichkeiten: ...)
    formatted_prompt = f"Frage: {text}\n\nKontext: {combine_docs}"
    # Sprachmodell starten und vorher generierte (Frage: ... Kontext/Antwortmöglichkeiten: ...) als Eingabe verwenden
    stream = ollama.chat(model=MODEL, messages=[
        {'role': 'user',
         'content': 'Du bist ein Pdf-Chatbot und antwortest ausschließlich auf Deutsch.' + formatted_prompt}],
                         # antwort nach und nach generieren
                         stream=True,
                         )
    print("Antwort:\n")
    # Antwort nach und nach ausgeben
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
