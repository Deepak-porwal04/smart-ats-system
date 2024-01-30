import os

def get_variable(key):
    """
   Loads the environment variable from the .env file.

   Loads the .env file using the `load_dotenv` function, then retrieves
   the environment variable stored in the .env file.

   Returns:
       env_var_value(str): The environment variable value, or None if the environment variable is not found.
    """
    env_var_value = os.environ.get(key)
    return env_var_value