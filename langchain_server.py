from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import uvicorn

app = FastAPI()

# Set up your chain
llm = llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short poem about {topic}."
)
chain = LLMChain(llm=llm, prompt=prompt)

# Serve frontend
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    return FileResponse("index.html")
from fastapi import Request
from fastapi.responses import JSONResponse

@app.post("/generate")
async def generate_poem(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(content={"error": "Missing topic"}, status_code=400)

    result = chain.run(topic)
    return {"result": result}