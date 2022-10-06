from fastapi import FastAPI, APIRouter

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


app.include_router(api)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'run:app',
        host='0.0.0.0',
        port=5000,
        log_level='debug',
        reload=True,
        workers=1,
    )
