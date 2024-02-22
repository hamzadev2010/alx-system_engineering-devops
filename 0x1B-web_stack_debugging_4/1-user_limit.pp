#e the OS configuration so that it is possible to login with the holberton
exec { '/usr/bin/env sed -i "s/holberton/baz/" /etc/security/limits.conf': }
