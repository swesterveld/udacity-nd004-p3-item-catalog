exec { 'update repository':
    command => 'sudo apt-get update',
    path => ['/usr/bin/'],
    logoutput => 'true',
    user => 'vagrant',
}

$deb_packages = [
    'postgresql',
    'python-flask',
    'python-pip',
    'python-psycopg2',
    'python-sqlalchemy',
]

$pypi_packages = [
    'oauth2client',
    'requests',
]

package { $deb_packages:
    ensure => present,
    require => Exec['update repository'],
}

package { $pypi_packages:
    ensure => present,
    provider => 'pip',
    require => Package['python-pip'],
}

class { 'postgresql::server': }

postgresql::server::db { 'beercatalog':
    user     => 'connoisseur',
    password => postgresql_password('connoisseur', 'michaeljackson'),
    before => Exec['load fixtures'],
}

postgresql::server::pg_hba_rule { 'allow localhost to access beercatalog database':
    description => 'open up postgresql for local access',
    type => 'host',
    database => 'beercatalog',
    user => 'connoisseur',
    address => 'localhost',
    auth_method => 'trust',
    before => Exec['load fixtures'],
}

postgresql::server::pg_hba_rule { 'allow vagrant to access beercatalog database':
    description => 'open up postgresql for local access',
    type => 'host',
    database => 'beercatalog',
    user => 'vagrant',
    address => 'localhost',
    auth_method => 'trust',
    before => Exec['load fixtures'],
}

postgresql::server::role { 'vagrant': }

exec { 'load fixtures':
    command => 'python database_init.py',
    cwd => '/vagrant/catalog/',
    logoutput => 'true',
    path => ['/usr/local/bin', '/usr/bin/', '/bin/'],
    user => 'vagrant',
    onlyif => 'psql --list | grep beercatalog',
}

exec { 'start web application':
    command => 'python /vagrant/catalog/catalog.py &',
    cwd => '/vagrant/catalog/',
    logoutput => 'true',
    path => ['/usr/bin/', '/bin/'],
    unless  => 'pgrep -lu vagrant | grep python',
    user => 'vagrant',
#    refreshonly => true,
    require => Exec['load fixtures'],
}
