"""
YAML configuration management for API keys and settings
Handles firsttime setup with interactive TUI prompts

"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional


class APIConfig:
    "YAML configuration for API keys and settings"

    def __init__(self, config_path: str = "config/settings.yaml"):
        self.config_path = Path(config_path)
        self.config_data: Dict[str, Any] = {}
        self.setup_complete = False

    def ensure_config_dir(self) -> None:
        "Create dir if it does not exist"
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

    def load_config(self) -> Dict[str, Any]:
        "Load configurations from YAML"
        if not self.config_path.exist():
            return self.create_default_config()

        try:
            with open(self.config_path, 'r') as file:
                self.config_data = yaml.safe_load(file) or {}
                self.setup_complete = bool(
                    self.config_data.get('setup_complete', False))
                return self.config_data

        except yaml.YAMLError as e:
            print(f"Error reading config file: {e}")
            return self.create_default_config()

    def create_default_config(self) -> Dict[str, Any]:
