from services import fetch_all_events
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import time
import streamlit as st


st.set_page_config(
    page_title="Singapore Event Assistant",
    page_icon=":cityscape:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_table(all_data):
    display_df = pd.DataFrame(all_data)
    gb = GridOptionsBuilder.from_dataframe(display_df)

    # Ensure columns are sortable
    gb.configure_default_column(
        wrapText=True,
        autoHeight=True,
        maxWidth=500,
        groupable=True,
        cellStyle={"white-space": "pre-wrap"},
        sortable=True,  # Make columns sortable
    )

    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_side_bar(filters_panel=True, columns_panel=True)

    gridOptions = gb.build()

    AgGrid(
        display_df,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=True,
        height=500,
        theme="streamlit",
        key="ag_grid_" + str(time.time()),
    )


def load_database_events():
    # Get points from Qdrant
    points = fetch_all_events()

    # Process all events
    all_data = []
    for point in points:  # Access the Record objects
        display_data = {
            "Event ID": point.get("event_id", "N/A"),
            "Name": point.get("name", "N/A"),
            "Category": point.get("category", "N/A"),
            "Subcategory": point.get("subcategory", "N/A"),
            "Description": point.get("description", "N/A"),
            "Location": point.get("location", "N/A"),
            "Area": point.get("area", "N/A"),
            "Price Range": point.get("price_range", "N/A"),
            "Actual Price": point.get("actual_price", "N/A"),
            "Duration (Hours)": point.get("duration_hours", "N/A"),
            "Suitable For": ", ".join(point.get("suitable_for", [])),
            "Intensity Level": point.get("intensity_level", "N/A"),
            "Tags": ", ".join(point.get("tags", [])),
            "Created At": point.get("created_at", "N/A"),
        }
        all_data.append(display_data)

    return all_data


if __name__ == "__main__":
    all_data = load_database_events()
    load_table(all_data)
