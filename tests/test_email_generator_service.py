from unittest.mock import patch

import pytest

from src.exceptions import ValidationError
from src.services.email_generator_service import (
    generate_email,
)


def test_empty_purpose():
    with pytest.raises(ValidationError):
        generate_email(
            "",
            "professional",
            "Discuss the project",
        )


def test_empty_tone():
    with pytest.raises(ValidationError):
        generate_email(
            "Request a meeting",
            "",
            "Discuss the project",
        )


def test_empty_key_points():
    with pytest.raises(ValidationError):
        generate_email(
            "Request a meeting",
            "professional",
            "",
        )


def test_whitespace_purpose():
    with pytest.raises(ValidationError):
        generate_email(
            "   ",
            "professional",
            "Discuss the project",
        )


def test_whitespace_tone():
    with pytest.raises(ValidationError):
        generate_email(
            "Request a meeting",
            "   ",
            "Discuss the project",
        )


def test_whitespace_key_points():
    with pytest.raises(ValidationError):
        generate_email(
            "Request a meeting",
            "professional",
            "   ",
        )


@patch(
    "src.services.email_generator_service.generate_text"
)
def test_generate_email(mock_generate_text):

    mock_generate_text.return_value = (
        "Subject: Meeting Request\n\n"
        "Dear Team,\n\n"
        "I would like to request a meeting.\n\n"
        "Best regards"
    )

    result = generate_email(
        purpose="Request a meeting",
        tone="professional",
        key_points="Discuss the project",
    )

    assert result == (
        "Subject: Meeting Request\n\n"
        "Dear Team,\n\n"
        "I would like to request a meeting.\n\n"
        "Best regards"
    )

    mock_generate_text.assert_called_once()