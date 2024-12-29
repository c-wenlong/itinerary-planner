import streamlit as st
import streamlit.components.v1 as components

GOOGLE_MAPS_API_KEY = st.secrets["MAPS"]["GOOGLE_MAPS_API_KEY"]


def update_place(place_data):
    st.session_state.selected_place = place_data


def show_google_maps_search():
    # Initialize session state
    if "selected_place" not in st.session_state:
        st.session_state.selected_place = None

    search_result = components.html(
        f"""
        <div style="position: relative; z-index: 1">
            <text for="searchBox" style="display: none">Search for a location</text>
            <input id="searchBox" type="text" placeholder="Search for a location" 
                style="width: 100%; padding: 0.5rem 0.75rem; color: rgb(49, 51, 63); 
                background-color: rgb(255, 255, 255); border: 1px solid rgb(223, 227, 235); 
                border-radius: 0.5rem; line-height: 1.5; font-size: 14px; 
                font-family: 'Source Sans Pro', sans-serif; 
                transition: border-color 0.2s ease-in-out; 
                box-shadow: rgb(0 0 0 / 0%) 0px 0px 0px;" 
                onmouseover="this.style.borderColor='rgb(128, 132, 149)'" 
                onmouseout="this.style.borderColor='rgb(223, 227, 235)'" 
                onfocus="this.style.borderColor='rgb(255, 75, 75)'; 
                this.style.boxShadow='rgb(255 75 75 / 20%) 0px 0px 0px 0.2rem'" 
                onblur="this.style.borderColor='rgb(223, 227, 235)'; 
                this.style.boxShadow='none'">
        </div>
        <script async
            src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}&libraries=places&callback=initAutocomplete">
        </script>
        <script>
            function initAutocomplete() {{
                const input = document.getElementById('searchBox');
                const options = {{
                    fields: ['formatted_address', 'geometry', 'name', 'place_id'],
                    strictBounds: false,
                    types: ['establishment', 'geocode']
                }};

                const autocomplete = new google.maps.places.Autocomplete(input, options);
                autocomplete.addListener('place_changed', function() {{
                    const place = autocomplete.getPlace();
                    if (!place.geometry) {{
                        console.log('No place geometry available');
                        return;
                    }}

                    const placeData = {{
                        name: place.name,
                        formatted_address: place.formatted_address,
                        place_id: place.place_id,
                        lat: place.geometry.location.lat(),
                        lng: place.geometry.location.lng()
                    }};

                    // Use Streamlit's component communication
                    window.parent.Streamlit.setComponentValue(placeData);
                }});
            }}
        </script>
        """,
        height=150,
    )

    # Update session state if we got a result
    if search_result is not None:
        st.session_state.selected_place = search_result
        st.rerun()


def main():
    st.title("Location Search")

    show_google_maps_search()

    # Display the selected place information
    if st.session_state.selected_place:
        st.write("Selected Location:")
        st.json(st.session_state.selected_place)

    st.markdown(st.session_state.selected_place)


if __name__ == "__main__":
    main()
