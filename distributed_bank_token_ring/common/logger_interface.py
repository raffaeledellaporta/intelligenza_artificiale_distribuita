from abc import ABC, abstractmethod


class LoggerInterface(ABC):

    @abstractmethod
    def info(self, message: str) -> None: ...

    @abstractmethod
    def debug(self, message: str) -> None: ...

    @abstractmethod
    def warning(self, message: str) -> None: ...

    @abstractmethod
    def error(self, message: str, *, exc_info: bool = False) -> None: ...

    @abstractmethod
    def exception(self, message: str) -> None: ...
