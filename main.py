import requests


def find_hero_max_intelligence():
    heroes = ['Hulk', 'Captain America', 'Thanos']
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url=url)

    hero_max_intelligence = max([(hero['name'], hero['powerstats']['intelligence']) for hero in resp.json() if hero['name'] in heroes])[0]
    return hero_max_intelligence


if __name__ == '__main__':
    print('Cамый умный герой:', find_hero_max_intelligence())
