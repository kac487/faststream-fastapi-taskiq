
from faststream.nats.fastapi import Logger
from app.routes.nats_router import router



@router.subscriber("goodbye", queue="goodbye")
@router.get("/goodbye")
async def goodbye(msg, logger: Logger):
    logger.info("Goodbye ROUTE!")
    return {"response": "Goodbye, ROUTE!"}