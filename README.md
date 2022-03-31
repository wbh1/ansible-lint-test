# Ansible Lint Bug Demonstration

Reproduction Steps:
1. `ansible-lint -vvv`
   1. Does not lint `tasks` files
2. Comment out the `handlers` block in `roles/cleanup/tasks/uninstall.yml`
3. `ansible-lint -vvv`
   1. Successfully lints all files.
