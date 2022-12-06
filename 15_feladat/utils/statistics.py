
def get_release_date(txt_data):
    for item in txt_data.split('\n'):
        if "[EBook #" in item:
            return int(item.replace('Release Date:', '').replace('Posting Date:', '')\
                .split("[")[0].split(" ")[-2])
    
    return False

def get_page_num(txt_data):
    import math
    return math.ceil(len(txt_data)/3000)

def get_five_char_words(txt_data):
    temp = []
    cnt = 0
    
    txt_data = txt_data.replace('.', '').replace(',', '')\
            .replace(':', '').replace('?', '')\
            .replace('!', '').replace('@', '')\
            .replace(';', '').replace("'", '')\
            .replace('"', '').replace('\n', ' ')
    
    for item in txt_data.split(' '):
        if len(item) > 5:
            cnt += 1
            temp.append(item)

    return cnt

if __name__ == '__main__':
    import os
    from file_handler import get_data_from_txt
    folder_path = r"C:\WORK\2022_oktober_python\15_feladat\books"


    files = [os.path.join(folder_path, item) for item in os.listdir(folder_path) if item.endswith(".txt")]

    for item in files[0:]:       
        data = get_data_from_txt(item)

        json_path = item.replace("txt", "json")
        # itt fogom a statisztikákat előállítani

        # print(get_five_char_words(data))
        print(get_release_date(data))