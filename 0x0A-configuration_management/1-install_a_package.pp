# Using Puppet, install puppet-lint

Package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
