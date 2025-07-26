# OpenAI Service for AI Agent MVP
# GPT-4o API integration with comprehensive error handling and logging

import os
import logging
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class OpenAIService:
    """
    OpenAI service class for GPT-4o interactions
    Handles API communication, error handling, and response processing
    """
    
    def __init__(self):
        """Initialize OpenAI client with API key from environment"""
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key or self.api_key == "your_openai_api_key_here":
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in .env file")
        
        self.client = OpenAI(api_key=self.api_key)
        logger.info("OpenAI service initialized successfully")

    def get_gpt_response(self, prompt: str, model: str = "gpt-4o") -> Optional[str]:
        """
        Send prompt to GPT-4o and get response
        
        Args:
            prompt (str): The prompt to send to GPT-4o
            model (str): The model to use (default: gpt-4o)
            
        Returns:
            Optional[str]: GPT-4o response content or None if error
        """
        try:
            logger.info(f"Sending request to {model}")
            logger.info(f"Prompt length: {len(prompt)} characters")
            
            # Send request to OpenAI API
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert software developer and architect. Provide comprehensive, detailed, and well-structured responses in Markdown format."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000,
                temperature=0.7
            )
            
            # Extract content from response
            content = response.choices[0].message.content
            
            logger.info("✅ GPT-4o response received successfully")
            logger.info(f"Response length: {len(content)} characters")
            
            return content
            
        except Exception as e:
            logger.error(f"❌ Error calling OpenAI API: {str(e)}")
            return None

# Global service instance
openai_service = OpenAIService()

def get_gpt_response(prompt: str) -> Optional[str]:
    """
    Convenience function to get GPT-4o response
    
    Args:
        prompt (str): The prompt to send to GPT-4o
        
    Returns:
        Optional[str]: GPT-4o response content or None if error
    """
    return openai_service.get_gpt_response(prompt) 