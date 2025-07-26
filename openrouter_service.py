# OpenRouter Service for AI Agent MVP
# AI Model API integration via OpenRouter.ai with comprehensive error handling and logging

import os
import logging
import requests
from typing import Optional
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class OpenRouterService:
    """
    OpenRouter service class for AI model interactions via OpenRouter.ai
    Handles API communication, error handling, and response processing
    Supports dynamic model selection with comprehensive logging
    """
    
    def __init__(self):
        """Initialize OpenRouter client with API key from environment"""
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key or self.api_key == "your_openrouter_api_key_here":
            raise ValueError("OpenRouter API key not found. Please set OPENROUTER_API_KEY in .env file")
        
        self.api_endpoint = "https://openrouter.ai/api/v1/chat/completions"
        # Model can be overridden via environment variable for easy switching
        self.model_name = os.getenv("OPENROUTER_MODEL", "qwen/qwen3-coder:free")
        
        # Set up headers for all requests
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        logger.info("OpenRouter service initialized successfully")
        logger.info(f"Using model: {self.model_name}")

    def get_model_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 4000) -> Optional[str]:
        """
        Send prompt to AI model via OpenRouter and get response
        
        Args:
            prompt (str): The prompt to send to the AI model
            temperature (float): The creativity level (default: 0.7)
            max_tokens (int): Maximum tokens for response (default: 4000)
            
        Returns:
            Optional[str]: AI model response content or None if error
        """
        try:
            logger.info(f"Sending request to {self.model_name} via OpenRouter")
            logger.info(f"Prompt length: {len(prompt)} characters")
            
            # Prepare request body according to OpenRouter API specification
            request_body = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            # Send POST request to OpenRouter API
            response = requests.post(
                self.api_endpoint,
                headers=self.headers,
                json=request_body,
                timeout=120  # 2 minutes timeout for large responses
            )
            
            # Check HTTP status code
            if response.status_code != 200:
                logger.error(f"❌ OpenRouter API returned status code: {response.status_code}")
                logger.error(f"Response: {response.text}")
                return None
            
            # Parse JSON response
            response_data = response.json()
            
            # Extract content from response
            if "choices" in response_data and len(response_data["choices"]) > 0:
                content = response_data["choices"][0]["message"]["content"]
                
                logger.info(f"✅ {self.model_name} response received successfully")
                logger.info(f"Response length: {len(content)} characters")
                
                return content
            else:
                logger.error("❌ No choices found in OpenRouter response")
                logger.error(f"Response structure: {response_data}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ HTTP request error: {str(e)}")
            return None
        except requests.exceptions.Timeout:
            logger.error("❌ Request timeout - OpenRouter API took too long to respond")
            return None
        except ValueError as e:
            logger.error(f"❌ JSON parsing error: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"❌ Unexpected error calling OpenRouter API: {str(e)}")
            return None

# Global service instance
openrouter_service = OpenRouterService()

def get_model_response(prompt: str) -> Optional[str]:
    """
    Convenience function to get AI model response via OpenRouter
    
    Args:
        prompt (str): The prompt to send to the AI model
        
    Returns:
        Optional[str]: AI model response content or None if error
    """
    return openrouter_service.get_model_response(prompt) 