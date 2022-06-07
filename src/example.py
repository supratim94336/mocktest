from src.dataset import load_data
from datetime import datetime


def add(x, y):
    """Add Function"""
    return x + y


def process_data():
    data = load_data()
    # process the data in certain ways ...
    processed_data = data["key1"]
    return processed_data


def get_time_of_day():
    """Return string Night/Morning/Afternoon/Evening depending on the hours range."""
    time = datetime.now()
    if 0 <= time.hour < 6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour < 18:
        return "Afternoon"
    return "Evening"
