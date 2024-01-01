import openai, os, spacy

nlp = spacy.load("en_core_web_sm")
api_key = "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"

def generate_summary(text):
    openai.api_key = api_key

    lines = text.splitlines()
    chunk_size = 20  # Number of lines in each chunk
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
    summary = []

    for chunk in chunks:
        chunk_text = "\n".join(chunk)

        prompt = f"""
        1. Hooks: {chunk_text}
        2. Introducing the guest: {chunk_text}
        3. Summarizing the manuscript: {chunk_text}
        4. The Topics: {chunk_text}
        5. The resources mentioned: {chunk_text}
        6. The CTAs: {chunk_text}
        7. Episode Transcript: {chunk_text}
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
        )

        summary.append(response.choices[0].text)
    return "\n".join(summary)

def read_text_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return None

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")
    output_file = os.path.join(script_dir, "output.txt")

    text = read_text_from_file(input_file)

    if text:
        doc = nlp(text)
        summary = generate_summary(text)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(summary)
        print(f"Summary saved to {output_file}")
    else:
        print(f"Input file {input_file} not found. Please make sure it exists.")

if __name__ == "__main__":
    main()