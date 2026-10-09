# Python Fundamentals Practice

Mark an item complete only when you can explain it, write a small example, and
debug a nearby variation without relying on a finished solution. All items
start unchecked because this is a new Python learning workspace.

## Level 1: Foundations

### Runtime and Tooling

- [ ] Explain Python source, bytecode, the interpreter, and CPython
- [ ] Select a Python version and create an isolated virtual environment
- [ ] Use `python`, the REPL, `uv`, and this repository's `make` commands
- [ ] Read `pyproject.toml`, `.python-version`, and `uv.lock`
- [ ] Run a script, pass arguments, and use `python -m` for a module
- [ ] Find a function or module in the official documentation

### Values and Language Basics

- [ ] Work with `None`, booleans, integers, floats, strings, and bytes
- [ ] Explain names, object identity, equality, and assignment
- [ ] Predict truthiness and short-circuit behavior
- [ ] Explain mutable versus immutable objects and aliasing
- [ ] Use f-strings and distinguish text from binary data
- [ ] Recognize why floating-point results can surprise

### Control Flow and Functions

- [ ] Write `if`, `for`, `while`, and `match` where appropriate
- [ ] Use `range`, `enumerate`, `zip`, and comprehensions
- [ ] Define functions with positional, keyword, and default arguments
- [ ] Explain why mutable default arguments persist across calls
- [ ] Use `*args`, `**kwargs`, and argument unpacking
- [ ] Explain local, enclosing, global, and built-in scope

### Collections and Objects

- [ ] Create, read, update, and iterate lists, tuples, dictionaries, and sets
- [ ] Choose a collection based on ordering, uniqueness, and lookup needs
- [ ] Slice a sequence and explain copy versus shared references
- [ ] Sort with `key` and explain stability
- [ ] Define a small class and distinguish instance from class attributes
- [ ] Use `dataclass` when it simplifies a data-focused object

### Type Hints

- [ ] Annotate function parameters and return values
- [ ] Read `list[T]`, `dict[K, V]`, `T | None`, and `Callable` annotations
- [ ] Explain that annotations do not validate values at runtime
- [ ] Use a type alias when it makes an interface clearer
- [ ] Distinguish `Any` from a specific type

### Errors and Resource Cleanup

- [ ] Raise and catch specific exceptions
- [ ] Preserve context with `raise ... from ...`
- [ ] Use `try`, `except`, `else`, and `finally` correctly
- [ ] Use `with` to close files and other resources
- [ ] Avoid bare `except` and silently swallowed errors

### Modules and Packages

- [ ] Import modules and names without shadowing standard-library modules
- [ ] Explain module search paths and why working directory matters
- [ ] Use `__name__ == "__main__"` for a runnable module
- [ ] Organize related files into a package when imports require it
- [ ] Distinguish an installed dependency from local source code

### Python Standard Library Basics

- [ ] Read arguments and exit status with `sys` and `argparse`
- [ ] Read and write text with `pathlib`, `open`, and explicit encoding
- [ ] Parse and serialize JSON safely
- [ ] Use `datetime` with aware timestamps where needed
- [ ] Use `collections` and `itertools` for a concrete task
- [ ] Build a small command-line program

### Foundation Projects

- [ ] CLI calculator
- [ ] File reader and writer
- [ ] JSON-backed task list
- [ ] Text statistics tool

## Level 2: Intermediate

### Python Data Model and Typing

- [ ] Explain `__repr__`, `__eq__`, and hashing contracts
- [ ] Use iterables, iterators, generators, and `yield`
- [ ] Write a small decorator and explain closure behavior
- [ ] Use `Protocol`, generics, and typed collections when useful
- [ ] Use `TypedDict` or a dataclass for a suitable data boundary
- [ ] Validate untrusted data at runtime despite annotations

### Asynchronous I/O

- [ ] Distinguish a coroutine object from a running task
- [ ] Use `async def`, `await`, and `asyncio.run`
- [ ] Explain which operations block the event loop
- [ ] Compare sequential awaits with `gather` and `TaskGroup`
- [ ] Bound concurrent I/O instead of starting unlimited tasks
- [ ] Handle timeouts and cancellation without swallowing them

### Threads and Scheduling

- [ ] Use a thread for a blocking I/O task
- [ ] Explain shared memory and race conditions
- [ ] Protect shared mutable state with a lock when needed
- [ ] Use `ThreadPoolExecutor` and await or collect every result
- [ ] Explain the GIL for the interpreter in use without assuming it is universal
- [ ] Measure whether threads help the chosen workload

### Iteration, Files, and Streams

- [ ] Process a large file line by line
- [ ] Use context managers for deterministic cleanup
- [ ] Explain buffering and text encoding
- [ ] Compose iterators without materializing unnecessary lists
- [ ] Handle malformed input and partial writes

### HTTP and Networking

- [ ] Make an HTTP request with the standard library or a justified package
- [ ] Set a timeout and handle network failures
- [ ] Parse URLs, headers, status codes, and JSON responses
- [ ] Write a small HTTP endpoint for learning purposes
- [ ] Distinguish request validation from Python type hints

### Testing

- [ ] Write a pytest test for a normal case and an edge case
- [ ] Test expected exceptions with `pytest.raises`
- [ ] Use parametrization for related input cases
- [ ] Use `tmp_path` or `tempfile` for filesystem tests
- [ ] Replace an external dependency at its use site when necessary
- [ ] Keep tests deterministic and clean up resources
- [ ] Measure coverage when it answers a concrete question

