import datetime
import pandas as pd
import streamlit as st


def show_form():
    # We're adding activities via an `st.form` and some input widgets. If widgets are used
    # in a form, the app will only rerun once the submit button is pressed.
    with st.form("add_ticket_form"):
        issue = st.text_area("Describe the activity!", height=80)
        intensity = st.selectbox("Intensity", ["High", "Medium", "Low"])
        submitted = st.form_submit_button("Submit")

    if submitted:
        # Make a dataframe for the new ticket and append it to the dataframe in session
        # state.
        recent_ticket_number = int(max(st.session_state.df.ID).split("-")[1])
        today = datetime.datetime.now().strftime("%m-%d-%Y")
        df_new = pd.DataFrame(
            [
                {
                    "ID": f"TICKET-{recent_ticket_number+1}",
                    "Issue": issue,
                    "Status": "Open",
                    "Priority": intensity,
                    "Date Submitted": today,
                }
            ]
        )

        # Show a little success message.
        st.write("Ticket submitted! Here are the ticket details:")
        st.dataframe(df_new, use_container_width=True, hide_index=True)
        st.session_state.df = pd.concat([df_new, st.session_state.df], axis=0)
