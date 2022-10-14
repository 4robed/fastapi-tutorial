import fastapi


hello_world_api = fastapi.APIRouter()


@hello_world_api.get('/', status_code=200)
def hello_world() -> dict:
    """
    Hello World
    :return: message Hello world
    """
    return dict(message='Hello World!')
