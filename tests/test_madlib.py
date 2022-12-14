import os

import pytest

from madlib_cli.madlib import merge, parse_template, read_template, write_result_to_file


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)


def test_write_result_to_text_file():
    content = read_template("assets/dark_and_stormy_night_template.txt")
    template, parts = parse_template(content)
    result_string = merge(template, ("dark", "stormy", "night"))
    write_result_to_file("test.txt", result_string)
    expected = "It was a dark and stormy night."
    with open("test.txt", "r") as file:
        assert file.read() == expected
    os.remove("test.txt")
