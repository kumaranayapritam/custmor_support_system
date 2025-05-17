import yaml
import os

def load_config(config_path: str = os.path.join("config", "config.yaml")) -> dict:
    """
    Load configuration from YAML file
    Args:
        config_path: Path to config file
    Returns:
        dict: Configuration dictionary
    """
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_path)
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config