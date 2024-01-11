for x in range(2, 30):
    url = f"https://podrocket.logrocket.com/page/{x}"
    with open("Podcasts.txt", "a", encoding="utf-8") as f:
        f.write(url + "\n")
