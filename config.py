# DO NOT CHANGE ANYTHING BELOW UNLESS YOU KNOW WHAT YOU ARE DOING!

from pathlib import Path

import tomli
from pydantic import ValidationError, model_validator
from pydantic_settings import BaseSettings


class PointSettings(BaseSettings):
    diameter: int
    color: str


class LineSettings(BaseSettings):
    thickness: int
    color: str


class UserSetting(BaseSettings):
    fullscreen: bool
    resolution: list
    framerate: int
    step_count: int
    performance_mode_threshold: int
    background_color: str
    point: PointSettings
    line: LineSettings


class Config(BaseSettings):
    project_dir: Path = Path(__file__).parent
    defaults: UserSetting = UserSetting(
        fullscreen=True,
        resolution=[1280, 720],
        framerate=60,
        step_count=100,
        performance_mode_threshold=4,
        background_color="gray30",
        point=PointSettings(diameter=5, color="white"),
        line=LineSettings(thickness=2, color="white"),
    )
    try:
        user_settings: UserSetting
    except ValidationError:
        # TODO: finish defaut "user_settings" loading
        user_settings: UserSetting = defaults

    @model_validator(mode="before")
    def load_user_settings(cls, values):
        with Path(Path(__file__).parent, "settings.toml").open(mode="rb") as f:
            values["user_settings"] = tomli.load(f)

        return values
