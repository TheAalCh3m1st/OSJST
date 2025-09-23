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
        "Create and return default config structure."
        self.config_data = {
            'setup_complete': False,
            'api_keys': {
                'linkedin': {
                    'username': ''.
                    'password': '',
                    'enable': False
                },
                'indeed': {
                    'publisher_id': '',
                    'enable': False
                },
                'glassdoor': {
                    'partner_id': '',
                    'api_key': '',
                    'enable': False
                }
            },
            'search_settings': {
                'daily_Linit': 10,
                'delay_between_requests': 5,
                'default_locations': ['USA', 'Remote'],
                'max_results_per_search': 50
            },
            'output_settings': {
                'format': 'csv',
                'save_directory': 'results',
                'include_salary_data': True,
                'include_company_info': True
            }
        }
        return self.config_data

    def save_config(self) -> bool:
        try:
            self.ensure_config_dir()
            with open(self.config_path, 'w') as file:
                yaml.dump(self.config_data, file,
                          default_flow_style=False, indent=2)

            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def get_api_key(self, service: str, key_type: str = '') -> Optional[str]:
        "Get specific API key or credentials."
        try:
            if key_type:
                return self.config_data['api_keys'][service].get(key_type, '')
            return self.config_data['api_keys'][service]
        except KeyError:
            return None

    def set_api_key(self, service: str, key_data: Dict[str, Any]) -> None:
        "Set API keys for service"
        if 'api_keys' not in self.config_data:
            self.config_data['api_keys'] = {}

        self.config_data['api_keys'][service] = key_data
        self.config_data['api_keys'][service]['enable'] = bool(
            key_data.get('username') or key_data.get(
                'publisher_id') or key_data.get('')
        )

    def is_service_enabled(self, service: str) -> bool:
        "Check if a service is enabled and configured"
        return self.config_data.get('api_keys', {}).get(service, {}).get('enabled', False)

    def mark_setup_complete(self) -> None:
        "Mark initial setup as complete"
        self.config_data['setup_complete'] = True
        self.setup_complete = True


# Utility function for quick config access
def get_config() -> None:
    "Get singleton configuration instance."
    if not hasattr(get_config, 'instance'):
        get_config.instance = APIConfig()
        get_config.instance.load_config()
    return get_config.instance
