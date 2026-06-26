import os

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tests_data"
)


def test_generate_diff_general():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_1.txt")).read()
    )

def test_generate_diff_one_line():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.json"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_2.txt")).read()
    )

def test_generate_diff_empty():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_empty_1.json"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_3.txt")).read()
    )
