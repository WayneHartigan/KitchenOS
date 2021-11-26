import fileinput


def format_file_lines(curry_preferences):
    """
    :param curry_preferences: file_object
    :return: list_of_choices: {1: 'MM', 2: 'VV'}
    """
    list_of_choices = {}
    for line in curry_preferences:
        line = line.strip().replace(" ", "")
        if not curry_preferences.isfirstline():
            for curry_choice in [line[index: index + 2] for index in range(0, len(line), 2)]:
                try:
                    list_of_choices[curry_choice[0]] = list_of_choices[curry_choice[0]] + curry_choice[1]
                except KeyError:
                    list_of_choices[curry_choice[0]] = curry_choice[1]
    return list_of_choices


def sort_curry_choices(curry_preferences):
    curry_choices = {}
    list_of_pref = format_file_lines(curry_preferences)
    for key, pref in list_of_pref.items():
        if "M" not in pref:
            curry_choices[key] = "V"
        if "V" not in pref:
            curry_choices[key] = "M"
        else:
            pass
            # Logic for finding most efficient
    ans = ""
    for key, pref in sorted(curry_choices.items()):
        ans = ans + pref
    return ans


if __name__ == "__main__":
    """
    python3 curry_wholesaler_problem.py test_files/test_1.txt
    """
    curry_preferences = fileinput.input()
    sort_curry_choices(curry_preferences)
