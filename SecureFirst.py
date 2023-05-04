# This project was developed for and used in the 2021 cyber defense competition.
# Make sure python3 is installed and run this program as root or with sudo.
# Run this as: sudo python3 SecureFirst.py

import os


def main():
    # Print header for program.
    print("\n", "*" * 10, "Starting The Program", "*" * 10, "\n")

    # Make backups of the scored service's config files.
    svc_config_backup = input(
        "\n>>> Create backups of config files? Type y or n, then hit enter:  "
    )
    if svc_config_backup == "y":
        svc_name = input(
            "\n>>> What is the scored service? Type openvpn, wordpress, mysql, or docker:  "
        )
        if svc_name == "openvpn":
            os.system("cp -r /etc/openvpn /home/openvpn")
            print("\n>>> backups saved to /home/openvpn")
        elif svc_name == "wordpress":
            os.system("cp -r /etc/apache2/apache2.conf /home/apache")
            print("\n>>> backups saved to /home/apache")
        elif svc_name == "mysql":
            os.system("cp -r /etc/my.cnf /home/mysql")
            print("\n>>> backups saved to /home/mysql")
        elif svc_name == "docker":
            os.system("cp -r /etc/docker /home/docker-frometc")
            os.system("cp -r /var/lib/docker /home/docker-fromvar")
            print("\n>>> backups saved to /home/docker")
        else:
            print("\n>>> Unknown service.")
    else:
        print("\n>>> OK")

    # Change password.
    current_pwd_change = input(
        "\n>>> Change current user's pwd? Type y or n, then hit enter:  "
    )
    if current_pwd_change == "y":
        os.system("passwd")
    else:
        print("\n>>> OK")

    # List current users.
    print("\n>>> Here are the current users and last REMOTE logins: ", "\n")
    os.system("lastlog")

    # Change another user's password.
    user_pwd_repeat = "y"
    while user_pwd_repeat == "y":
        other_pwd_change = input(
            "\n>>> Change other users pwd? Type y or n, then hit enter:  "
        )
        if other_pwd_change == "y":
            user_name = input("\n>>> Which user? Type name, then hit enter:  ")
            os.system("passwd " "%s" % (user_name))
        else:
            print("\n>>> OK")

        # Ask to repeat user password change.
        user_pwd_repeat = input(
            "\n>>> Enter y to go back and change a user's pwd, enter or n to move on:  "
        )

    # Show users with bash.
    print("\n>>> Here are the users with shell access:\n")
    os.system("cat /etc/passwd | grep bash")

    user_del_repeat = "y"
    while user_del_repeat == "y":
        del_user = input("\n>>> Delete a user? Type y or n, then hit enter:  ")
        if del_user == "y":
            user_del_name = input("\n>>> Which user? Type name, then hit enter:  ")
            os.system("userdel " "%s" % (user_del_name))
            print("\n>>> User " + user_del_name + " deleted sucessfully. ")
        else:
            print("\n>>> OK")

        # Ask to repeat user deletetion.
        user_del_repeat = input(
            "\n>>> Enter y to go back and delete a user, or enter n to move on:  "
        )

    # Show services running.
    services_show = input("\n>>> Show all services? Type y or n, then hit enter:  ")
    if services_show == "y":
        os.system("service --status-all | grep '\[ + \]'")
    else:
        print("\n>>> OK")

    # Disable a service.
    service_dis_repeat = "y"
    while service_dis_repeat == "y":
        service_disable = input(
            "\n>>> Stop / Disable a service (SSH, FTP, RDP, HTTP)? Type y or n, then hit enter:  "
        )
        if service_disable == "y":
            service_dis_name = input(
                "\n>>> Which service? Type name from above and hit enter:  "
            )
            service_cmd = input(
                "\n>>> Does this distro use systemctl? Type y or n, then hit enter:  "
            )
            if service_cmd == "y":
                os.system("systemctl stop " "%s" % (service_dis_name))
                os.system("systemctl disable " "%s" % (service_dis_name))
            else:
                os.system("stop " "%s" % (service_dis_name))
            print(
                "\n>>> Service "
                + service_dis_name
                + " stopped / disabled successfully. "
            )
        else:
            print("\n>>> OK")

        # Ask to repeat service disable.
        service_dis_repeat = input(
            "\n>>> Enter y to go back and disable a service, or enter n to move on:  "
        )

    # Install packages.
    print(
        "\nThe following packages will be installed: ufw, fail2ban, net-tools, nmap, and a few more."
    )
    package_mgr = input(
        "\n>>> Which package manager is used? Type apt or yum, then hit enter:  "
    )
    if package_mgr == "apt":
        os.system("apt-get install nano ufw fail2ban net-tools nmap wget curl -y")
    elif package_mgr == "yum":
        os.system("yum install nano ufw fail2ban net-tools nmap wget curl -y")
    else:
        print("\n>>> Unknown package manager.")

    # Update System.
    sys_update = input("\n>>> Update system? Type y or n, then hit enter:  ")
    if sys_update == "y":
        if package_mgr == "apt":
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
        elif package_mgr == "yum":
            os.system("yum install update -y")
            os.system("yum install upgrade -y")
        else:
            print("\n>>> OK")
    else:
        print("\n>>> OK")

    # Print footer for program.
    print("\n", "*" * 10, "Closing The Program", "*" * 10, "\n")


main()
