#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Basic tests for SocialAnalyzer.
Tests only import and initialization without performing network calls.
"""

import pytest


def test_import_social_analyzer():
    """Test that SocialAnalyzer can be imported."""
    from app import SocialAnalyzer
    assert SocialAnalyzer is not None


def test_social_analyzer_initialization():
    """Test that SocialAnalyzer can be initialized without network calls."""
    from app import SocialAnalyzer
    
    # Initialize with silent=True to avoid any output
    sa = SocialAnalyzer(silent=True)
    
    # Verify basic attributes are set
    assert sa is not None
    assert hasattr(sa, 'websites_entries')
    assert hasattr(sa, 'shared_detections')
    assert hasattr(sa, 'log')
    assert sa.silent == True


def test_main_function_exists():
    """Test that main function exists for entry point."""
    from app import main
    assert main is not None
    assert callable(main)
