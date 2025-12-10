"""Basic tests for social_analyzer package."""

import pytest
from social_analyzer import SocialAnalyzer


def test_import_social_analyzer():
    """Test that SocialAnalyzer can be imported."""
    assert SocialAnalyzer is not None


def test_social_analyzer_initialization():
    """Test that SocialAnalyzer can be initialized in silent mode."""
    analyzer = SocialAnalyzer(silent=True)
    assert analyzer is not None
    assert analyzer.silent is True


def test_social_analyzer_attributes():
    """Test that SocialAnalyzer has expected attributes."""
    analyzer = SocialAnalyzer(silent=True)
    assert hasattr(analyzer, 'websites_entries')
    assert hasattr(analyzer, 'shared_detections')
    assert hasattr(analyzer, 'generic_detection')
    assert hasattr(analyzer, 'log')
    assert hasattr(analyzer, 'silent')


def test_main_function_exists():
    """Test that main function exists and can be imported."""
    from social_analyzer import main
    assert callable(main)
