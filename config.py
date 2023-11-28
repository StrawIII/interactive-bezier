from pydantic_settings import BaseSettings
from pathlib import Path


class Config(BaseSettings):
    project_dir: Path = Path(__file__).parent