from src.data_cleaner import (
    normalize_full_name,
    capitalize_word,
    normalize_age,
    normalize_phone,
    normalize_email,
)


def test_normalize_full_name_should_clean_and_format_name():
    assert normalize_full_name("  иванов   иван  ") == "Иванов Иван"


def test_normalize_full_name_should_return_empty_for_invalid_name():
    assert normalize_full_name("Иван") == ""


def test_capitalize_word_should_support_hyphenated_names():
    assert capitalize_word("анна-мария") == "Анна-Мария"


def test_normalize_age_should_return_valid_age():
    assert normalize_age(" 25 ") == "25"


def test_normalize_age_should_return_empty_for_invalid_age():
    assert normalize_age("150") == ""
    assert normalize_age("abc") == ""


def test_normalize_phone_should_format_russian_phone_starting_with_eight():
    assert normalize_phone("8 (999) 123-45-67") == "+7 (999) 1234567"


def test_normalize_phone_should_format_russian_phone_starting_with_seven():
    assert normalize_phone("+7 999 123 45 67") == "+7 (999) 1234567"


def test_normalize_phone_should_return_empty_for_invalid_phone():
    assert normalize_phone("12345") == ""


def test_normalize_email_should_clean_and_lowercase_email():
    assert normalize_email(" Test@Example.COM ") == "test@example.com"


def test_normalize_email_should_return_empty_for_invalid_email():
    assert normalize_email("wrong-email") == ""