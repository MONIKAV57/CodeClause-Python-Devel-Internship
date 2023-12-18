import re
from collections import Counter
import math

def get_cosine(vec1, vec2):
    intersection = set(vec1) & set(vec2)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1])
    sum2 = sum([vec2[x] ** 2 for x in vec2])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = re.compile(r'\w+').findall(text)
    return Counter(words)

def main():
    # Get input from users
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # Convert texts to vectors
    vector1 = text_to_vector(text1.lower())
    vector2 = text_to_vector(text2.lower())

    # Calculate cosine similarity
    cosine = get_cosine(vector1, vector2)

    # Define a threshold for similarity
    similarity_threshold = 0.2

    # Check for plagiarism
    if cosine > similarity_threshold:
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")

if __name__ == "__main__":
    main()
