REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.IsAdminUser',
      'rest_framework.permissions.IsAuthenticated',
      'rest_framework.permissions.AllowAny',
    ),
    # это размер пагинатора (количество элементов на 1 странице)
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
      'rest_framework_json_api.parsers.JSONParser',
      'rest_framework.parsers.FormParser',
      'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}