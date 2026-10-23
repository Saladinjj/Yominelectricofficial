# -*- coding: utf-8 -*-
"""Aggregate the 2026-10-23 multilingual blog content."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_1023_a import A_EN, A_FR, A_ES, A_AR
from content_1023_b import B_EN, B_FR, B_ES, B_AR

ALL_POSTS_1023 = [A_EN, A_FR, A_ES, A_AR, B_EN, B_FR, B_ES, B_AR]
