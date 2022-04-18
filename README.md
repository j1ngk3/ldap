# Ansible Role: ldap

An Ansible Role that installs Installs Open LDAP (slapd) as service on specified nodes and configures its structure and permissions to identify users and services among multiple domains on Linux.

## Requirements

python-ldap. See [prepare.yml](molecule/default/prepare.yml) for one example of installing.

## Role Variables

Define `organizations` in your playbook or inventory as array of domains and the role will configure the directory structure for all of them.

Generate a slapd compatible password via:
```
slappasswd -s password
```
and setting `ldap_password` to equal the output.

## Dependencies

None.

## Example Playbook

```
# playbook.yml
---
- name: Setup LDAP
  hosts: all
  become: yes
  vars:
    organizations:
      - example.com

  roles:
    - ldap

```

```
# LDAP Structure
dc=ldap
├─ ou=admin
├─ ou=services
└─ dc=example.com
   ├─ ou=groups
   └─ ou=users
```

## License

MIT

## Author Information

This role was created in 2017 by [Pavel Žák](https://github.com/just-paja), forked in 2022 by [j1ngk3](https://github.com/j1ngk3).