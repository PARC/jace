import json
from pprint import pprint

"""tool"""


def make_content_sequence(file_name, start, end, new_name):
    with open(file_name, "r") as data_file:
        data = json.load(data_file)
    newDataList = []
    for i in range(start, end):
        for item in data['sequences']:
            item['askDate'] = str(i)
            item['expireDate'] = str(i)
            newDataList.append(item.copy())
    newDictList = {"sequences": newDataList}

    with open(new_name, "w") as outfile:
        json.dump(newDictList, outfile)


if __name__ == "__main__":
    make_content_sequence(input("File Name? (include .json) "), input("Start Date?"), input("End Date? "),
                          "New File Name? (include.json) ")
