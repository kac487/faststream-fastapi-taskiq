
To run the task scheduler run
```bash
taskiq scheduler -fsd app.schedule:scheduler
```

To run the fastapi application run
```bash
fastapi run app/main.py
```

when these are run simulanaously they can be used to trigger routes
- on a fixed schedule
- on a subscription to a NATS topic
- on a http request
