import os

from gendiff import generate_diff

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tests_data"
)


# json tests
def test_generate_diff_general_json():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_1.txt")).read()
    )

def test_generate_diff_one_line_json():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.json"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_2.txt")).read()
    )

def test_generate_diff_empty_json():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_empty_1.json"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_3.txt")).read()
    )

# yaml tests
def test_generate_diff_general_yaml():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file1.yaml"),
            os.path.join(TEST_DATA_DIR, "file2.yaml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_1.txt")).read()
    )

def test_generate_diff_one_line_yaml():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.yml"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.yml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_2.txt")).read()
    )

def test_generate_diff_empty_yaml():
    assert (
        generate_diff(
            os.path.join(TEST_DATA_DIR, "file_empty_1.yaml"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.yaml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_3.txt")).read()
    )