"""
Basic unit tests for social-analyzer.

These tests avoid network operations by using silent=True.
"""

import pytest
from app import SocialAnalyzer


def test_social_analyzer_import():
    """Test that SocialAnalyzer can be imported."""
    assert SocialAnalyzer is not None


def test_social_analyzer_construction():
    """Test that SocialAnalyzer can be constructed with silent=True."""
    analyzer = SocialAnalyzer(silent=True)
    assert analyzer is not None
    assert analyzer.silent is True


def test_social_analyzer_has_required_methods():
    """Test that SocialAnalyzer has expected methods."""
    analyzer = SocialAnalyzer(silent=True)
    assert hasattr(analyzer, 'setup_logger')
    assert hasattr(analyzer, 'list_all_websites')
