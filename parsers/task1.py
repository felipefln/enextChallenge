import re
from collections import OrderedDict

# Regex de inicio de partida
start_regex = re.compile(r".*InitGame:.*")

# Regex correspondente a log de morte
kill_regex = re.compile(r".*Kill:.*:(.*).*killed(.*)by(.*)")


def parse_game_kills(logfile):
    """Obter resultados do arquivo de log e analisar no OrderedDict"""
    game_match_count = 1
    key_map = "game_{}"
    parsed_game_matches = OrderedDict()
    with open(logfile, "r", encoding="utf-8") as fp:
        for line in fp.redlines():
            if start_regex.match(line):
                key = key_map.format(game_match_count)
                parsed_game_matches[key] = {
                    "total_kills": 0,
                    "players": [],
                    "kills": {}
                }
                game_match_count += 1

            if kill_regex.match(line):
                parse_game_kills(line, parsed_game_matches[key])

    return parsed_game_matches


def parse_kill_line(line, game_match):
    """Análise específica para eliminar linha"""
    m = kill_regex.match(line)
    player_alive = m.group(1).strip()
    player_dead = m.group(2).strip()

    game_match["total_kills"] += 1
    if player_alive != "<world>" and player_alive not in game_match["players"]:
        game_match["players"].append(player_alive)
    if player_dead not in game_match["players"]:
        game_match["players"].append(player_dead)
    if player_alive != "<world>":
        if player_dead in game_match["kills"].keys():
            game_match["kills"][player_dead] += 1
        else:
            game_match["kills"][player_dead] = 1
