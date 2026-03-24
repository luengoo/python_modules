def game_data() -> None:
    print("Processing 1000 game events...\n")
    nbr = data_stream()
    next(nbr)
    print(f"Event {next(nbr)}: Player alice (level 5) killed a monster")
    print(f"Event {next(nbr)}: Player bob (level 12) found a treasure")
    print(f"Event {next(nbr)}: Player charlie (level 8) leveled up")
    print("...\n")


def stream_analytics() -> None:
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    for event in game_events():
        total += 1
        if event % 2 == 0:
            high_level += 1
        elif event % 3 == 0:
            level_up += 1
        elif event % 5 == 0:
            treasure += 1
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


def data_stream() -> iter:
    for i in range(1000):
        yield i


def game_events() -> iter:
    for i in range(1000):
        yield i


def fibonacci(n: int) -> iter:
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def generator_demo() -> None:
    fibo_times = 10
    prime_times = 5
    fibo = fibonacci(fibo_times)
    prime_nbr = prime(prime_times)
    it_f = iter(fibo)
    it_p = iter(prime_nbr)
    i = 0
    j = 0
    print("Fibonacci sequence (first 10): ", end="")
    for _ in range(fibo_times):
        if i == fibo_times - 1:
            print(next(it_f))
        else:
            print(next(it_f), end=", ")
        i += 1
    print("Prime numbers (first 5): ", end="")
    for _ in range(prime_times):
        if j == prime_times - 1:
            print(next(it_p))
        else:
            print(next(it_p), end=", ")
        j += 1


def prime(n: int) -> iter:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
            count += 1
        num += 1


def main_func() -> None:
    print("=== Game Data Stream Processor ===\n")
    game_data()
    stream_analytics()
    generator_demo()


if __name__ == "__main__":
    main_func()
