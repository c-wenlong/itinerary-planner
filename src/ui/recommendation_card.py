def create_event_card(event):
    # CSS for the card
    card_html = f"""
    <div style="
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 10px 0;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <h3 style="color: #1E88E5; margin: 0 0 8px 0;">{event['name']}</h3>
            <span style="
                background-color: {get_price_color(event['price_range'])};
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 14px;">
                {event['price_range']}
            </span>
        </div>
        
        <p style="
            color: #666;
            margin: 8px 0;
            font-size: 14px;">
            {event['description']}
        </p>
        
        <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;
            color: #555;
            font-size: 14px;">
            
            <div>
                <i>📍</i> {event['location']} ({event['area']})
            </div>
            
            <div>
                <i>⏱️</i> {event['duration_hours']} hours
            </div>
        </div>
        
        <div style="
            margin-top: 12px;
            display: flex;
            flex-wrap: wrap;
            gap: 6px;">
            {create_tags_html(event['tags'])}
        </div>
        
        <div style="
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid #eee;
            color: #666;
            font-size: 14px;">
            <span style="
                background-color: {get_intensity_color(event['intensity_level'])};
                color: white;
                padding: 2px 6px;
                border-radius: 4px;
                font-size: 12px;">
                {event['intensity_level'].upper()}
            </span>
            <span style="margin-left: 12px;">Suitable for: {', '.join(event['suitable_for'])}</span>
        </div>
    </div>
    """
    return card_html

def get_price_color(price_range):
    colors = {
        "$": "#4CAF50",    # Green
        "$$": "#FF9800",   # Orange
        "$$$": "#F44336",  # Red
        "free": "#4CAF50"  # Green
    }
    return colors.get(price_range, "#757575")

def get_intensity_color(intensity):
    colors = {
        "low": "#4CAF50",      # Green
        "moderate": "#FF9800",  # Orange
        "high": "#F44336"      # Red
    }
    return colors.get(intensity, "#757575")

def create_tags_html(tags):
    tags_html = ""
    for tag in tags:
        tags_html += f"""
        <span style="
            background-color: #E3F2FD;
            color: #1E88E5;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;">
            {tag}
        </span>
        """
    return tags_html
