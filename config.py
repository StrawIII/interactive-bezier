#  DO NOT CHANGE ANYTHING BELOW UNLESS KNOW WHAT YOU ARE DOING!

from pathlib import Path
from typing import Tuple

import tomli
from pydantic import model_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    project_dir: Path = Path(__file__).parent
    user_settings: dict

    @model_validator(mode="before")
    def load_user_settings(cls, values):
        with Path(Path(__file__).parent, "settings.toml").open(mode="rb") as f:
            values["user_settings"] = tomli.load(f)

        return values
