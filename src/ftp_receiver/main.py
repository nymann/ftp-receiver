import logging
from pathlib import Path
import sys

from ftp_receiver.config import Config
from ftp_receiver.ftp_client import FTPClient
from ftp_receiver.publisher import KafkaPublisher

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main() -> None:
    config = Config()
    client = FTPClient(config=config)
    publisher = KafkaPublisher(config=config)
    downloaded = filenames(output=config.download.output_dir)
    for filename in sorted(client.list()):
        if filename in downloaded:
            continue
        client.download(filename=filename)
        publisher.publish(filename=filename)


def filenames(output: Path) -> set[str]:
    return {filepath.name for filepath in output.iterdir()}


if __name__ == "__main__":
    main()
