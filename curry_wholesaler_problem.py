import fileinput
import re


def format_file_lines(file):
    """
    :param file: file_object
    :return: list_of_choices: {1: 'MM', 2: 'VV'}
    """
    list_of_choices = {}
    for line in file:
        line = line.strip().replace(" ", "")
        choices = re.findall(r"(\d+[VM])", line.strip().replace(" ", ""))
        for curry_choice in choices:
            index = int(curry_choice[:-1])
            try:
                list_of_choices[index] = list_of_choices[index] + curry_choice[-1]
            except KeyError:
                list_of_choices[index] = curry_choice[-1]
    return sorted(list_of_choices.items())


def check_for_no_solution(answer, max_length):
    if len(answer) == 0 or len(answer) != max_length:
        answer = "No solution exists"
    return answer


def sort_curry_choices(curry_preferences):
    ans = ""
    max_length = int(curry_preferences.readline().strip())
    list_of_pref = format_file_lines(curry_preferences)
    for _, pref in list_of_pref:
        if "M" not in pref or "V" not in pref:
            ans = ans + pref[0]
        else:
            if len(pref) == 2 and max_length == 1:
                return "No solution exists"
            ans = ans + "V"
    return check_for_no_solution(ans, max_length)


if __name__ == "__main__":
    """
    python3 curry_wholesaler_problem.py test_files/test_1.txt
    """
    curry_preferences = fileinput.input()
    print(sort_curry_choices(curry_preferences))
