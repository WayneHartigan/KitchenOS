import fileinput
import re


def format_file_lines(file):
    """
    :param file: file_object
    :return: list_of_choices: [(1, 'MM'), (2, 'VV')]
    Formats file correctly to be checked
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
    """
    :param answer: "VVMVV"
    :param max_length: 5
    :return: answer
    """
    # If returned ans == "" or
    # If the length of the answer is not equal to the required curries
    # return "No solution exists"
    if len(answer) == 0 or len(answer) != max_length:
        answer = "No solution exists"
    return answer


def sort_curry_choices(curry_preferences):
    ans = ""
    # Get the max length from first line
    # This also reads the first line, will not be read by rest of code
    max_length = int(curry_preferences.readline().strip())
    list_of_pref = format_file_lines(curry_preferences)

    # Loop through each number to check the preferred curry
    for _, pref in list_of_pref:
        # If preference is only one curry choose that curry
        # E.g "MMM" == "M" or "VV" == "V"
        if "M" not in pref or "V" not in pref:
            ans = ans + pref[0]
        else:
            # If pref == "VM" and only 1 can be chosen, no solution exists
            if len(pref) == 2 and max_length == 1:
                return "No solution exists"
            # Otherwise V can be assumed to be correct
            ans = ans + "V"
    return check_for_no_solution(ans, max_length)


if __name__ == "__main__":
    """
    python3 curry_wholesaler_problem.py test_files/test_1.txt
    """
    curry_preferences = fileinput.input()
    print(sort_curry_choices(curry_preferences))
