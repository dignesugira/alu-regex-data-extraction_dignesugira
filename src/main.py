import re

with open("input/raw-text.txt") as f:
    text = f.read()

phones = re.findall(r"\b07\d{2}[ -]?\d{3}[ -]?\d{3}\b", text)
print(phones)

cards = re.findall(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", text)
print(cards)

times = re.findall(r"(?:1[0-2]|[1-9]):[0-5]\d\s?[AaPp][Mm]", text)
print(times)

emails = re.findall(r" [a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)