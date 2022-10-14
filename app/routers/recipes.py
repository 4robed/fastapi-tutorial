import fastapi
from app.models.recipes import RECIPES


recipe_api = fastapi.APIRouter(prefix='/recipe')


@recipe_api.get('/{recipe_id}', status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    :param recipe_id:
    :return: recipe match with recipe_id
    """
    result = [rcp for rcp in RECIPES if rcp['id'] == recipe_id]
    if result:
        return result[0]


@recipe_api.get('/search', status_code=200)
def search_recipes(
    keyword: str | None = None,
    max_results: int | None = 10,
) -> dict:
    """
    Search recipe by keyword, with max_results
    :param keyword: Keyword to search
    :param max_results: support pagination
    :return: list of recipes or []
    """
    if not keyword:
        return {'results': RECIPES[:max_results]}
    results = filter(
        lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES
    )
    return {'results': list(results)[:max_results]}
