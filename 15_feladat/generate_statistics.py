import os

from utils.file_handler import get_data_from_txt, write_json
from utils.statistics import get_release_date, get_page_num, get_five_char_words


def main():
    folder_path = r"C:\WORK\2022_oktober_python\15_feladat\books"

    files = [os.path.join(folder_path, item) for item in os.listdir(folder_path) if item.endswith(".txt")]

    oldest_release = {"title": "", "release": 0}
    youngest_release = {"title": "", "release": 0}
    longest = {"page_size": 0, "title": ""}
    shortest = {"page_size": 0, "title": ""}
    longest_title = {"title": "", "length": 0}
    most_five_words = {"words_num": 0, "title": ""}

    for idx, item in enumerate(files):
        data = get_data_from_txt(item)
        release_date = get_release_date(data)     
        page_num = get_page_num(data)
        title = item.split('\\')[-1].replace('.txt', '')
        five_words = get_five_char_words(data)

        if most_five_words["words_num"] < five_words or idx == 0:
            most_five_words["words_num"] = five_words
            most_five_words["title"] = title

        if longest_title['length'] < len(title) or idx == 0:
            longest_title['length'] = len(title) 
            longest_title['title'] = title

        if longest['page_size'] < page_num or idx == 0:
            longest['page_size'] = page_num
            longest['title'] = title

        if shortest['page_size'] > page_num or idx == 0:
            shortest['page_size'] = page_num
            shortest['title'] = title

        if oldest_release["release"] > release_date or idx == 0:
            oldest_release["title"] = title
            oldest_release["release"] = release_date

        if youngest_release["release"] < release_date or idx == 0:
            youngest_release["title"] = title
            youngest_release["release"] = release_date

        statistics = {
            "release_date": release_date,
            "page_num": page_num,
            "title": title
            }


        json_path = item.replace("txt", "json")

        write_json(json_path, statistics)

    overall_statistics = {   
        "longest_book": longest,
        "shortest_book": shortest, 
        "oldest_book": oldest_release, 
        "longest_title": longest_title,
        "legtobb_5_karakteres_szo": most_five_words
    }

    write_json(os.path.join(folder_path, "overall_statistics.json"), overall_statistics)


if __name__ == '__main__':
    main()
