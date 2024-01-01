import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Function to read text from a file
def read_text_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.readlines()
        return text
    except FileNotFoundError:
        return None

# Preprocess the text using spaCy
def preprocess_text(text_lines):
    preprocessed_lines = []
    for line in text_lines:
        doc = nlp(line)
        # Remove stopwords and punctuation, and lemmatize
        tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        preprocessed_lines.append(' '.join(tokens))
    return preprocessed_lines

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")

    text_lines = read_text_from_file(input_file)

    if text_lines:
        # Preprocess all the lines
        preprocessed_lines = preprocess_text(text_lines)

        # Specify the number of clusters
        num_clusters = 5  # You can adjust this as needed

        # Vectorize the text data using TF-IDF
        vectorizer = TfidfVectorizer(max_df=0.85, max_features=5000)
        tfidf_matrix = vectorizer.fit_transform(preprocessed_lines)

        # Perform K-Means clustering
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(tfidf_matrix)

        # Create a list of clustered text
        clustered_text = [[] for _ in range(num_clusters)]
        for i, label in enumerate(cluster_labels):
            clustered_text[label].append(text_lines[i])

        # Write the clustered output to separate text files
        for cluster_num, text_in_cluster in enumerate(clustered_text):
            output_file = os.path.join(script_dir, f"cluster_{cluster_num + 1}.txt")
            with open(output_file, 'w', encoding='utf-8') as file:
                file.writelines(text_in_cluster)

            print(f"Cluster {cluster_num + 1} saved to {output_file}")
    else:
        print(f"Input file {input_file} not found. Please make sure it exists.")

if __name__ == "__main__":
    main()
