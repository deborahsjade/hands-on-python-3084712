import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"
FAKE_ENV = "Guitar time"


def print_env(env):
    if env == DEVELOPMENT:
        print("Development environment")
    elif env == PRODUCTION:
        print("Production environment")
    elif env == STAGING:
        print("Staging environment")
    elif env in [CODE_SPACE, LOCAL]:
        print("Codespace or local environment")
    else:
        print("Unknown environment")


print_env(os.environ.get("ENV_NAME", DEVELOPMENT))
print_env(os.environ.get("ENV_NAME", LOCAL))
print_env(os.environ.get("ENV_NAME", FAKE_ENV))
