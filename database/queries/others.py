from translations import get_string, toggle_language

def options():
    """Provides access to user preferences."""
    if input(get_string('options')) == '1':
        toggle_language()
        return get_string('toggledLanguage')
    return None

def statistics():
    """Returns statistics of past user performance."""
    return None
