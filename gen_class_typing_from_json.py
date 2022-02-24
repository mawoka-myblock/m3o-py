import json
import re

json_str = """
{

        "id": "df91a612-5b24-4634-99ff-240220ab8f55",

        "created": "1623677579",

        "expires": "1623699579",

        "userId": "8b98acbe-0b6a-4d66-a414-5ffbf666786f"

    }

"""


def main():
    json_dict = json.loads(json_str)
    for i in json_dict:
        term_str = re.compile("^<class \'(.+)\'>$").findall(str(type(json_dict[i])))[0]
        print(f"{i}: {term_str}")


if __name__ == '__main__':
    main()
