from pathlib import Path

from pydantic import BaseSettings

from ftp_receiver.version import __version__


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DownloadConfig(BaseConfig):
    output_dir: Path


class KafkaConfig(BaseConfig):
    host: str
    port: int

    class Config:
        env_prefix = "kafka_"


class FTPConfig(BaseConfig):
    username: str
    password: str
    host: str
    port: int = 21

    class Config:
        env_prefix = "ftp_"


class Config:
    def __init__(self) -> None:
        self.version = __version__
        self.ftp = FTPConfig()
        self.kafka = KafkaConfig()
        self.download = DownloadConfig()
