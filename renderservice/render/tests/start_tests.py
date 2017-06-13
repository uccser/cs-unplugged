"""Starts tests for the Render Service, daemon and webservice."""
import unittest

#
# Resource Generation Tests
#

from render.tests.test_binary_cards_small import BinaryCardsSmallResourceTest  # noqa: F401
from render.tests.test_binary_cards import BinaryCardsResourceTest  # noqa: F401
from render.tests.test_binary_to_alphabet import BinaryToAlphabetResourceTest  # noqa: F401
from render.tests.test_binary_windows import BinaryWindowsResourceTest  # noqa: F401
from render.tests.test_modulo_clock import ModuloClockResourceTest  # noqa: F401
from render.tests.test_sorting_network import SortingNetworkResourceTest  # noqa: F401
from render.tests.test_treasure_hunt import TreasureHuntResourceTest  # noqa: F401

#
# General Tests
#

from render.tests.test_file_manager import FileManagerTest  # noqa: F401
from render.tests.test_resource_generator import ResourceGeneratorTest  # noqa: F401
from render.tests.test_queue_handler import QueueHandlerTest  # noqa: F401

#
# Webservice Tests
#

if __name__ == "__main__":
    unittest.main()
