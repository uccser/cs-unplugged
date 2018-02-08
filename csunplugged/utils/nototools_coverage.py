"""Module for detecting ord of characters in fonts."""

# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This Python snippet is from the Google Nototools repository:
# https://github.com/googlei18n/nototools/blob/master/nototools/coverage.py
#
# To use under the Apache 2.0 License, modifications have been listed below:
# 1. File has been renamed from 'coverage.py' to 'nototools_coverage.py'
# 2. All code not required by 'character_set' function has been removed.
# 3. Double quotes have been used instead of single quotes to match project
#    style.
# 4. Indentation has been changed to match project style.
# 5. Change first word of 'character_set' function docstring to imperative
#    mood to match project style.

__author__ = 'roozbeh@google.com (Roozbeh Pournader)'

from fontTools import ttLib


def character_set(font):
    """Return the character coverage of a font.

    Args:
        font: The input font's file name, or a TTFont.

    Returns:
        A frozenset listing the characters supported in the font.
    """
    if type(font) is str:
        font = ttLib.TTFont(font, fontNumber=0)
    cmap_table = font["cmap"]
    cmaps = {}
    for table in cmap_table.tables:
        if (table.format, table.platformID, table.platEncID) in [
            (4, 3, 1),
            (12, 3, 10),
        ]:
            cmaps[table.format] = table.cmap
    if 12 in cmaps:
        cmap = cmaps[12]
    elif 4 in cmaps:
        cmap = cmaps[4]
    else:
        cmap = {}
    return frozenset(cmap.keys())
