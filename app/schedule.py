from taskiq_faststream import BrokerWrapper
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_faststream import StreamScheduler
from faststream.nats import NatsBroker
from app.settings import env

# Taskiq Scheduler --------
broker = NatsBroker(env.nats_url)

tiq_broker = BrokerWrapper(broker)


tiq_broker.task(
    message={"msg": 123},
    subject="hello",
    schedule=[{"cron": "* * * * *"}],
)

scheduler = StreamScheduler(
    broker=tiq_broker,
    sources=[LabelScheduleSource(tiq_broker)],
)