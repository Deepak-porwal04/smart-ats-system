from configuration.config import get_variable
from constants.constant import MODEL_TEMPRATURE
import google.generativeai as genai
def configure_gemini():
    """
    Initializes the Gemini generative model with the appropriate API key.

    1. Retrieves the API key securely from the environment variables.
    2. Configures the generativeai library with the retrieved API key.

    Raises:
        ValueError: If the API key is not available.
    """
    genai.configure(api_key=get_variable("API_KEY"))

def get_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input, generation_config=genai.types.GenerationConfig(temperature=MODEL_TEMPRATURE))
    return response.text