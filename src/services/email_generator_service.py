from src.api import generate_text
from src.exceptions import ValidationError
from src.utils import clean_text


def generate_email(
    purpose: str,
    tone: str,
    key_points: str,
) -> str:
    """Generate a professional email."""

    purpose = clean_text(purpose)
    tone = clean_text(tone)
    key_points = clean_text(key_points)

    if not purpose:
        raise ValidationError(
            "Email purpose cannot be empty."
        )

    if not tone:
        raise ValidationError(
            "Email tone cannot be empty."
        )

    if not key_points:
        raise ValidationError(
            "Email key points cannot be empty."
        )

    prompt = f"""
You are a professional email writing assistant.

Generate a clear and professional email based on the information below.

Purpose:
{purpose}

Tone:
{tone}

Key points:
{key_points}

Rules:
- Include an appropriate subject.
- Include an appropriate greeting.
- Follow the requested tone.
- Include all important key points.
- Do not invent information.
- Keep the email clear and concise.
- Return only the email.
"""

    return generate_text(prompt)