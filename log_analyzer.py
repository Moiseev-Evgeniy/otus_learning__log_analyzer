import argparse

from src.app.log_analyzer import update_config, event_logging, main

from structlog.processors import format_exc_info

config = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "reports",
    "LOG_DIR": "logs",
    "SELF_LOG_DIR": "logs",
    "TEMPLATES_DIR": "templates",
    "ERROR_THRESHOLD": 0.5,
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="src/app/config.json", help="path from root dir to config file")
    args = parser.parse_args()

    update_config(config, args.config)

    try:
        main(config)
    except Exception:
        event_logging(config, "Unexpected error", "error", format_exc_info(None, None, {"exc_info": True}))