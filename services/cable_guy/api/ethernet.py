from . import manager


def post(body):
    """REST API Post method

    Args:
        body (dict): Check YAML description

    Returns:
        dict: Check YAML description
    """
    if manager.ethernetManager.set_configuration(body):
        manager.ethernetManager.save()
        return body, 200

    return body, 400

def search():
    """REST API Get method

    Returns:
        (dict, HTTP status code): Check YAML description
    """
    return manager.ethernetManager.get_interfaces(), 200
