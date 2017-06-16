"""Handles access to external filesystems from the render service."""
import os
from cachetools import LRUCache, cachedmethod
from io import BytesIO

CACHE_SIZE = int(os.getenv("DAEMON_CACHE_SIZE", 300 * 1024 * 1024))


class FileManager(object):
    """Handles access to the filesystem for loading and reading files.

    Caching is important to this class as it speeds up slow reads when
    the directory is a mounted bucket.

    Since files with the same filepath could belong to different
    directories only the first found is used, based on the order
    of the constructor arguments in FIFO.
    """

    __cache = LRUCache(maxsize=CACHE_SIZE, getsizeof=lambda value: value.__sizeof__())

    def __init__(self, *args, **kwargs):
        """Create a resource manager.

        Args:
            args: Directories to load files from.
        """
        if len(args) == 0:
            raise Exception()  # TODO
        self.directories = tuple(args)
        self.save_directory = kwargs.get("save_directory", None)

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

        Finds the first file that matches the filepath (this means
        if a folder matches first it is not returned.)

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            A string of the filepath.
        """
        for directory in self.directories:
            path = os.path.join(directory, filepath)
            if os.path.exists(path) and os.path.isfile(path):
                return path
        raise OSError("File not found.")

    def save(self, filepath, content):
        """Save a file to the cloud bucket.

        If save directory is not set, tries to find the file within
        any directories contained to overwrite it. If no directory
        is found then writes to the first given directory.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
            content: Bytes of the content to be saved to the file.
        """
        save_path = None
        if self.save_directory is None:
            for directory in self.directories:
                path = os.path.join(directory, filepath)
                if os.path.exists(path) and os.path.isfile(path):
                    save_path = path

            if save_path is None:
                directory = self.directories[0]
                save_path = os.path.join(directory, filepath)
        else:
            save_path = os.path.join(self.save_directory, filepath)

        save_directory, _ = os.path.split(save_path)
        os.makedirs(save_directory, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(content)
