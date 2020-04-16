# загрузка базовых настроек для локального окружения
try:
    from what_to_cook.settings.base_settings import *
except ImportError:
    raise Exception('Please create base_settings.py file')

# загрузка настроек rest_framework
try:
    from what_to_cook.settings.rest_settings import *
except ImportError:
    raise Exception('Please create rest_settings.py file')

# загрузка настроек djoser
try:
    from what_to_cook.settings.djoser_settings import *
except ImportError:
    raise Exception('Please create djoser_settings.py file')

# загрузка настроек для разрешения всех кросдоменных запросов
try:
    from what_to_cook.settings.corsheaders_settings import *
except ImportError:
    raise Exception('Please create corsheaders_settings.py file')
