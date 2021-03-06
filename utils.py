import json

__data = []


def load_candidates_from_json(path):  # возвращает список всех кандидатов
    global __data  # data объявлена вне функции(изменения будут как здесь и извне)
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):  # возвращает одного кандидата по его id
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return {"not found": "не найден"}


def get_candidates_by_name(candidate_name):  # возвращает кандидатов по имени
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]
    # "Списковое включение" (одной строкой тоже можно)


def get_candidates_by_skill(skill_name):  # возвращает кандидатов по навыку
    candidates = []
    for candidate in __data:
        skills = candidate["skills"].lower().split(", ")  # делим список навыков ч/з пробел
        if skill_name.lower() in skills:  # проверяем наличие навыков в списке
            candidates.append(candidate)
            return candidates
