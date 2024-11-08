import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
def main():
    url_to_scrape = input("Enter in the link in concern from ycombinator's Ask HN: Who is hiring? section: ")
    response = requests.get(url_to_scrape)
    soup = BeautifulSoup(response.content, "html.parser")
    elems = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elems]
    key_words = {"python": 0, "javascript": 0, "typescript": 0, "ruby": 0, "rust": 0, "java": 0, "c": 0, "c#": 0, "c++": 0, "swift": 0, "react": 0, "postgresql": 0, "docker": 0, "aws": 0}
    for comment in comments:
        text_in_comment = comment.get_text().lower()
        words_in_text = text_in_comment.split(" ")
        words_in_text = {word.strip(".,/:;!@") for word in words_in_text}
        for key_word in key_words:
            if key_word in words_in_text:
                key_words[key_word] += 1
    plt.bar(key_words.keys(), key_words.values())
    plt.xlabel("Language/Asset")
    plt.ylabel("Number of Mentions")
    plt.title("Insights of Most Sought After Technological Skills")
    plt.show()

if __name__ == "__main__":
    main()