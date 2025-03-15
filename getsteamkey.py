import json
import re
import yaml
import time
import requests
import os


key = "************"
steamid = "************"


def get_steam_data(key, steamid):
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1?include_appinfo=true&key={key}&steamid={steamid}&skip_unvettend_apps=false&include_played_free_games%3D1=true&format=json"
    response = requests.get(url)
    return json.loads(response.text)["response"]["games"]


def get_achievement_data(appid, key, steamid):
    achievement_url = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={appid}&key={key}&steamid={steamid}&l=zh_CN"
    res = requests.get(achievement_url)
    return json.loads(res.text)


def load_yaml_file(file_path):
    with open(file_path, "r", encoding="utf8") as file:
        return yaml.safe_load(file)


def save_yaml_file(file_path, data):
    with open(file_path, "w", encoding="utf8") as fw:
        yaml.dump(data, fw, allow_unicode=True, sort_keys=False)


def baike(en_name):
    url = f"https://baike.baidu.com/search/word?fromModule=lemma_search-box&word={en_name}"
    res = requests.request("get", url)
    pattern = r"<title>(.*?)_百度百科</title>"
    match = re.search(pattern, res.text)
    if match:
        return match.group(1)
    else:
        return en_name


def main(file):
    steam_data = get_steam_data(key, steamid)
    file_data = load_yaml_file(file)
    game_list = file_data[0]["steam"][0]["games_list"]

    for i, game in enumerate(steam_data):
        if i >= len(game_list):
            game_list.append({})

        game_list[i]["en_name"] = game.get("name", "")
        game_list[i]["name"] = baike(game.get("name", ""))
        appid = game.get('appid')
        if appid:
            game_list[i]["link"] = f"https://store.steampowered.com/app/{appid}"
            game_list[i]["img"] = f"https://cdn.cloudflare.steamstatic.com/steam/apps/{appid}/header.jpg"
        else:
            print("appid 不存在")
            break

        game_list[i]["totalTime"] = f"{round(game.get('playtime_forever', 0) / 60, 2)} 小时"
        game_list[i]["lastTime"] = time.strftime("%Y-%m-%d", time.localtime(game.get('rtime_last_played', 0))) if game.get(
            'rtime_last_played') else "从未运行"

        ach_res = get_achievement_data(appid, key, steamid)
        ach_data = ach_res.get("playerstats", {}).get("achievements", [])
        num = sum(1 for ach in ach_data if ach.get("achieved") == 1)
        game_list[i]["num"] = f"{num}/{len(ach_data)}"
        game_list[i]["achievement"] = f"{round(num / len(ach_data) * 100, 2) if ach_data else 0}%"

        print(f"完成进度: {i + 1} / {len(steam_data)}, 游戏名:{game.get('name')}")

    save_yaml_file(file, file_data)


if __name__ == '__main__':
    os.system("pip3 freeze > requirements.txt")
    main("source/_data/games.yml")
