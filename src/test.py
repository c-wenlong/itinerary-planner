from services import text_to_structured_output

if __name__ == "__main__":
    # test text_to_structured_output
    activity_prompt = "Name: Hiking\nCategory: Outdoor\nDuration: 2.5\nDescription: Hiking is a great way to explore the outdoors and get some exercise."
    structured_output = text_to_structured_output(activity_prompt)
    print(structured_output)
