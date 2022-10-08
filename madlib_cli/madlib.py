import re


def read_template(filepath):
    with open(filepath, "r") as file:
        return file.read()


def parse_template(template):
    matching_parts = re.findall(r"\{(.*?)\}", template)
    stripped_template = re.sub(r"\{(.*?)\}", "{}", template)
    return stripped_template, tuple(matching_parts)


def merge(template, parts):
    return template.format(*parts)


def write_result_to_file(filename, string):
    with open(filename, "w") as file:
        file.write(string)


welcome_message = """
Welcome to the Madlib CLI. You will be prompted to provide a series
of words from which the CLI will generate sentences
"""

if __name__ == '__main__':
    print(welcome_message)

    content = read_template("assets/make_me_a_video_game_template.txt")

    word_template, old_parts = parse_template(content)

    user_responses = []
    for part in old_parts:
        user_response = input(f"Enter {part}: ")
        user_responses.append(user_response)

    print("Your sentence is:")

    result = merge(word_template, tuple(user_responses))
    print(result)

    write_result_to_file("result.txt", result)
