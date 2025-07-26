# Model Configuration for AI Agent MVP
# Easy model switching for OpenRouter.ai

# Current active model
CURRENT_MODEL = "qwen/qwen3-coder:free"

# Available models (for easy switching)
AVAILABLE_MODELS = {
    "qwen": "qwen/qwen3-coder:free",
    "gemini": "google/gemini-2.5-pro-exp-03-25", 
    "claude": "anthropic/claude-3.5-sonnet",
    "gpt": "openai/gpt-4o",
    "llama": "meta-llama/llama-3.1-70b-instruct:free"
}

def get_model_name(model_key: str = None) -> str:
    """Get model name for OpenRouter API"""
    if model_key and model_key in AVAILABLE_MODELS:
        return AVAILABLE_MODELS[model_key]
    return CURRENT_MODEL

# Model-specific settings
MODEL_SETTINGS = {
    "temperature": 0.7,
    "max_tokens": 4000,
    "timeout": 120
} 