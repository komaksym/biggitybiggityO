from dotenv import load_dotenv
import os
import mlflow


def setup_mlflow():
    # To not hang for an hour if no connection could be established
    mlflow.environment_variables.MLFLOW_HTTP_REQUEST_TIMEOUT = 10

    # Fetch secrets from .env
    load_dotenv()

    username = os.getenv("MLFLOW_NGROK_USERNAME")
    password = os.getenv("MLFLOW_NGROK_PASSWORD")
    uri = os.getenv("MLFLOW_NGROK_URI")

    # Connect
    mlflow.set_tracking_uri(f"https://{username}:{password}@{uri}")

    # Name the experiment
    mlflow.set_experiment("QLoRA Base vs QLoRA it vs prompt tuning")
