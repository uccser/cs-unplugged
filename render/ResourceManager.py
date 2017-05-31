"""Handles access to external filesystems from the render service."""
import os
from google.cloud import storage, Blob
from cachetools import LRUCache, cachedmethod

CACHE_SIZE = int(os.getenv("DAEMON_CACHE_SIZE", 300 * 1024 * 1024))
RESOURCE_FILEPATH = os.getenv("RESOURCE_FILEPATH", "/resource_files")


def __getsizeof(value):
    """Approximate the size of a python string in memory.

    Args:
        value: A python string to measure.
    Returns:
        An integer of the approximate memory requirement of the
        given string.
    """
    # A string by default requires around 40 bytes
    return 40 + len(value)


class ResourceManager(object):
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
        """Create a resource manager.

        Args:
            bucket_id: The cloud bucket to access.
        """
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_id)

    @cachedmethod(lambda cls: type(cls).__cache)  # Equivilent to ResourceManager.__cache
    def load(self, filepath):
        """Load a file from the cloud bucket.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
        Returns:
            Bytes of the file contents.
        """
        blob = self.bucket.get_blob(filepath)
        if blob is None:
            raise Exception()  # TODO
        return blob.download_as_string()

    def load_to_file(self, filepath, filename):
        """Load a file from the cloud bucket and save to file.

        If the file already exists then the file will not be loaded.
        Should be used sparingly, daemon will likely have more memory
        than disk.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
            filename: The name of the file to save too.
        Returns:
            A string of the filepath where the file was saved.
        """
        if not os.path.exists(RESOURCE_FILEPATH):
            os.makedirs(RESOURCE_FILEPATH, exist_ok=True)

        out_filepath = os.path.join(RESOURCE_FILEPATH, filename)
        if not os.path.exists(out_filepath):
            content = self.load(filepath)
            with open(out_filepath, 'rb') as f:
                f.write(content)

        return out_filepath

    def save(self, filepath, content, content_type='text/plain', is_public=False):
        """Save a file to the cloud bucket.

        Args:
            filepath: The name of the file including full path to the
                file within the storage bucket.
            content: Bytes of the content to be saved to the file.
            content_type: HTTP ‘Content-Type’ header for this object.
            is_public: Determines if all users have read access to this content.
        """
        blob = Blob(filepath, self.bucket)
        blob.upload_from_string(content, content_type)
        if is_public:
            blob.make_public()
