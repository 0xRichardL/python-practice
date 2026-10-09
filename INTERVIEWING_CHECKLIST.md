# Python Interview Skills Checklist

These tiers prioritize common Python and backend interview topics; the mix
depends on the role. Explain each item and demonstrate it with a small example.

## Tier 1: Core Skills

### Python Semantics

- [ ] Names, object identity, equality, mutability, and aliasing
- [ ] Truthiness, `None`, and short-circuit expressions
- [ ] List, tuple, dict, and set behavior and complexity
- [ ] Slicing, comprehensions, iteration, and generators
- [ ] Function arguments, mutable defaults, and closures
- [ ] Class versus instance attributes, dataclasses, and method lookup
- [ ] Exceptions, context managers, and deterministic cleanup

### Algorithms and Problem Solving

- [ ] Clarify constraints and edge cases before coding
- [ ] Choose a suitable collection or algorithm
- [ ] Explain time and space complexity
- [ ] Test empty, duplicate, boundary, and invalid inputs
- [ ] Improve a simple correct solution using evidence

### Runtime and Tooling

- [ ] Python, CPython, bytecode, and implementation-dependent behavior
- [ ] Imports, packages, module execution, and `__main__`
- [ ] Virtual environments, `pyproject.toml`, and locked dependencies
- [ ] Type hints versus runtime validation
- [ ] File paths, text encodings, JSON, and command-line arguments

### API and Error Handling

- [ ] HTTP lifecycle, status codes, and consistent errors
- [ ] Input validation at system boundaries
- [ ] Timeouts, retries, and cancellation
- [ ] Preserve useful error context without leaking sensitive data

### Testing

- [ ] Unit versus integration versus end-to-end tests
- [ ] Normal, error, and boundary cases
- [ ] Deterministic tests and resource cleanup
- [ ] Test doubles at the dependency boundary

## Tier 2: Common Backend Topics

### Concurrency and Parallelism

- [ ] Coroutines, tasks, and blocking calls in `asyncio`
- [ ] `gather`, `TaskGroup`, timeout, and cancellation behavior
- [ ] Threads, shared state, locks, and race conditions
- [ ] GIL behavior for the interpreter in use
- [ ] Process pools, pickling, startup, and data-copy costs
- [ ] Safe subprocess arguments, output, exit status, and timeouts

### Performance and Memory

- [ ] Profiling CPU and memory before optimization
- [ ] Iterator versus materialized collection trade-offs
- [ ] Benchmark setup and measurement pitfalls
- [ ] Caching and invalidation trade-offs

### Databases and Reliability

- [ ] Parameterized queries and transactions
- [ ] Connection lifetime and pooling
- [ ] Retry safety, idempotency, and partial failures
- [ ] Bounded concurrency and graceful shutdown

### Security

- [ ] Authentication versus authorization
- [ ] Command, path, and SQL injection
- [ ] Unsafe deserialization and dynamic code execution
- [ ] Secret handling and dependency risk

## Tier 3: Role-Dependent Depth

### Advanced Python

- [ ] Descriptors and the attribute lookup model
- [ ] Protocols, generics, and variance
- [ ] Iteration protocol and context-manager internals
- [ ] Import system and package distribution

### Runtime and Systems

- [ ] CPython reference counting and cycle collection
- [ ] Thread and process start-method differences
- [ ] CPU and heap profiling under realistic load
- [ ] Observability across async boundaries

### Distributed Systems

- [ ] Stateless processes and horizontal scaling
- [ ] Queues, delivery semantics, and idempotency
- [ ] Cache consistency and partial failures
- [ ] Tracing context and service boundaries

## Tier 4: Nice to Have

- [ ] CPython contribution workflow
- [ ] C extensions or the Python C API
- [ ] Advanced interpreter internals
- [ ] Specialized networking protocols

## Practical Interview Readiness

- [ ] Clarify the task and state assumptions
- [ ] Start with a correct simple solution
- [ ] Narrate important trade-offs in plain language
- [ ] Write or describe useful tests
- [ ] Debug from evidence rather than guessing
- [ ] Use Python features to clarify the solution, not hide it
