"""Handles access to external filesystems from the render service."""
import os
from ResourceManager import ResourceManager, __getsizeof
from cachetools import LRUCache, cachedmethod

DEBUG = not int(os.getenv("FLASK_PRODUCTION", 1))
CACHE_SIZE = int(os.getenv("DAEMON_CACHE_SIZE", 300 * 1024 * 1024))
NGINX_HOST = int(os.getenv("NGINX_HOST", 300 * 1024 * 1024))
NGINX_PORT = int(os.getenv("NGINX_PORT", 300 * 1024 * 1024))


class LocalResourceManager(ResourceManager):
    """Hanndles access to the external Google Cloud filesystem with caching.

    Caching is important to have here as an entire class will likely
    request the same or similar files.

    The caching mechanism that is used is naiive and requires that
    the each individual daemon must have its own cache therefore their
    is a possibility for redundant use of space. The benefit of this
    system is  that one daemon cannot corrupt the cache for others and
    it is relatively simple to understand compared to redis/memcache.
    """

    __cache = LRUCache(maxsize=CACHE_SIZE, getsizeof=__getsizeof)

    def __init__(self, bucket_id):
        """Create a local resource manager.

        Args:
            bucket_id: The cloud bucket to access.
        """
        if not DEBUG:
            raise Exception("WARNING: Using DEV resource manager in production.")

    @cachedmethod(lambda cls: type(cls).__cache)  # Equivilent to ResourceManager.__cache
    def load(self, filename):
        """Load a file from the cloud bucket.

        Args:
            filename: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            A string of the file contents.
        """
        pass

    def save(self, filename, content, content_type='text/plain', is_public=False):
        """Save a file to the cloud bucket.

        Args:
            filename: The name of the file including full path to the
                file within the storage bucket.
            content: The content to be saved to the file.
            content_type: HTTP ‘Content-Type’ header for this object.
            is_public: Determines if all users have read access to this content.
        """
        pass
