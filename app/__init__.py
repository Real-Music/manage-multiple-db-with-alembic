from sqlalchemy.ext.declarative import declarative_base

Base_Model_One = declarative_base()
Base_Model_Two = declarative_base()

from app import address, user

def print_to_console(*args):
    """Write string to terminal"""
    print(f"===={args}====\n")