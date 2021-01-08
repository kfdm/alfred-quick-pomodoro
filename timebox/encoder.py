from datetime import datetime
from pathlib import PosixPath


def encoder(z):
    if isinstance(z, datetime):
        return datetime.isotime()
    if isinstance(z, PosixPath):
        return str(z)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type {type_name} is not serializable")
