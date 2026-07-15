from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from core.openjarvis.agent import JarvisAgent
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Jarvis AI Employee",
    description="Local AI employee platform",
    version="0.2.0"
)


class ChatRequest(BaseModel):
    """Chat request model with validation."""
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User message for Jarvis"
    )


class ChatResponse(BaseModel):
    """Chat response model."""
    response: str
    status: str = "success"


agent = None


@app.on_event("startup")
async def startup_event():
    """Initialize agent on startup."""
    global agent
    try:
        agent = JarvisAgent()
        logger.info("JarvisAgent initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize JarvisAgent: {e}")
        raise


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Chat with Jarvis AI employee.
    
    Args:
        request: ChatRequest with user message
        
    Returns:
        ChatResponse with AI response
    """
    if not agent:
        raise HTTPException(
            status_code=503,
            detail="Jarvis agent not initialized"
        )
    
    try:
        response = agent.ask(request.message)
        return ChatResponse(response=response, status="success")
    except Exception as e:
        logger.error(f"Error processing chat: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "agent": "initialized" if agent else "not initialized"
    }
