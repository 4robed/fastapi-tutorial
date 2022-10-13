from fastapi import FastAPI, APIRouter
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


@api.get('/recipe/{recipe_id}', status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    :param recipe_id: int
    :return: Dict
    """
    result = [rcp for rcp in RECIPES if rcp['id'] == recipe_id]
    if result:
        return result[0]


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
