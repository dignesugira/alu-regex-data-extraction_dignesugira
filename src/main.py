import re
import json

def mask_card(card):
    digits = card.replace(" ", "").replace("-", "")
    last4 = digits[-4:]
    return "**** **** **** " + last4
def mask_email(email):
    parts = email.split("@")
    return parts[0][0] + "***@" + parts[1]

with open("input/raw-text.txt") as f:
    text = f.read()
# Rwandan mobile numbers. 07 is the prefix. The \b at each end
# stops the pattern matching 10 digits from inside a 16-digit card number.
# [ -]? makes the separator optional so 0788123456, 0788 123 456 and
# 0788-123-456 all match.
phones = re.findall(r"\b07\d{2}[ -]?\d{3}[ -]?\d{3}\b", text)
print(phones)

cards = re.findall(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", text)

masked_cards = []
for c in cards:
    masked_cards.append(mask_card(c))
    print(mask_card(c))

times = re.findall(r"(?:1[0-2]|[1-9]):[0-5]\d\s?[AaPp][Mm]", text)
print(times)

emails = re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

alu_official = r"[a-zA-Z0-9._-]+@alueducation\.com"
alu_alumni   = r"[a-zA-Z0-9._-]+@alumni\.alueducation\.com"
alu_si       = r"[a-zA-Z0-9._-]+@si\.alueducation\.com"

alu_results = []
for e in emails:
    if re.fullmatch(alu_official, e):
        category = "OFFICIAL"
    elif re.fullmatch(alu_alumni, e):
        category = "ALUMNI"
    elif re.fullmatch(alu_si, e):
        category = "SI"
    else:
        category = "OTHER"
    alu_results.append({"email": mask_email(e), "category": category})
    print(category + ":", mask_email(e))

results = {
    "phones": phones,
    "cards_masked": masked_cards,
    "times": times,
    "emails": alu_results
}

with open("output/sample-output.json", "w") as f:
    json.dump(results, f, indent=2)

print("Wrote output/sample-output.json")