
from faststream.nats.fastapi import Logger
from app.routes.nats_router import router
from app.settings import env


@router.subscriber("hello", queue="hello")
@router.get("/hello")
async def hello(msg, logger: Logger):
    
    logger.info("Hello ROUTE!")
    
    await router.broker.publish(
        message=msg,
        subject="goodbye"
    )
    return {"response": "Hello, ROUTE!"}



