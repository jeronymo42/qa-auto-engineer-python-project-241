import os

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tests_data"
)


def test_generate_diff():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "test_1_result.txt")).read()
    )
