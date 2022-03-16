from github import Github


g = Github("GH_TOKEN_TEST") # Your personal token

def change_protected_branch_settings():
    # Loops through all the repos and changes the /settings/branch_protection_rules/
    # CAREFUL with this!
    for repo in g.get_user().get_repos():
        branch = repo.get_branch("dev1")
        branch.edit_protection(required_approving_review_count=2, enforce_admins=True)
        print("Edited the branch protection rules for: " + repo.name)

def change_protected_branch_settings_test():
    repo = g.get_repo("Chandrasekhar674/secure-ghpages")
    branch = g.get_repo("Chandrasekhar674/secure-ghpages").get_branch("dev1")
    branch.edit_protection(required_approving_review_count=2, enforce_admins=True)

