import fileinput
import re


def format_file_lines(file, max_length):
    """
    :param file: file_object
    :return: list_of_choices: [(1, 'MM'), (2, 'VV')]
    Formats file correctly to be checked
    """
    list_of_choices = {}
    for line in file:
        # Coverts string line to a list of "num:choice"
        # "1 V 3 M" -> ["1V", "3M"]
        choices = re.findall(r"(\d+[VM])", line.strip().replace(" ", ""))
        for curry_choice in choices:
            # Gets the index from choice
            # "12M" == 12
            index = int(curry_choice[:-1])
            try:
                # Get previous use of key and concat preview value with new
                list_of_choices[index] = list_of_choices[index] + curry_choice[-1]
            except KeyError:
                # First time this key has been used
                list_of_choices[index] = curry_choice[-1]

    # Raise early if not number of choices does not match required
    if len(list_of_choices) != max_length:
        raise AssertionError

    # Returns a sorted list of all choices: [(1, 'MM'), (2, 'VV')]
    return sorted(list_of_choices.items())


def sort_curry_choices(curry_preferences):
    try:
        ans = ""
        # Get the max length from first line
        # This also reads the first line, will not be read by rest of code
        max_length = int(curry_preferences.readline().strip())
        list_of_pref = format_file_lines(curry_preferences, max_length)

        # Loop through each number to check the preferred curry
        for _, pref in list_of_pref:
            # If preference is only one curry choose that curry
            # E.g "MMM" == "M" or "VV" == "V"
            if "M" not in pref or "V" not in pref:
                ans = ans + pref[0]
            else:
                # If pref == "VM" and only 1 can be chosen, no solution exists
                if len(pref) == 2 and max_length == 1:
                    raise AssertionError
                # Otherwise V can be assumed to be correct
                ans = ans + "V"
        # If no ans is returned, no solution exists
        if len(ans) == 0:
            raise AssertionError

        # return answer: "VVVM"
        return ans

    except AssertionError:
        # Any AssertionErrors raised means no solution exists
        return "No solution exists"


if __name__ == "__main__":
    """
    python3 curry_wholesaler_problem.py test_files/test_1.txt
    """
    curry_preferences = fileinput.input()
    print(sort_curry_choices(curry_preferences))
