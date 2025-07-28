class Generators:

    def fib_generator(self, max):
        a = 0
        b = 1
        while a <= max:
            yield a
            a, b = b, a + b

    def count_up_to(self, max):
        num = 1
        while num <= max:
            yield num
            num += 1

    def square_numbers(self, max):
        for i in range(max + 1):
            yield i * i

    def infinite_counter(self):
        num = 0
        while True:
            yield num
            num += 1

    def even_numbers(self):
        num = 2
        while True:
            yield num
            num += 2

    def odd_numbers(self):
        num = 1
        while True:
            yield num
            num += 2

    def string_characters(self, string):
        for ch in string:
            yield ch

    def load_generator(self, generator_fn, *args, genrate_till=10):
        gen = generator_fn(*args)
        for _ in range(genrate_till):
            try:
                print(next(gen), end=' ')
            except StopIteration:
                break
        
        print()

GENERATOR = Generators()

GENERATOR.load_generator(GENERATOR.count_up_to, 20, genrate_till=20)
GENERATOR.load_generator(GENERATOR.fib_generator, 100)
GENERATOR.load_generator(GENERATOR.square_numbers, 10)
GENERATOR.load_generator(GENERATOR.infinite_counter, genrate_till=5)
GENERATOR.load_generator(GENERATOR.even_numbers, genrate_till=5)
GENERATOR.load_generator(GENERATOR.odd_numbers, genrate_till=10)
GENERATOR.load_generator(GENERATOR.string_characters, "OpenAI", genrate_till=50)
