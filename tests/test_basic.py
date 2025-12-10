"""
Basic tests for social-analyzer.
Tests only import and initialization without network calls.
"""

import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_import_social_analyzer():
    """Test that SocialAnalyzer can be imported."""
    from app import SocialAnalyzer
    assert SocialAnalyzer is not None


def test_social_analyzer_initialization():
    """Test that SocialAnalyzer can be initialized without network calls."""
    from app import SocialAnalyzer
    
    # Initialize with silent=True to avoid any output
    analyzer = SocialAnalyzer(silent=True)
    
    # Verify basic attributes are set
    assert analyzer is not None
    assert analyzer.silent is True
    assert analyzer.workers == 15
    assert hasattr(analyzer, 'websites_entries')
    assert hasattr(analyzer, 'shared_detections')
    assert hasattr(analyzer, 'log')


def test_social_analyzer_attributes():
    """Test that SocialAnalyzer has expected attributes."""
    from app import SocialAnalyzer
    
    analyzer = SocialAnalyzer(silent=True)
    
    # Check that essential attributes exist
    assert hasattr(analyzer, 'sites_path')
    assert hasattr(analyzer, 'languages_path')
    assert hasattr(analyzer, 'headers')
    assert isinstance(analyzer.headers, dict)
    assert 'User-Agent' in analyzer.headers
