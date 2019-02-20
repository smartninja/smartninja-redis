# SmartNinja Redis

A wrapper that simulates Redis on localhost (using TinyDB) and uses a real Redis db in production.

**Important:** This package is meant to be used at SmartNinja courses for learning purposes. It is not advised to use this package for serious projects. Use the default `redis` package instead. You only need to change the import statement.

## Installation

Install via pip:

```bash
pip install smartninja-redis
```

## Dependencies

The package has two dependencies: `tinydb` and `redis`. It installs them automatically.

## Usage

Access Redis via the `from_url()` function:

```python
import smartninja_redis as redis

r_url = redis.from_url(url="localhost")
r_url.set(name="Ninja", value="Smart")

print(r_url.get("Ninja"))
```

or via Redis class directly:

```python
from smartninja_redis import Redis

r_class = Redis(host="localhost")
r_class.set(name="smart", value="ninja")

print(r_class.get("smart"))
```

For now, only `set()` and `get()` methods work on localhost.

> The following set() parameters do not work: ex, px, nx, xx

### TinyDB

TinyDB is used to simulate Redis on localhost (if you don't have Redis installed and `REDIS_URL` env var set). TinyDB does not store any data on disk (in this case). It uses memory storage only.

### Using a real Redis service

If you'd like to use SmartNinja with a real Redis service (instead of TinyDB), make sure you have `REDIS_URL` environment variable set.

## Contributions

Contributions via pull requests are warmly welcome!

## TODO

- tests
- CI
