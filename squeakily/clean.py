# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_clean.ipynb.

# %% auto 0
__all__ = ['fake', 'whitespace', 'unicode_punctuation', 'normalize_whitespace', 'normalize_punctuation', 'remove_empty_lines',
           'replace_urls', 'replace_dates', 'replace_email', 'replace_phone', 'replace_ip', 'replace_credit_card',
           'replace_ssn']

# %% ../nbs/02_clean.ipynb 2
import re
from faker import Faker

fake = Faker()

# %% ../nbs/02_clean.ipynb 4
# From: https://github.com/bigscience-workshop/data-preparation/blob/main/preprocessing/training/01b_oscar_cleaning_and_filtering/filtering.py#L95
whitespace={
    " ",
    " ",
    " ",
    " ",
    " ",
    "　",
    " ",
    " ",
    " ",
    " ",
    "￼",
    "",
}

def normalize_whitespace(
    text: str,  # The text to normalize
) -> str:       # The normalized text
    """
    Replace the various whitespace characters with the standard one.
    """
    text = "".join(
        [char if char not in whitespace else " " for char in text]
    )
    return text

# %% ../nbs/02_clean.ipynb 6
unicode_punctuation = {
    "，": ",",
    "。": ".",
    "、": ",",
    "„": '"',
    "”": '"',
    "“": '"',
    "«": '"',
    "»": '"',
    "１": '"',
    "」": '"',
    "「": '"',
    "《": '"',
    "》": '"',
    "´": "'",
    "∶": ":",
    "：": ":",
    "？": "?",
    "！": "!",
    "（": "(",
    "）": ")",
    "；": ";",
    "–": "-",
    "—": " - ",
    "．": ". ",
    "～": "~",
    "’": "'",
    "…": "...",
    "━": "-",
    "〈": "<",
    "〉": ">",
    "【": "[",
    "】": "]",
    "％": "%",
    "►": "-",
}

def normalize_punctuation(
    text: str,  # The text to normalize
) -> str:       # The normalized text
    """
    Replace the various unicode punctuation characters with the standard ones.
    """
    text = "".join(
        [unicode_punctuation.get(char, char) for char in text]
    )
    return text

# %% ../nbs/02_clean.ipynb 8
def remove_empty_lines(
    text: str,  # The text to remove empty lines from
) -> str:       # The text with empty lines removed
    """
    Remove empty lines from the text.
    Solution from https://stackoverflow.com/a/3711884/5768407
    """
    lines = text.splitlines()
    filtered = filter(lambda x: not re.match(r'^\s*$', x), lines)
    return "\n".join(filtered)

# %% ../nbs/02_clean.ipynb 10
def replace_urls(
    text: str,                              # The text to replace URLs in
    dummy: str = "https://example.com/",    # The dummy text to replace URLs with
) -> str:                                   # The text with URLs replaced
    """Replace urls from text with a dummy."""
    return re.sub(r"http\S+", dummy, text)

# %% ../nbs/02_clean.ipynb 12
def replace_dates(
    text: str,                  # The text to remove dates from
    dummy: str = fake.date(),   # The dummy text to replace dates with
) -> str:                       # The text with dates replaced
    """Replace dates from text with a dummy."""
    return re.sub(r'\d{1,2}/\d{1,2}/\d{4}', dummy, text)

# %% ../nbs/02_clean.ipynb 15
def replace_email(
    text: str,                          # The text to replace email addresses in
    dummy: str = fake.email(),          # The dummy text to replace email addresses with
) -> str:                               # The text with email addresses replaced
    """Replace email addresses from text with a dummy."""
    return re.sub(r"[\w\.-]+@[\w\.-]+", dummy, text)

# %% ../nbs/02_clean.ipynb 17
def replace_phone(
    text: str,                          # The text to replace phone numbers in
    dummy: str = fake.phone_number(),   # The dummy text to replace phone numbers with
) -> str:                               # The text with phone numbers replaced
    """Replace phone numbers from text with a dummy."""
    return re.sub(r"\(?\d{3}\)?-? *\d{3}-? *-?\d{4}", dummy, text)

# %% ../nbs/02_clean.ipynb 19
def replace_ip(
    text,                       # The text to replace ip addresses in
    dummy1: str = fake.ipv4(),  # The dummy text to replace ipv4 addresses with
    dummy2: str = fake.ipv6(),  # The dummy text to replace ipv6 addresses with
) -> str:                       # The text with ip addresses replaced
    """
    Replace ip addresses from text with a dummy.
    Solution from https://github.com/bigcode-project/bigcode-analysis/blob/main/data_analysis/pii/utils/emails_ip_addresses_detection.py#L48
    """
    ipv4_pattern = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    text = re.sub(ipv4_pattern, dummy1, text)
    ipv6_pattern = r"(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])"
    text = re.sub(ipv6_pattern, dummy2, text)
    return text

# %% ../nbs/02_clean.ipynb 21
def replace_credit_card(
    text: str,                              # The text to replace credit card numbers in
    dummy: str = fake.credit_card_number(), # The dummy text to replace credit card numbers with
) -> str:                                   # The text with credit card numbers replaced
    """Replace credit card numbers from text with a dummy."""
    return re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", dummy, text)

# %% ../nbs/02_clean.ipynb 23
def replace_ssn(
    text: str,                  # The text to replace social security numbers in
    dummy: str = fake.ssn(),    # The dummy text to replace social security numbers with
) -> str:                       # The text with social security numbers replaced
    """Replace social security numbers from text with a dummy."""
    return re.sub(r"\d{3}-\d{2}-\d{4}", dummy, text)
