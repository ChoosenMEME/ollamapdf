import ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings


PDF_PATH = "HIER PFAD EINSETZEN" #C:/Users/Tim/Desktop

loader = PyPDFLoader(PDF_PATH)
splits = loader.load_and_split()
embeddings = OllamaEmbeddings(model="llama3")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()

while True:
    text = input("\nHier die Fragen zum pdf eingeben: ")
    retrieved_docs = retriever.invoke(text)
    combine_docs = "\n\n".join(doc.page_content for doc in retrieved_docs)
    formatted_prompt = f"Frage: {text}\n\nKontext: {combine_docs}"
    stream = ollama.chat(model='llama3', messages=[
        {'role': 'user',
         'content': 'Du bist ein Pdf-Chatbot und beantwortest Fragen ausschließlich auf Deutsch.' + formatted_prompt}],
        stream=True,
        )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
