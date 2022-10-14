from fastapi import FastAPI
from routers import hello_world_api, recipe_api


# Init FastAPI app
app = FastAPI(title='FastAPI tutorial', openapi_url='/openapi.json')

app.include_router(hello_world_api)
app.include_router(recipe_api)


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
