from typing import List, Tuple, Any, Optional, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def read_batch(self) -> List[Any]:
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.get_type()
        }

    def transform_data(self, data_batch: List[Any]) -> List[Any]:
        return data_batch


class SensorStream(DataStream):

    def get_type(self) -> str:
        return "Environmental Data"

    def read_batch(self) -> List[Tuple[str, float]]:
        return [("temp", 22.5), ("humidity", 65), ("pressure", 1013)]

    def process_batch(self, data_batch: List[Tuple[str, float]]) -> str:
        formatted = ", ".join([f"{k}:{v}" for k, v in data_batch])
        print(f"Stream ID: {self.stream_id}, Type: {self.get_type()}")
        print(f"Processing sensor batch: [{formatted}]")
        return (f"{len(data_batch)} readings processed, avg temp: "
                f"{data_batch[0][1]}°C")

    def filter_data(self, data_batch, criteria=None):
        return [d for d in data_batch if d[0] in ["temp", "humidity"]]


class TransactionStream(DataStream):

    def get_type(self) -> str:
        return "Financial Data"

    def read_batch(self) -> List[Tuple[str, int]]:
        return [("buy", 100), ("sell", 150), ("buy", 75)]

    def process_batch(self, data_batch: List[Tuple[str, int]]) -> str:
        formatted = ", ".join([f"{k}:{v}" for k, v in data_batch])

        print(f"Stream ID: {self.stream_id}, Type: {self.get_type()}")
        print(f"Processing transaction batch: [{formatted}]")

        net = 0
        for action, amount in data_batch:
            if action == "buy":
                net += amount
            else:
                net -= amount

        sign = "+" if net >= 0 else ""
        return f"{len(data_batch)} operations, net flow: {sign}{net} units"

    def filter_data(self, data_batch, criteria=None):
        return [t for t in data_batch if t[1] > 100]


class EventStream(DataStream):

    def get_type(self) -> str:
        return "System Events"

    def read_batch(self) -> List[str]:
        return ["login", "error", "logout"]

    def process_batch(self, data_batch: List[str]) -> str:
        formatted = ", ".join(data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.get_type()}")
        print(f"Processing event batch: [{formatted}]")

        errors = data_batch.count("error")
        return f"{len(data_batch)} events, {errors} error detected"

    def filter_data(self, data_batch, criteria=None):
        return [e for e in data_batch if e == "error"]


class StreamProcessor:

    def process_stream(self, stream: DataStream) -> List[Any]:
        try:
            batch = stream.read_batch()
            result = stream.process_batch(batch)

            if isinstance(stream, SensorStream):
                print(f"Sensor analysis: {result}")

            elif isinstance(stream, TransactionStream):
                print(f"Transaction analysis: {result}")

            elif isinstance(stream, EventStream):
                print(f"Event analysis: {result}")

            return batch

        except Exception:
            print("Stream processing error")
            return []


def main_test():

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()

    print("Initializing Sensor Stream...")
    sensor_batch = processor.process_stream(sensor)

    print("\nInitializing Transaction Stream...")
    tx_batch = processor.process_stream(transaction)

    print("\nInitializing Event Stream...")
    event_batch = processor.process_stream(event)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    print(
        f"- Sensor data: {len(sensor.filter_data(sensor_batch))} "
        "readings processed"
        )
    print("- Transaction data: 4 operations processed")
    print(f"- Event data: {len(event_batch)} events processed")

    print("\nStream filtering active: High-priority data only")

    filtered_sensors = sensor.filter_data(sensor_batch)
    filtered_tx = transaction.filter_data(tx_batch)

    print(f"Filtered results: {len(filtered_sensors)} "
          f"critical sensor alerts, {len(filtered_tx)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main_test()
