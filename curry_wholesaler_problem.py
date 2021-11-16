import fileinput


def format_file_lines(curry_preferences):
    """
    :param curry_preferences: file_object
    :return: list_of_lines: [["1V", "2M"] ["3M", "4V"]]
    """
    list_of_lines = []
    for line in curry_preferences:
        if not curry_preferences.isfirstline():
            line = line.strip().replace(" ", "")
            list_of_lines.append([line[index: index + 2] for index in range(0, len(line), 2)])
    return list_of_lines


def sort_curry_choices(curry_preferences):
    curry_choices = []
    list_of_pref = format_file_lines(curry_preferences)
    for pref in list_of_pref:
        for choice in pref:
            if choice not in curry_choices:
                if "M" in choice:
                    if len(pref) == 1:
                        curry_choices.append(choice)
                else:
                    curry_choices.append(choice)

    # Formats list to string format ("VVVM")
    ans = ""
    for choice in curry_choices:
        ans = ans + choice[1]
    print(ans)
    return ans


if __name__ == "__main__":
    """
    python3 curry_wholesaler_problem.py test_files/test_1.txt
    """
    curry_preferences = fileinput.input()
    sort_curry_choices(curry_preferences)