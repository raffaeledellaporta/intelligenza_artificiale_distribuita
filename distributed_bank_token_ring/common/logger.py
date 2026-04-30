import logging

from distributed_bank_token_ring.common.logger_interface import LoggerInterface


class LoggerAdapter(LoggerInterface):
    """
    Inizializza un logger che invia messaggi sulla console.
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger()
        if not self._logger.hasHandlers():  # Controlla se ci sono già degli handler
            self._logger.setLevel(logging.INFO)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
            self._logger.addHandler(console_handler)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str, *, exc_info: bool = False) -> None:
        self._logger.error(message, exc_info=exc_info)

    def exception(self, message: str) -> None:
        self._logger.exception(message)
