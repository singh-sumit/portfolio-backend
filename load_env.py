from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

