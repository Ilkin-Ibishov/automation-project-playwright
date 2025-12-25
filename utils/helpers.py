import random
import string
from datetime import datetime

def get_unique_email(prefix: str = "testuser") -> str:
    """Generate a unique email for testing"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = random.randint(1, 9999)
    return f"{prefix}_{timestamp}_{random_suffix}@example.com"

def get_random_string(length: int = 8) -> str:
    """Generate a random string (useful for usernames, etc.)"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))
