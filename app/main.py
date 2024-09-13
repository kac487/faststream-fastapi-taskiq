from fastapi import FastAPI
# from faststream.nats.fastapi import NatsRouter
from app.routes.hellos import router as hellos_router
from app.routes.goodbyes import router as goodbyes_router
from app.settings import env

# router = NatsRouter(env.nats_url)

app = FastAPI()
# app.include_router(router)
app.include_router(hellos_router)
app.include_router(goodbyes_router)
# app.include_router(application.routes.users.router)


