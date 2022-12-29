import pandas as pd
from bs4 import BeautifulSoup


def html_to_data_frame(html_path: str) -> pd.DataFrame:
    # empty list
    data = []

    # for getting the header from
    # the HTML file
    list_header = []
    soup = BeautifulSoup(open(html_path), 'html.parser')
    header = soup.find_all("table")[0].find("tr")

    for items in header:
        try:
            if items != "\n":
                list_header.append(items.get_text())
        except Exception:
            continue

    # for getting the data
    HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                if sub_element != "\n":
                    sub_data.append(sub_element.get_text())
            except Exception:
                continue
        data.append(sub_data)

    df = pd.DataFrame(data=data, columns=list_header)
    df.to_csv("csv_name")  # if you need to save the data in a csv file, uncomment this line
    return df


if __name__ == '__main__':
    html_to_data_frame("test.html")
