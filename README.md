# AI Health Buddy 🏥🤖

**Your Personal AI Health Assistant** - A full-stack web application that uses cutting-edge AI to help users interact with their health documents and get personalized health insights.

## 🚀 Features

- **📄 PDF Upload & Analysis**: Upload medical reports and health documents
- **🤖 Document Q&A**: Ask questions about your uploaded health documents
- **💡 AI Health Recommendations**: Get personalized health advice based on your documents
- **🏃‍♂️ Fitness Planning**: Custom workout routines tailored to your health profile
- **🥗 Meal Planning**: Personalized diet plans considering health conditions
- **🔍 Semantic Search**: Advanced vector-based document search
- **📊 Health Profile Extraction**: Automatically extract key health info from documents

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **ChromaDB** - Vector database for document embeddings
- **Google Generative AI (Gemini)** - LLM for text generation and embeddings
- **LangChain** - Text processing and chunking
- **PyPDF** - PDF text extraction

### Frontend
- **React** - User interface library
- **JavaScript** - Frontend logic

### AI & ML
- **RAG (Retrieval-Augmented Generation)** - Context-aware AI responses
- **Vector Embeddings** - Semantic document search
- **Agentic Workflows** - AI agents for health recommendations

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **Node.js 14+**
- **npm** or **yarn**
- **Git**

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lokesh1028/healthagent1.git
cd healthagent1
```

### 2. Backend Setup

#### Open Terminal 1 - Navigate to Backend Directory
```bash
cd backend
```

#### Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables
1. Create a `.env` file in the `backend` directory:
```bash
touch .env
```

2. Add the following configuration to `.env`:
```env
# Google AI API Key - Get from https://aistudio.google.com/app/apikey
GOOGLE_API_KEY=your_google_api_key_here

# ChromaDB Configuration
CHROMADB_PATH=./vector_db
COLLECTION_NAME=pdf_documents

# Text Chunking Configuration
CHUNK_SIZE=1000
CHUNK_OVERLAP=100

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
LOG_LEVEL=INFO
```

3. **Important**: Replace `your_google_api_key_here` with your actual Google AI API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

#### Start the Backend Server
```bash
python main.py
```

✅ **Backend server will start at `http://localhost:8000`**

You should see output like:
```
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     ChromaDB initialized at ./vector_db
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 3. Frontend Setup

#### Open Terminal 2 - Navigate to Frontend Directory
**Keep the backend terminal running and open a NEW terminal window/tab**

```bash
# Navigate to the project root first
cd healthagent1

# Then go to frontend directory
cd healthbud
```

#### Install Node.js Dependencies
```bash
npm install
```

#### Start the Frontend Development Server
```bash
npm start
```

✅ **Frontend will start at `http://localhost:3000` and automatically open in your browser**

You should see output like:
```
Compiled successfully!

You can now view healthbud in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

## 🎯 Quick Start Commands

### Terminal 1 (Backend):
```bash
cd healthagent1/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
# Add your Google API key to .env file
python main.py
```

### Terminal 2 (Frontend):
```bash
cd healthagent1/healthbud
npm install
npm start
```

## 🎯 Usage

### 1. Upload Health Documents
- Click on "📤 Upload & Process PDF" button
- Select your medical reports, lab results, or health documents (PDF format only)
- Wait for the document to be processed and vectorized
- You'll see a success message when processing is complete

### 2. Fill Your Health Profile
- Complete the "Your Profile & Goals" section
- Add your age, fitness level, health conditions, goals, and food preferences
- This information helps provide personalized recommendations

### 3. Ask Questions About Your Documents
- Use the "📚 Document Q&A" feature
- Type questions like:
  - "What is my cholesterol level?"
  - "Are there any concerning values in my blood test?"
  - "What medications am I currently taking?"
  - "Summarize my recent lab results"

### 4. Get AI Health Recommendations
- Click "💡 Get Health Recommendations"
- Receive personalized health advice based on your uploaded documents and profile

### 5. Create Fitness Plans
- Click "🏃‍♂️ Create Fitness Plan"
- Get a customized workout routine based on your goals and fitness level

### 6. Plan Your Meals
- Click "🥗 Create Meal Plan"
- Receive personalized meal plans considering your health conditions and preferences

### 7. Search Health Information
- Use "🌐 Health Knowledge Search"
- Search for general health information, exercises, recipes, etc.

## 🔍 API Endpoints

The backend provides the following key endpoints:

- `POST /upload-pdf/` - Upload and process PDF documents
- `GET /ask/` - Ask questions about uploaded documents
- `POST /recommendation-agent/` - Get AI health recommendations
- `POST /create-fitness-plan/` - Generate fitness plans
- `POST /meal-planner/` - Create meal plans
- `GET /documents/` - List all uploaded documents
- `DELETE /delete-document/` - Delete specific documents
- `GET /extract-profile/` - Extract profile info from documents
- `GET /status/` - Check system status
- `GET /health/` - Health check endpoint

## 🌐 Live Demo

- **Frontend**: https://healthagentf.vercel.app/
- **Backend API**: https://healthagent1.vercel.app/

## 🚀 Deployment

### Frontend Deployment (Vercel)
```bash
cd healthbud
npm run build
npx vercel --prod
```

### Backend Deployment (Railway/Vercel)
The app includes configuration files for easy deployment:
- `Dockerfile` for containerized deployment
- `vercel.json` for Vercel serverless deployment
- `railway.json` for Railway deployment

## 🔐 Security & Privacy

- **Data Security**: Documents are processed locally and stored in your ChromaDB instance
- **API Keys**: Keep your Google AI API key secure in environment variables
- **Medical Disclaimer**: This app provides general health information and is not a substitute for professional medical advice

## ⚠️ Important Notes

1. **Google AI API Key**: You must obtain a valid API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **Medical Disclaimer**: This application is for informational purposes only and should not replace professional medical advice
3. **Data Privacy**: Your health documents are processed locally and not shared with third parties
4. **File Format**: Only PDF files are supported for document upload
5. **Internet Connection**: Required for AI processing and web search features

## 🆘 Troubleshooting

### Common Issues:

1. **"Google API key not configured"**
   - Ensure your `.env` file has the correct `GOOGLE_API_KEY`
   - Verify the API key is valid and has proper permissions
   - Restart the backend server after adding the key

2. **"Failed to fetch" errors**
   - Check that both frontend (port 3000) and backend (port 8000) servers are running
   - Verify CORS configuration in backend
   - Check browser console for detailed error messages

3. **PDF upload issues**
   - Ensure PDF files are not password-protected or corrupted
   - Check file size (large files may take longer to process)
   - Only PDF format is supported

4. **ChromaDB initialization errors**
   - Check write permissions in the backend directory
   - Ensure sufficient disk space
   - Delete `vector_db` folder and restart if corrupted

5. **Port already in use**
   - If port 8000 or 3000 is busy, kill existing processes:
   ```bash
   # Kill process on port 8000
   lsof -ti:8000 | xargs kill -9
   
   # Kill process on port 3000
   lsof -ti:3000 | xargs kill -9
   ```

### Getting Help:

- Check the backend logs for detailed error messages
- Ensure all dependencies are properly installed
- Verify environment variables are correctly set
- Check network connectivity for AI API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 📞 Contact

For questions, issues, or collaboration:
- **GitHub**: https://github.com/Lokesh1028/healthagent1

---

**🎉 Happy Health Tracking with AI Health Buddy!** 

*Empowering individuals to take control of their health journey through AI-powered insights.*


---

**Made with ❤️ using FastAPI, React, and Google AI**
