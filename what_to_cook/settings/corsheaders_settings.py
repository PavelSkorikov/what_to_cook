from .base_settings  import MIDDLEWARE

# мидлваре для разрешения кросдоменных запросов
MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')
# разрешает все кросдоменные запросы
CORS_ORIGIN_ALLOW_ALL = True