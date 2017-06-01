"""Handles access to external filesystems from the render service."""
import os
from cachetools import LRUCache, cachedmethod
from io import BytesIO

CACHE_SIZE = int(os.getenv("DAEMON_CACHE_SIZE", 300 * 1024 * 1024))


class ResourceManager(object):
    """Handles access to the filesystem for loading and reading files.

    Caching is important to this class as it speeds up slow reads when
    the directory is a mounted bucket.
    """

    __cache = LRUCache(maxsize=CACHE_SIZE, getsizeof=lambda value: value.__sizeof__())

    def __init__(self, directory):
        """Create a resource manager.

        Args:
            directory: The directory to load from.
        """
        self.directory = directory

    @cachedmethod(lambda cls: type(cls).__cache)
    def load(self, filepath):
        """Load a file from the directory/mounted cloud bucket.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            BytesIO stream of the file contents.
        """
        path = self.get_path(filepath)
        data = None
        with open(path, 'rb') as f:
            data = f.read()
        return BytesIO(data)

    def get_path(self, filepath):
        """Get the full filepath for a given resource.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            A string of the filepath.
        """
        return os.path.join(self.directory, filepath)

    def file_exists(self, filepath):
        """Check to see if a file exists.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            True if the filepath exists and is file, False otherwise.
        """
        path = self.get_path(filepath)
        return os.path.exists(path) and os.path.isfile(path)

    def save(self, filepath, content):
        """Save a file to the cloud bucket.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
            content: Bytes of the content to be saved to the file.
        """
        path = self.get_path(filepath)
        with open(path, 'wb') as f:
            f.write(content)
