import os

from utils.file_handler import read_txt, write_json
from utils.statistics import (create_min_max_stat,
                                create_page_num_stat,
                                create_most_common_words_stat)

# DRY: Don't Repeat Yourself

# CONSTANS:  nagy betűvel megadott, globális változók
FILE_PATH = os.path.join(os.path.dirname(__file__), "Dracula.txt")
STATISTICS_PATH = os.path.join(os.path.dirname(__file__), "statistics.json")

def main():
    data = read_txt(FILE_PATH)
    min_max = create_min_max_stat(data)
    page_num = create_page_num_stat(data)
    words_mc = create_most_common_words_stat(data)

    statistics = {
        'page_num': page_num,
        'most_common_words': words_mc,
        'min_max_rows': min_max }

    # statistics.update(min_max)
    write_json(STATISTICS_PATH, statistics)
    

main()