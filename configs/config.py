import os
from pathlib import Path

import toml

PROFILE_ENVIRON = "PROFILE"


def load_config():
    profile = "local"
    if env := os.environ.get(PROFILE_ENVIRON):
        profile = env

    cfg_dir = Path(__file__).parent
    config_path = cfg_dir / f"{profile}.toml"
    return toml.load(config_path)


CONFIG = load_config()
