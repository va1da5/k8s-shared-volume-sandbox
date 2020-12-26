from app import app
from settings import SETTINGS

if __name__ == "__main__":
    app.run(port=int(SETTINGS["port"]), host="0.0.0.0")