### Package Management

- [ ] Explain virtual environments and dependency isolation
- [ ] Distinguish runtime from development dependencies
- [ ] Update `pyproject.toml` and `uv.lock` together
- [ ] Reproduce an environment with `uv sync --locked`
- [ ] Inspect dependency licenses and advisories
- [ ] Explain when a script workspace needs packaging

### Intermediate Projects

- [ ] Streaming log analyzer
- [ ] Bounded concurrent URL checker
- [ ] HTTP JSON API using the standard library
- [ ] File synchronization CLI with cancellation

## Level 3: Proficient

### Asynchronous Design

- [ ] Propagate cancellation through multiple operations
- [ ] Apply timeouts at external boundaries
- [ ] Retry only safe operations with bounds and backoff
- [ ] Shut down tasks and executors cleanly
- [ ] Diagnose a program that does not exit

### Parallelism and Processes

- [ ] Explain concurrency versus parallelism in Python
- [ ] Compare `asyncio`, threads, processes, and subprocesses
- [ ] Use `ProcessPoolExecutor` for suitable CPU-bound work
- [ ] Explain pickling and data-transfer costs between processes
- [ ] Use `subprocess.run` and `Popen` with argument lists and timeouts
- [ ] Handle exit codes, output streams, and cleanup
- [ ] Choose an execution model using correctness and measurements

### Runtime and Memory

- [ ] Explain reference counting and cyclic garbage collection in CPython
- [ ] Recognize common retention and memory-growth patterns
- [ ] Use `tracemalloc` for a focused memory investigation
- [ ] Profile CPU work with `cProfile`
- [ ] Use `time.perf_counter` and repeat measurements
- [ ] Avoid optimization claims without evidence

### APIs and Data Boundaries

- [ ] Validate external input and return consistent errors
- [ ] Implement pagination and filtering
- [ ] Stream large inputs rather than reading all into memory
- [ ] Handle binary and multipart data safely
- [ ] Apply request-size limits and timeouts
- [ ] Shut down an HTTP service cleanly

### Data Stores

- [ ] Use parameterized SQL queries
- [ ] Use transactions correctly
- [ ] Understand connection lifetime and pooling when applicable
- [ ] Handle missing and nullable values explicitly
- [ ] Test against a disposable database when appropriate

### Security

- [ ] Avoid `eval`, unsafe `pickle` input, and unsafe YAML loaders
- [ ] Prevent command, path, and SQL injection
- [ ] Keep secrets out of source control and logs
- [ ] Separate authentication from authorization
- [ ] Understand dependency and supply-chain risks

### Project Organization

- [ ] Organize modules by current responsibility
- [ ] Keep side effects at clear boundaries
- [ ] Separate configuration from core logic
- [ ] Avoid circular imports and unnecessary packaging layers
- [ ] Add abstractions only for a concrete need

### Proficient Projects

- [ ] Rate-limited API client with retries and cancellation
- [ ] Streaming file-processing pipeline
- [ ] CPU-bound batch with measured process-pool behavior
- [ ] HTTP service with validation, persistence, and integration tests

## Level 4: Advanced

### Runtime Internals

- [ ] Explain CPython execution, bytecode, and the GIL at a practical level
- [ ] Compare interpreter/version behavior before relying on internals
- [ ] Diagnose import and module-loading problems
- [ ] Use traceback, logging, and profiling tools effectively
- [ ] Explain memory ownership across thread and process boundaries

### Advanced Typing and APIs

- [ ] Design readable generic interfaces and protocols
- [ ] Use overloads only when they clarify real call patterns
- [ ] Explain variance at a practical level
- [ ] Keep public annotations and runtime behavior aligned
- [ ] Publish a small package only when distribution is a real goal

### Reliability and Observability

- [ ] Implement structured, contextual logging
- [ ] Expose health checks for a service
- [ ] Record useful latency and error metrics
- [ ] Define timeouts and failure budgets at external boundaries
- [ ] Diagnose partial failures from logs and traces

### Performance and Scale

- [ ] Build a representative benchmark
- [ ] Separate latency, throughput, CPU, and memory concerns
- [ ] Profile before and after an optimization
- [ ] Measure serialization and process-start overhead
- [ ] Use caching only with a concrete invalidation plan

### Advanced Testing and Delivery

- [ ] Write integration tests at useful boundaries
- [ ] Test cancellation, timeouts, retries, and partial failures
- [ ] Use property-based testing when input complexity justifies it
- [ ] Run lint and tests in continuous integration
- [ ] Reproduce a deployment environment from locked dependencies

### Advanced Projects

- [ ] Service with observability and graceful shutdown
- [ ] CPU-bound process pool with measured scaling behavior
- [ ] Streaming proxy with bounded memory use
- [ ] Packaged CLI with documented entry points

## Mastery Milestones

### Foundations to Intermediate

- [ ] Build three small tools with the standard library
- [ ] Explain names, mutation, functions, imports, and exceptions
- [ ] Test normal and failure paths with the configured pytest runner

### Intermediate to Proficient

- [ ] Explain and demonstrate coroutine versus task behavior
- [ ] Build bounded concurrent I/O and cleanly cancel it
- [ ] Diagnose a race, blocked event loop, or leaked resource

### Proficient to Advanced

- [ ] Build and operate a complete service with graceful shutdown
- [ ] Find a real bottleneck with profiling and verify an improvement
- [ ] Explain important runtime and typing trade-offs clearly
