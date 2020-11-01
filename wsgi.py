"""Application entry point."""
from dashboards import init_app
import config

app = init_app()

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=True)