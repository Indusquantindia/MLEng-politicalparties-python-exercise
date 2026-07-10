# MLEng Political Parties - UI & Commands Guide

**Project**: MLEng-politicalparties-python-exercise  
**Repository**: https://github.com/Indusquantindia/MLEng-politicalparties-python-exercise.git  
**Branch**: copilot/worktree-2026-07-10T15-20-25

---

## 🚀 Quick Start

### Option 1: Command Line Only (Fastest)
```bash
cd c:\Users\pc\projects\MLEng-politicalparties-python-exercise
.venv\Scripts\activate
.venv\Scripts\python.exe -m pytest tests/test_data_loader.py -v
.venv\Scripts\python.exe test_predictions.py
```

### Option 2: With Streamlit UI (Visual Dashboard)
```bash
cd c:\Users\pc\projects\MLEng-politicalparties-python-exercise
.venv\Scripts\activate
.venv\Scripts\streamlit run src/app/app.py
# Opens at http://localhost:8501
```

### Option 3: With FastAPI (REST API + Interactive Docs)
```bash
cd c:\Users\pc\projects\MLEng-politicalparties-python-exercise\src
.venv\Scripts\activate
.venv\Scripts\uvicorn model-inference-endpoint.main:app --reload
# API runs at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
# Alternative docs at http://localhost:8000/redoc
```

---

## 📋 Complete Setup & Commands

### Phase 1: Environment Setup

```bash
# Navigate to project
cd c:\Users\pc\projects\MLEng-politicalparties-python-exercise

# Create virtual environment
C:/Users/pc/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install all dependencies
.venv\Scripts\python.exe -m pip install -r requirements.txt -q

# Verify installation
.venv\Scripts\python.exe -m pip list
```

---

## 🧪 Testing (Command Line)

### Run All Tests
```bash
.venv\Scripts\python.exe -m pytest tests/ -v
```

### Run Specific Test File
```bash
.venv\Scripts\python.exe -m pytest tests/test_data_loader.py -v
```

### Run with Short Traceback
```bash
.venv\Scripts\python.exe -m pytest tests/test_data_loader.py -v --tb=short
```

### Test Predictions Only
```bash
.venv\Scripts\python.exe test_predictions.py
```

### Quick Functionality Tests
```bash
# Test data loading
.venv\Scripts\python.exe -c "import sys; sys.path.insert(0, 'src'); from text_loader.loader import DataLoader; loader = DataLoader(filepath='data/Tweets.csv'); print(f'Data loaded: {loader.data.shape[0]} tweets')"

# Test text cleaning
.venv\Scripts\python.exe -c "import sys; sys.path.insert(0, 'src'); from text_loader.loader import DataLoader; result = DataLoader.remove_characters('test123!!!'); print(f'Cleaned: {result}')"
```

---

## 🎨 UI Options

### 1️⃣ Streamlit Web App (Visual Interface)

**Start Streamlit:**
```bash
.venv\Scripts\streamlit run src/app/app.py
```

**Access:**
- 🌐 http://localhost:8501
- Automatically opens in your default browser

**Features:**
- Visual text input for predictions
- Interactive data exploration
- Real-time results display
- Responsive design

**Stop:**
Press `Ctrl+C` in terminal or click ❌ in Streamlit interface

---

### 2️⃣ FastAPI REST API (Professional API)

**Start FastAPI Server:**
```bash
cd src
.venv\Scripts\uvicorn model-inference-endpoint.main:app --reload
```

**Access:**
- 📡 API Base: http://localhost:8000
- 📚 Interactive Docs (Swagger): http://localhost:8000/docs
- 📖 Alternative Docs (ReDoc): http://localhost:8000/redoc

**Endpoints:**
```
POST /predict - Make predictions
GET /health - Check API health
GET /docs - View API documentation
```

**Example Request (using curl or Postman):**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

**Features:**
- RESTful API for programmatic access
- Interactive API documentation
- Model serving ready for production
- CORS enabled for web integration

**Stop:**
Press `Ctrl+C` in terminal

---

### 3️⃣ Jupyter Notebook (Exploration)

