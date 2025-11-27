"""Regression tests for django-honeyguard migrations."""

import pytest
from django.core.management import call_command


@pytest.mark.django_db
def test_models_aligned_with_migrations():
    """Ensure makemigrations detects no pending model changes."""
    try:
        call_command(
            "makemigrations",
            "--check",
            "--dry-run",
            verbosity=0,
        )
    except SystemExit:
        pytest.fail(
            "Pending model changes detected."
            "Run `python manage.py makemigrations`"
        )
