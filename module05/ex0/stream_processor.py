from typing import Any, List, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self) -> str:
        pass

    @abstractmethod
    def format_output(self) -> str:
        pass


class NumericProcessor(DataProcessor):

    def process(self, data: List[int]) -> str:
        self.data = data
        return f"Processing data: {data}"

    def validate(self, data: Optional[Any] = None) -> str:
        return "Validation: Numeric data verified"

    def format_output(self, data: Optional[Any] = None) -> str:
        total = sum(self.data)
        avg = total / len(self.data)
        return (
            f"Processed {len(self.data)} numeric values,"
            f"sum={total}, avg={avg}"
        )


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        self.data = data
        return f"Proocessing data: {data}"

    def validate(self, data: Optional[Any] = None) -> str:
        return "Validation: Text data verified"

    def format_output(self, data: Optional[Any] = None) -> str:
        chars = len(self.data)
        words = len(self.data.split())
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        print(f'Processing data: {data}')
        super().process(data)
        self.data: str = data

    def validate(self, data: Optional[Any] = None) -> None:
        print("Validation: Log entry verified")

    def format_output(self, data: Optional[Any] = None) -> str:
        level: str = "INFO"
        level1: str = "INFO"
        msg: str = self.data
        if "ERROR" in self.data:
            level = "ALERT"
            level1: str = "ERROR"
            msg = self.data.replace("ERROR: ", "")
        elif "INFO" in self.data:
            level = "INFO"
            level1 = "INFO"
            msg = self.data.replace("INFO: ", "")
        return f'[{level}] {level1} level detected: {msg}'


def data_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("Initializing Numeric Processor...")
    numeric.process([1, 2, 3, 4, 5])
    numeric.validate()
    print("Output:", numeric.format_output())
    print()

    print("Initializing Text Processor...")
    text.process("Hello Nexus World")
    text.validate()
    print("Output:", text.format_output())
    print()

    print("Initializing Log Processor...")
    log.process("ERROR: Connection timeout")
    log.validate()
    print("Output:", log.format_output())
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    numeric_data = [1, 2, 3]
    text_data = "System ready"
    log_data = "INFO: System ready"

    try:
        processors[0].process(numeric_data)
        processors[0].validate()
        print("Result 1:", processors[0].format_output())
    except Exception:
        print("Error processing numeric data")

    try:
        processors[1].process(text_data)
        processors[1].validate()
        print("Result 2:", processors[1].format_output())
    except Exception:
        print("Error processing text data")

    try:
        processors[2].process(log_data)
        processors[2].validate()
        print("Result 3:", processors[2].format_output())
    except Exception:
        print("Error processing log data")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    data_processor()
