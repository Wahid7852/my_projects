def compute_length(input_data):
    if isinstance(input_data, str):
        return f"The input is a string with length {len(input_data)}."
    elif isinstance(input_data, list):
        return f"The input is a list with length {len(input_data)}."
    else:
        return "Unsupported input type."

user_input = eval(input("Enter a string or a list: "))
result = compute_length(user_input)
print(result)
