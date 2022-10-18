from fastapi import FastAPI, APIRouter, Query, HTTPException
from schema.recipe import Recipe, RecipeSearchResults, RecipeCreate
from models import RECIPES

# init FastAPI app
app = FastAPI(title='FastAPI tutorial', openapi_url='/openapi.json')

api = APIRouter()


@api.get('/', status_code=200)
def hello_world() -> dict:
    """
    get index
    :return: Dict
    """
    return dict(message='Hello World!')


@api.get('/recipe/{recipe_id}', status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    :param recipe_id: int
    :return: Dict
    """
    result = [rcp for rcp in RECIPES if rcp['id'] == recipe_id]
    if not result:
        raise HTTPException(
            status_code=404, detail=f'Recipe with ID {recipe_id} not found'
        )
    return result[0]


@api.get('/search/', status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: str | None = Query(default=None, min_length=3, example='chicken'),
    max_results: int | None = 10,
) -> dict:
    """
    Search recipe by keyword, with max_results
    :param keyword:
    :param max_results:
    :return:
    """
    if not keyword:
        return {'results': RECIPES[:max_results]}
    results = filter(
        lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES
    )
    return {'results': list(results)[:max_results]}


@api.post('/recipe/', status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    """
    Create a new recipe (in memory only)
    :param recipe_in:
    :return:
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url
    ).dict()
    RECIPES.append(recipe_entry)
    return recipe_entry


app.include_router(api)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'run:app',
        host='0.0.0.0',
        port=8009,
        log_level='debug',
        reload=True,
        workers=1,
    )
