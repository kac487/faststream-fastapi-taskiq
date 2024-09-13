from faststream.nats.fastapi import NatsRouter, Logger

from app.settings import env
router = NatsRouter(env.nats_url)