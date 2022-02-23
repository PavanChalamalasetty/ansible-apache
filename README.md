dd-ansible-role-httpd
===============

Ansible playbook role for building and configuring apache httpd servers.

Requirements
------------
- ansible
- ansible-framework
- ansible-role-common
- AWS - Servers tag: dd-ansible-role-httpd
- ansible_local.designator.environment should be defined


Default Variables
--------------

Structure
---------
<pre>
        JenkinsFile             	#  blank - uses Jenkensfile from jenkins_library
        tasks/                  	#
            main.yml            	#  <-- main playbook , calls sub tasks
            setup_rhel.yml      	#  <-- setup for rhel which calls httpd
        handlers/               	#
            main.yml            	#  <-- handlers file, service to restart httpd
        templates/              	#  <-- files for use with the template resource
            authorized_keys.j2		# 
            daemon.j2           	#  <------- templates end in .j2
        files/                  	#
            bar.txt             	#  <-- files for use with the copy resource
        defaults/               	#
            main/               	#  <-- variables associated with this role
               httpd.yml  	     	#  httpd related vars
               ansible.yml      	#  ansible vars
        vars/                   	#
            vars.yml            	#  <-- default lower priority variables for this role
        meta/                   	#
            main.yml            	#  <-- role dependencies
        library/                	# roles can also include custom modules
        module_utils/           	# roles can also include custom module_utils
        lookup_plugins/         	# or other types of plugins, like lookup in this case
</pre>

Example Playbook
----------------
Including an example of how to use the ansible tags:

    - name: set environment fact
      include_tasks: "configure_httpd.yml"
      tags:
        - daily
        - frequent

Usage
----------------
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tags: [ frequent, daily ]
      roles:
         - { ansible_role_httpd }
