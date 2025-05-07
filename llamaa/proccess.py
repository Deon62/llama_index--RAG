#from loady import *
from loady import documents
from llama_index.core import VectorStoreIndex
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from config import HF_TOKEN
from tqdm import tqdm
from llama_index.core.schema import Document
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.gemini import Gemini
from config import GEMINI_API_KEY
from llama_index.core.evaluation import FaithfulnessEvaluator

db= chromadb.PersistentClient(path="./chroma")
chroma_collection = db.get_or_create_collection("llamaa")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=1000, chunk_overlap=0),
        HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"),
    ],
    vector_store = vector_store
)
print("Processing documents...")
nodes = pipeline.run(documents=(Document(text=doc.get_content()) for doc in documents))

#progress bar
for node in tqdm(nodes):
    print(node)

print(f"Created {len(nodes)} nodes")

#creating index
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex(nodes, embed_model=embed_model, vector_store=vector_store)

#save index
#index.save_to_disk("./index.json")
#querying a vectorestore index with prompts and llms
#as_retriever() ---> to retrieve the most relevant nodes
#as_query_engine() ---> to query the index, for a single answer interactions
#as_chat_engine() ---> to query the index, for a chatbot interaction

llm = Gemini(
    api_key=GEMINI_API_KEY,
    model="gemini-2.0-flash",
    temperature=0.7,
    max_tokens=100,
)

query_engine = index.as_query_engine(
    llm=llm,
    response_mode="compact",
)
query_engine.query("What is the main idea of the document?")
