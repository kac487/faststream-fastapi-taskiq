from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    # Postgres connection string
    postgres_url: str = (
        "postgresql://postgres:password@localhost:4433/postgres?schema=public"
    )

    # Nats connection string
    nats_url: str = "nats://localhost:4222"

    # Axon settings
    axon_client_id: str = ""
    axon_client_secret: str = ""
    axon_partner_id: str = ""
    axon_agency_uri: str = ""
    axon_token_refresh_interval: int = 3600

    # Job settings
    axon_evidence_process_all: bool = False
    axon_evidence_capture_devices: str = "axonbody"
    # axon_evidence_monitoring_interval_sec: int = 12000
    # axon_evidence_monitoring_backdate_days: int = 8

    # Azure Blob Storage
    azure_account_name: str = "devstoreaccount1"
    azure_account_key: str = ""
    azure_default_endpoints_protocol: str = "http"
    azure_blob_endpoint: str = "http://localhost:10000/devstoreaccount1"
    azure_queue_endpoint: str = "http://localhost:10001/devstoreaccount1"
    azure_table_endpoint: str = "http://localhost:10002/devstoreaccount1"


env = Settings()
