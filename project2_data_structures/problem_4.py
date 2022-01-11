class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_sub_child = Group('subsubchild')

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
sub_child.add_group(sub_sub_child)


def is_user_in_group(user, group):
    if user in group.users:
        return True
    elif len(group.groups) == 0:
        return False
    else:
        for subgroup in group.groups:
            return is_user_in_group(user, subgroup)


### TEST CASES ###

print(is_user_in_group(sub_child_user, parent))
# True

print(is_user_in_group('child_user', child))
# False

print(is_user_in_group('', sub_sub_child))
# False
