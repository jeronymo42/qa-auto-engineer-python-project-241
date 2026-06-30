import os

from gendiff import generate_diff as gd

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "tests_data"
)


# json tests
def test_generate_diff_general_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_1.txt")).read()
    )


def test_generate_diff_one_line_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.json"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_2.txt")).read()
    )


def test_generate_diff_empty_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_empty_1.json"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.json"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_3.txt")).read()
    )


# yaml tests
def test_generate_diff_general_yaml():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file1.yaml"),
            os.path.join(TEST_DATA_DIR, "file2.yaml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_1.txt")).read()
    )


def test_generate_diff_one_line_yaml():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.yml"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.yml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_2.txt")).read()
    )


def test_generate_diff_empty_yaml():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_empty_1.yaml"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.yaml"),
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_3.txt")).read()
    )


# plain tests
def test_generate_diff_general_plain():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
            styler="plain",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_4.txt")).read()
    )


def test_generate_diff_one_line_plain():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.json"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.json"),
            styler="plain",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_5.txt")).read()
    )


def test_generate_diff_empty_plain():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_empty_1.json"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.json"),
            styler="plain",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_6.txt")).read()
    )


# json tests
def test_generate_diff_json_format_general_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file1.json"),
            os.path.join(TEST_DATA_DIR, "file2.json"),
            styler="json",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_7.txt")).read()
    )


def test_generate_diff_json_format_one_line_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_one_line_1.json"),
            os.path.join(TEST_DATA_DIR, "file_one_line_2.json"),
            styler="json",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_8.txt")).read()
    )


def test_generate_diff_json_format_empty_json():
    assert (
        gd(
            os.path.join(TEST_DATA_DIR, "file_empty_1.json"),
            os.path.join(TEST_DATA_DIR, "file_empty_2.json"),
            styler="json",
        )
        == open(os.path.join(TEST_DATA_DIR, "result_test_9.txt")).read()
    )
