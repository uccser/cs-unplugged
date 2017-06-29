"""Test the file manager for reading of and writing to files."""
import os
import shutil
from render.tests.BaseTest import BaseTest
from render.daemon.FileManager import FileManager


class FileManagerTest(BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        cwd = os.getcwd()
        cls.folderpath_one = os.path.join(cwd, "test_assets")
        cls.folderpath_two = os.path.join(cwd, "other_test_assets")
        os.makedirs(cls.folderpath_one, exist_ok=False)
        os.makedirs(cls.folderpath_two, exist_ok=False)

        cls.testfile_name = "test.txt"
        cls.testfile_contents = "This is a testing file."

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.folderpath_one, ignore_errors=False)
        shutil.rmtree(cls.folderpath_two, ignore_errors=False)

    def setUp(self):
        filepath = os.path.join(self.folderpath_one, self.testfile_name)
        with open(filepath, "wb") as f:
            f.write(self.testfile_contents.encode("ascii"))

    def test_load_file(self):
        file_manager = FileManager(self.folderpath_one)
        data = file_manager.load(self.testfile_name)
        string = data.read().decode("ascii")
        self.assertEqual(string, self.testfile_contents)

    def test_load_file_multiple_directories(self):
        file_manager = FileManager(self.folderpath_two, self.folderpath_one)
        data = file_manager.load(self.testfile_name)
        string = data.read().decode("ascii")
        self.assertEqual(string, self.testfile_contents)

    def test_save_file_with_directory(self):
        file_manager = FileManager(self.folderpath_one, self.folderpath_two, save_directory=self.folderpath_two)

        filename = "save_with_directory.txt"
        file_content = "Hello world!"
        file_manager.save(filename, file_content.encode("ascii"))

        data = file_manager.load(filename)
        string = data.read().decode("ascii")
        self.assertEqual(string, file_content)

    def test_save_file_without_directory(self):
        file_manager = FileManager(self.folderpath_one, self.folderpath_two)

        filename = "save_without_directory.txt"
        file_content = "Hello world!"
        file_manager.save(filename, file_content.encode("ascii"))

        data = file_manager.load(filename)
        string = data.read().decode("ascii")
        self.assertEqual(string, file_content)

    def test_save_file_without_directory_overwrite(self):
        file_manager = FileManager(self.folderpath_two, self.folderpath_one)

        file_content = "Hello world!"
        file_manager.save(self.testfile_name, file_content.encode("ascii"))

        data = file_manager.load(self.testfile_name)
        string = data.read().decode("ascii")
        self.assertEqual(string, file_content)
