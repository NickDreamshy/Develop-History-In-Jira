import os
import pytest
from your_module import getting_date_deep

@pytest.fixture
def sample_sources_file(tmp_path):

    data = [
        "VCS URL https://github.com/example/repo1\n",
        "Commit hash: abc123\n",
        "VCS URL https://github.com/example/repo2\n",
        "Commit hash: def456\n",
    ]
    file_path = tmp_path / "sources.txt"
    with open(file_path, "w") as f:
        f.writelines(data)
    return file_path

def test_getting_date_deep(sample_sources_file):
    expected_result = {
        "https://github.com/example/repo1": " abc123",
        "https://github.com/example/repo2": " def456"
    }
    assert getting_date_deep(sample_sources_file) == expected_result

def test_getting_date_deep_with_build_number(sample_sources_file):

        pass
