#change the limit
exec { 'there is no limit':
command => 'sed -i "s/15/4069/" /etc/default/nginx | service nginx restart',
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
