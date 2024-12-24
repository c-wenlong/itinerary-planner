import streamlit as st


def create_history_card(idx, prompt, response):
    return f"""
        <div style="padding: 12px 0; border-bottom: 1px solid #eee;">
            <p style="margin: 0 0 8px 0; color: #666;">
                {idx}. {prompt}
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {' '.join([
                    f'<span style="background: #f0f0f0; padding: 2px 8px; border-radius: 12px; font-size: 14px; font-weight: bold; color: #666;">{chip}</span>'
                        for chip in response
                ])}
            </div>
        </div>
    """


if __name__ == "__main__":
    history = {
        "prompt": "I wanna plan a date with someone called kai.",
        "response": ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"],
    }
    for idx, entry in enumerate([history], 1):
        st.markdown(create_history_card(idx, entry["prompt"], entry["response"]), unsafe_allow_html=True)
