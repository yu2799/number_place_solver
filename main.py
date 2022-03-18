from requests import post
from json import dumps
from os import environ
# from dotenv import load_dotenv


def main():
    # load_dotenv()
    URL = environ["ENDPOINT"]
    main_content = {'content': '送るテキスト'}
    headers = {'Content-Type': 'application/json'}

    response = post(
        URL, dumps(main_content), headers=headers)


if __name__ == '__main__':
    main()
