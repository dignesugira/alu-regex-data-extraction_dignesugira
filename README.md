# ALU Regex Data Extraction

Extracts phone numbers, credit card numbers, times and emails from raw text
using regex.

## Run
python src/main.py

## Patterns
Phones: \b07\d{2}[ -]?\d{3}[ -]?\d{3}\b
- 

Cards: \b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b
- 

Times: (?:1[0-2]|[1-9]):[0-5]\d\s?[AaPp][Mm]
- 

Emails: [a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
- 


