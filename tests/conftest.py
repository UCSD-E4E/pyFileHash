'''Test Configurations
'''

from pathlib import Path
from random import randbytes
from tempfile import TemporaryDirectory

import pytest

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
        with open(temp_file, 'wb') as handle:
            idx = 0
            while idx < request.param:
                rand_buffer = randbytes(2*1024*1024)
                if (request.param - idx) < len(rand_buffer):
                    handle.write(rand_buffer[:request.param - idx])
                    idx += request.param - idx
                else:
                    handle.write(rand_buffer)
                    idx += len(rand_buffer)
        assert temp_file.stat().st_size == request.param
        yield temp_file

