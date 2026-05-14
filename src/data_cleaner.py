import re


def normalize_full_name(full_name: str) -> str:
    full_name = full_name.strip()
    full_name = re.sub(r"[^А-Яа-яA-Za-z\s-]", "", full_name)
    full_name = re.sub(r"\s+", " ", full_name).strip()
    full_name = re.sub(r"([a-zа-я])([A-ZА-Я])", r"\1 \2", full_name)

    parts = full_name.split()

    if len(parts) < 2 or len(parts) > 3:
        return ""

    normalized_parts = [capitalize_word(part) for part in parts]

    if any(part == "" for part in normalized_parts):
        return ""

    return " ".join(normalized_parts)


def capitalize_word(word: str) -> str:
    if not word:
        return ""

    hyphen_parts = word.split("-")
    result = []

    for part in hyphen_parts:
        if not part:
            return ""

        result.append(part[0].upper() + part[1:].lower())

    return "-".join(result)


def normalize_age(age: str) -> str:
    age = age.strip()

    if not age.isdigit():
        return ""

    age_value = int(age)

    if age_value < 1 or age_value > 120:
        return ""

    return str(age_value)


def normalize_phone(phone: str) -> str:
    digits = re.sub(r"\D", "", phone.strip())

    if len(digits) == 11 and digits.startswith("8"):
        digits = "7" + digits[1:]

    if len(digits) == 11 and digits.startswith("7"):
        return f"+7 ({digits[1:4]}) {digits[4:]}"

    return ""


def normalize_email(email: str) -> str:
    email = re.sub(r"\s+", "", email.strip().lower())

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.match(pattern, email):
        return email

    return ""