# AI Blog Generation

A full-stack application designed to generate, edit, and export SEO-optimized blog posts using Artificial Intelligence.

## 🚀 Features

- **AI Generation**: Generate blog content based on title, tone, and language.
- **Rich Editor**: Full featured CKEditor 5 for fine-tuning your content.
- **Image Sidebar**: image suggestions from Unsplash and Pexels.
- **Multi-Format Export**:
  - **PDF**: Professional rendering with `xhtml2pdf`.
  - **Word (DOCX)**: Native document format via `python-docx` and `htmldocx`.
  - **Markdown**: Clean text format for developers.
  - **HTML**: Standard web format.
- **Copy to Clipboard**: Quick sharing of your generated content.

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **AI Orchestration**: LangChain, OpenAI
- **PDF/Docx Processing**: xhtml2pdf, python-docx, BeautifulSoup4
- **API Styling**: RESTful architecture

### Frontend
- **Framework**: React.js (Vite)
- **Styling**: Tailwind CSS
- **Editor**: CKEditor 5
- **Icons/UI**: Custom modern components

## 🏁 Getting Started

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```