# a Puppet code find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet
exec { 'fix-phpp':
path     => 'usr/bin/:/bin/',
command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}
