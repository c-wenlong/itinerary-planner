import streamlit as st

prices_colors = {
    "free": "blue", # Blue
    "$": "#4CAF50",  # Green
    "$$": "#FF9800",  # Orange
    "$$$": "#F44336",  # Red
}

intensity_colors = {
    "Low": "#4CAF50",  # Green
    "Moderate": "#FF9800",  # Orange
    "High": "#F44336",  # Red
}


def create_event_card(event):
    card_html = f"""
    <div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; margin: 10px 0; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1)">
        <div style="display: flex; justify-content: space-between; align-items: start">
            <h3 style="color: #1E88E5; margin: 0 0 8px 0">{event['name']}</h3>
            <span style="background-color: {get_price_color(event['price_range'])}; color: white; padding: 4px 8px; border-radius: 4px; font-size: 14px">{event['price_range']}</span>
        </div>
        <p style='color:#666; margin:8px 0; font-size:14px;'>{event['description']}</p>
       <div style='display:flex; justify-content:space-between; align-items:center; color:#555; font-size:14px; margin:1rem 0;'>
            <div>📍 {event['location']} ({event['area']})</div>
            <div>⏱️ {event['duration_hours']} hours</div>
        </div>
        <div style='display:flex; flex-wrap:wrap; gap:8px; margin:1rem 0;'>
            {create_tags_html(event['tags'])}
        </div>
        <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #eee; color: #666; font-size: 14px">
            <span style="background-color: {get_intensity_color(event['intensity_level'])}; color: white; padding: 2px 6px; border-radius: 4px; font-size: 12px">{event['intensity_level'].upper()}</span>
            <span style="margin-left: 12px">Suitable for: {', '.join(event['suitable_for'])}</span>
        </div>
    </div>
    """
    return card_html


def get_price_color(price_range):
    return prices_colors.get(price_range, "#757575")


def get_intensity_color(intensity):
    return intensity_colors.get(intensity, "#757575")


def create_tags_html(tags):
    return "".join(
        [
            f'<span style="background-color: #E3F2FD; color: #1E88E5; padding: 4px 8px; margin-right: 6px; border-radius: 12px; font-size: 12px; display: inline-block">{tag}</span>'
            for tag in tags
        ]
    )


def test_price_element():
    prices = "".join(
        [
            f'<span style="background-color: {colour}; color: white; padding: 4px 8px; border-radius: 4px; font-size: 14px">{price}</span>'
            for (price, colour) in prices_colors.items()
        ]
    )
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; margin: 10px 0; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1)">
            <div style="display: flex; justify-content: space-between; align-items: start">
                {prices}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def test_intensity_element():
    intensities = "".join(
        [
            f'<span style="background-color: {colour}; color: white; padding: 4px 8px; border-radius: 4px; font-size: 14px">{intensity}</span>'
            for (intensity, colour) in intensity_colors.items()
        ]
    )
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; margin: 10px 0; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1)">
            <div style="display: flex; justify-content: space-between; align-items: start">
                {intensities}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def test_elements():
    test_price_element()
    test_intensity_element()


if __name__ == "__main__":
    # Example usage
    event = {
        "name": "Monster Curry",
        "price_range": "$$",
        "description": "Grab a hearty meal at Monster Curry in the afternoon with Kai.",
        "location": "Tampines Mall, Level 1-32",
        "area": "Tampines",
        "duration_hours": 2,
        "tags": ["Food", "Spicy", "Mall"],
        "intensity_level": "low",
        "suitable_for": ["Beginners", "Intermediates"],
    }

    # Display the card
    st.markdown(create_event_card(event), unsafe_allow_html=True)

    test_elements()
