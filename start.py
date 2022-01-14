"""App entry point."""

"""App entry point."""
import sys

sys.path.append("./app")
from app.create_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
