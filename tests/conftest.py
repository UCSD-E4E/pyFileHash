'''Test Configurations
'''

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from utils import create_random_file


@pytest.fixture(name='test_file', params=['size'])
def create_test_file(request: pytest.FixtureRequest) -> Path:
    """Creates a test file with the specified size

    Args:
        size (int): Desired size of file

    Returns:
        Path: Path to test file

    Yields:
        Iterator[Path]: Path to test file
    """
    with TemporaryDirectory() as tmp_dir:
        temp_file = Path(tmp_dir, 'temp_file').resolve()
        size = request.param
        create_random_file(temp_file, size)
        yield temp_file

