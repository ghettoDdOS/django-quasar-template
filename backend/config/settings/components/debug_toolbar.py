def custom_show_toolbar(request):
    from debug_toolbar.middleware import show_toolbar

    return show_toolbar(request)


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": custom_show_toolbar}