**Start Jupyter:**
```bash
.venv\Scripts\jupyter notebook
```

**Create New Notebook:**
1. Click "New" → "Python 3"
2. Explore data interactively:
```python
import sys
sys.path.insert(0, 'src')
from text_loader.loader import DataLoader

loader = DataLoader(filepath='data/Tweets.csv')
print(loader.data.head())
```

---

## 🐳 Docker Deployment

### Build & Run with Docker Compose

```bash
cd src
docker-compose build
docker-compose up
```

**Access Services:**
- 🎨 Streamlit: http://localhost:8501
- 📡 FastAPI: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs

**Background Execution:**
```bash
docker-compose up -d
docker-compose logs -f
docker-compose down
```

---

## 📊 Project Structure

```
├── src/
│   ├── text_loader/
│   │   └── loader.py          # DataLoader class for data processing
│   ├── app/
│   │   └── app.py             # Streamlit web interface
│   ├── model-inference-endpoint/
│   │   └── main.py            # FastAPI server
│   └── docker-compose.yml
├── tests/
│   ├── test_data_loader.py    # Unit tests
│   └── test_data_loader_1.py
├── data/
│   └── Tweets.csv             # Sample dataset
├── train.py                   # Model training script
├── test_predictions.py        # Prediction tests
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🎯 Common Workflows

### Workflow 1: Development + Testing
```bash
1. .venv\Scripts\activate
2. Make code changes in src/
3. .venv\Scripts\python.exe -m pytest tests/ -v
4. Fix any failures
5. Repeat steps 2-4
```

### Workflow 2: Quick Demo
```bash
1. .venv\Scripts\activate
2. .venv\Scripts\streamlit run src/app/app.py
3. Interact with web interface at http://localhost:8501
4. Test predictions with sample text
```

### Workflow 3: API Integration
```bash
1. .venv\Scripts\activate
2. cd src
3. .venv\Scripts\uvicorn model-inference-endpoint.main:app --reload
4. Test API at http://localhost:8000/docs
5. Integrate endpoints into your applications
```

### Workflow 4: Production Deployment
```bash
1. cd src
2. docker-compose build
3. docker-compose up -d
4. Services available on ports 8501 (Streamlit) & 8000 (FastAPI)
```

---

## 🛠️ Troubleshooting

### Issue: Virtual environment not activating
```bash
# Recreate it
rmdir /s .venv
C:/Users/pc/AppData/Roaming/uv/python/cpython-3.14.3-windows-x86_64-none/python.exe -m venv .venv
.venv\Scripts\activate
```

### Issue: Port already in use
```bash
# Change port for Streamlit
.venv\Scripts\streamlit run src/app/app.py --server.port 8502

# Change port for FastAPI
cd src
.venv\Scripts\uvicorn model-inference-endpoint.main:app --port 8001 --reload
```

### Issue: Tests not running
```bash
# Install pytest
.venv\Scripts\python.exe -m pip install pytest pytest-mock

# Run tests with verbose output
.venv\Scripts\python.exe -m pytest tests/ -vv
```

---

## 📝 Code Changes Reference

See `CODE_CHANGES.txt` for detailed list of modifications made for production deployment.

---

## 🔗 Quick Links

- 📦 **Repository**: https://github.com/Indusquantindia/MLEng-politicalparties-python-exercise
- 🚀 **Streamlit Docs**: https://docs.streamlit.io
- 🔌 **FastAPI Docs**: https://fastapi.tiangolo.com
- 🧪 **Pytest Docs**: https://docs.pytest.org
- 🐳 **Docker Docs**: https://docs.docker.com

---

## ✅ Checklist for New Team Member

- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install dependencies
- [ ] Run tests (`pytest tests/ -v`)
- [ ] Start Streamlit app (`streamlit run src/app/app.py`)
- [ ] Access web interface at http://localhost:8501
- [ ] Test with sample text
- [ ] Try FastAPI endpoint (`uvicorn model-inference-endpoint.main:app --reload`)
- [ ] Review `CODE_CHANGES.txt` for modifications
- [ ] Deploy with Docker if needed

---

Generated: 2026-07-10  
Maintained by: GitHub Copilot
