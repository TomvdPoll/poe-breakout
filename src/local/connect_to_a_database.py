import time

import click


@click.command()
@click.option("--database", prompt="Which database?", help="Name of the database to connect to")
def connect(database: str):
    """Connect to a very real and not fake database."""
    print("Connecting to database...")
    time.sleep(1)
    print(f"Connected to {database}.")
    time.sleep(1)
    print("This is definitely a real database connection and not just a print statement.")


if __name__ == "__main__":
    connect()
