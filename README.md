# SOP → AI Training System

An AI-powered system that converts SOP (Standard Operating Procedure) documents into structured training content, including summaries, step-by-step instructions, and evaluation quizzes.

---

## Overview

Training employees using SOP documents is often manual and time-consuming.  
This project automates that process by transforming SOPs into:

- ✅ Key summary points  
- ✅ Step-by-step training instructions  
- ✅ Multiple-choice quiz questions  

The system provides a simple interface where users can upload an SOP and instantly generate training-ready content.

---

## Features

- Upload SOP in PDF format  
- Automatic text extraction  
- AI-generated summary  
- Step-by-step training content  
- Auto-generated quiz (MCQs)  
- Download generated outputs  
- Clean and interactive UI (Streamlit)

---

## 🏗️ Architecture
```
                ┌────────────────────┐
                │   SOP Upload UI    │
                └────────┬───────────┘
                         ↓
                ┌────────────────────┐
                │ Text Extraction    │
                │ (PDF → Text)       │
                └────────┬───────────┘
                         ↓
                ┌────────────────────┐
                │ Text Chunking      │
                └────────┬───────────┘
                         ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
 ┌────────────┐ ┌──────────────┐ ┌────────────┐
 │ Summary     │ │ Training     │ │ Quiz        │
 │ Generator   │ │ Generator    │ │ Generator   │
 └────┬────────┘ └────┬─────────┘ └────┬───────┘
      ↓               ↓                ↓
        ┌────────────────────────────┐
        │ Structured Output (JSON)   │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │ Streamlit UI / Export      │
        └────────────────────────────┘

```

---

## Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **LLM/API:** Groq API (LLaMA 3)  
- **PDF Processing:** pdfplumber  
- **Environment Management:** python-dotenv  

---

##  Project Structure
```
sop-ai-training-system/
│
├── app.py                     # Main Streamlit app
├── requirements.txt          # Dependencies
├── .env                      # API key (not pushed to GitHub)
├── README.md                 # Project description
│
├── src/                      # Core logic (clean separation)
    │
    ├── pdf_utils.py          # PDF text extraction
    ├── llm_engine.py         # LLM setup (OpenAI client)
    ├── generators.py         # Summary, training, quiz functions
    └── prompts.py            # All prompts (VERY important for clarity)

```

---
##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/tanyamishra26/sop-ai-training-system.git
cd sop-ai-training-system
```

---

### 2. Create virtual environment

```bash
python -m venv rag_venv
source rag_venv/bin/activate   # Mac/Linux
rag_venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file in root:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the app

```bash
streamlit run app.py
```

---
## Demo

---
## How It Works

1. Upload an SOP document (PDF)
2. The system extracts text using pdfplumber
3. LLM processes the content using structured prompts
4. Outputs are generated:
   - Summary
   - Training Steps
   - Quiz
5. Results are displayed in an interactive UI

---
##  Future Improvements
- Interactive quiz with scoring
- Export to PPT/PDF
- Support for large SOPs using RAG
- Integration with HR/training platforms
---

##  Conclusion

This project demonstrates how AI can transform static SOP documents into interactive training systems, reducing manual effort and improving learning efficiency.

---
##  Author

Tanya Mishra
