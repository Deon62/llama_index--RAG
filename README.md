

````markdown
# 🔍 Gemini-Powered RAG Pipeline using LlamaIndex, ChromaDB & HuggingFace

This project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline powered by **Google Gemini**, using **LlamaIndex** as the orchestration layer, **ChromaDB** for vector storage, and **HuggingFace embeddings** for dense semantic retrieval.

📂 **Input**: A local directory of PDF documents  
🧠 **Output**: Compact, LLM-generated answers to user queries  
🛠️ **Evaluation**: Automated response faithfulness evaluation using LlamaIndex's built-in tools

---

## 🚀 Features

- ✅ **Document Loading** via `SimpleDirectoryReader`
- ✂️ **Preprocessing & Chunking** with `SentenceSplitter`
- 🧬 **Semantic Embeddings** using `BAAI/bge-small-en-v1.5` via HuggingFace
- 🧠 **Indexing** with `ChromaVectorStore` for fast dense retrieval
- 🤖 **Query Answering** with Google **Gemini-Pro** or **Gemini 2.0 Flash**
- 🧪 **Faithfulness Evaluation** using `FaithfulnessEvaluator`
- 🔄 **Modular Design** using `IngestionPipeline` and persistent vector store

---

## 📁 Project Structure

```bash
llamaindex-gemini-rag/
│
├── config.py                  # Contains GEMINI_API_KEY and HF_TOKEN
├── proccess.py               # Vector indexing, embedding, and Gemini setup
├── loady.py                 # Loads PDFs from specified folder
├── evals.py              # Evaluates the quality of LLM response
├── /Pdfs/                    # Directory containing the raw PDF documents
├── /chroma/                  # Persistent ChromaDB vector storage
└── README.md                 # You are here
````

---

## 📚 How It Works

1. **Load Documents**
   PDFs are loaded from a directory using `SimpleDirectoryReader`.

2. **Preprocessing Pipeline**
   Documents are split into manageable chunks (tokens), embedded via a HuggingFace transformer, and stored in a Chroma vector DB.

3. **Index Creation**
   `VectorStoreIndex` is created and saved, allowing fast and semantic RAG lookups.

4. **Query Engine with Gemini**
   Gemini LLM is integrated with LlamaIndex as the response engine for query handling.

5. **Response Evaluation**
   Generated answers are evaluated using `FaithfulnessEvaluator` to assess alignment with source documents.

---

## 📦 Dependencies

Install the required packages:

```bash
pip install llama-index==0.12.34
pip install chromadb
pip install huggingface-hub
pip install google-generativeai
```

Make sure you have:

* Google Gemini API Key → `GEMINI_API_KEY`
* HuggingFace Token → `HF_TOKEN`

---

## 🧪 Example Usage

**Load and index documents:**

```bash
python loady.py
python proccess.py
```

**Evaluate the LLM response:**

```bash
python evals.py
```

---

## 📈 Future Improvements

* Add streaming support and conversational memory
* Integrate custom document schemas
* Fine-tune retrieval thresholds and evaluation metrics
* Add OpenAI and Mistral backends for comparison

---

## 🧠 Why This Matters

This project showcases a real-world, production-style RAG pipeline using next-gen LLMs, enabling enterprises or researchers to build intelligent systems that understand domain-specific data.

---

## 🔐 License

This project is licensed under the MIT License.

```


