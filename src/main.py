import logging

from src.exceptions import (
    AIProviderError,
)
from src.services.email_generator_service import (
    generate_email,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    """Run the AI Email Generator application."""

    logger.info("Application started")

    purpose = input(
        "What is the purpose of the email? "
    )

    if not purpose.strip():
        logger.warning(
            "Email purpose is empty"
        )
        print(
            "Input Error: Email purpose cannot be empty."
        )
        return

    tone = input(
        "What tone do you want? "
    )

    if not tone.strip():
        logger.warning(
            "Email tone is empty"
        )
        print(
            "Input Error: Email tone cannot be empty."
        )
        return

    key_points = input(
        "What key points should the email include? "
    )

    if not key_points.strip():
        logger.warning(
            "Email key points are empty"
        )
        print(
            "Input Error: Email key points cannot be empty."
        )
        return

    try:
        email = generate_email(
            purpose=purpose,
            tone=tone,
            key_points=key_points,
        )

        logger.info(
            "Email generation completed"
        )

        print("\nGenerated Email")
        print("-" * 30)
        print(email)

    except AIProviderError as error:
        logger.error(
            "AI provider error: %s",
            error,
        )
        print(f"AI Error: {error}")

    except Exception:
        logger.exception(
            "Unexpected application error"
        )
        print(
            "Unexpected Error: "
            "Something went wrong."
        )


if __name__ == "__main__":
    main()