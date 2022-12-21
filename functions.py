import json


def load_post() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def search_word(word: str) -> list[dict]:
    final_list = []
    for i in load_post():
        if word.lower() in i['content'].lower():
            final_list.append(i)
    return final_list


def add_post(post: dict) -> dict:
    posts: list[dict] = load_post()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False)
    return post
