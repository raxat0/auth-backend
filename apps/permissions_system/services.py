from .models import AccessRule


def has_permission(user, element_name, action):

    if not user:
        return False

    rule = AccessRule.objects.filter(
        role=user.role,
        element__name=element_name
    ).first()

    if not rule:
        return False

    permissions_map = {
        "read": rule.read_permission,
        "create": rule.create_permission,
        "update": rule.update_permission,
        "delete": rule.delete_permission,
    }

    return permissions_map.get(action, False)