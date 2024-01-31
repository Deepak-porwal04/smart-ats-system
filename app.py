from src import generative_model
from src.views import create_app_ui

generative_model.configure_gemini()

if __name__ == "__main__":
    create_app_ui()