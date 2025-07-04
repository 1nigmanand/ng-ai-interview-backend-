from dataclasses import dataclass
from typing import List
from omegaconf import DictConfig
import hydra
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AppConfig:
    name: str
    debug: bool
    api_v1_str: str

@dataclass
class ServerConfig:
    host: str
    port: int
    reload: bool

@dataclass
class LoggingConfig:
    level: str
    format: str
    file: str
    rotation: str

@dataclass
class CorsConfig:
    allow_origins: List[str]
    allow_credentials: bool
    allow_methods: List[str]
    allow_headers: List[str]

@dataclass
class Config:
    app: AppConfig
    server: ServerConfig
    logging: LoggingConfig
    cors: CorsConfig

    @classmethod
    def load_config(cls) -> 'Config':
        """Load configuration using Hydra"""
        with hydra.initialize(version_base=None, config_path="../conf"):
            cfg = hydra.compose(config_name="config")

            # Override cors allow_origins from environment variable
            allow_origins_str = os.getenv("CORS_ALLOWED_ORIGINS")
            if allow_origins_str:
                cfg.cors.allow_origins = allow_origins_str.split(',')

            return hydra.utils.instantiate(cfg)