#Change the OS configuration so that it is possible to login with the holberton
exec { ' login with the holberton user':
command => 'echo "" > /etc/security/limits.conf',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
