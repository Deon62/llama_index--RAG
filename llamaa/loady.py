from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.llms.gemini import Gemini
from config import GEMINI_API_KEY

reader = SimpleDirectoryReader(input_dir=r"C:\Users\ALEMAX CYBER\Desktop\HF\Pdfs")
print("Loading documents...")
documents = reader.load_data()

print(f"Found {len(documents)} documents")
