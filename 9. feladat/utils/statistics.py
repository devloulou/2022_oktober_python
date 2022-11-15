"""
This module represent functions that can be used for creating statistincs regarding txt investigation
"""

def create_min_max_stat(txt_data):
    rows = txt_data.split('\n')

    min_row = len(rows[0])
    max_row = 0
    temp = {}
    for idx, item in enumerate(rows):
        if min_row > len(item) and len(item) != 0:
            min_row = len(item)
            temp['min_row'] = {"row": idx + 1, "value": item}
        if len(item) > max_row:
            max_row = len(item)
            temp['max_row'] = {"row": idx + 1, "value": item}

    return temp


def create_page_num_stat(txt_data):
    return len(txt_data)/3000

def create_most_common_words_stat(txt_data):
    pass


if __name__ == '__main__':
    from file_handler import read_txt

    file_path = r"C:\WORK\2022_oktober_python\9. feladat\Dracula.txt"
    data = read_txt(file_path)

    sol = create_min_max_stat(data)

    sol = create_page_num_stat(data)
    print(sol)