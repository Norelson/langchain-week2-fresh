# LangChain Week 5 Project

This is a simple LangChain-powered backend app with a working FastAPI server and client test script.

## 🔧 Features
- `langchain_server.py`: LangChain backend API using FastAPI
- `test_client.py`: Script to send requests and test the backend
- Organized file structure for deployment

## 🚀 Usage

### Run the Server
```bash
python langchain_server.py
## API docs
When the server is running, interactive docs are at:
- `GET /` – serves the UI
- `POST /generate`
- `POST /ask`
- `POST /chat` (Week 7)
- **Docs:** open `http://localhost:8000/docs`
