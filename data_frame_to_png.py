import pandas as pd
import dataframe_image as dfi

from html_to_data_frame import html_to_data_frame


def data_frame_to_image(data_frame: pd.DataFrame, name_file):
    data_frame = data_frame.style.set_table_styles(
        [
            dict(
                selector='th',
                props=[
                    ('text-align', 'center'),
                    ('color', '#FFFFFF'),
                    ('background-color', '#004B49'),
                    ("row_heading", "50px")
                ]
             )
        ]
    )
    data_frame.set_properties(**{'width': '13em', 'text-align': 'center'}).hide(axis='index')
    pd.set_option('colheader_justify', 'center')
    dfi.export(data_frame, name_file)


def html_to_png(html_path: str, file_name: str) -> None:
    df = html_to_data_frame(html_path)
    data_frame_to_image(df, file_name)


if __name__ == '__main__':
    html_to_png("html_path", "file_name")
