#exec { 'build database':
#    command => 'python database_init.py',
#    cwd     => '/vagrant/catalog',
#    environment => ['LC_ALL=en_US.UTF-8', 'LANG=en_US.UTF-8', 'LC_CTYPE=UTF-8'],
#    path    => '/usr/bin',
#    user    => 'vagrant',
#    notify  => Exec['start catalog'],
#}
#exec { 'start catalog':
#    command => 'python /vagrant/catalog/catalog.py',
#    cwd     => '/vagrant/catalog',
#    unless  => 'pgrep -lu vagrant | grep python',
#    path    => '/usr/bin',
#    user    => 'vagrant',
#    subscribe => Exec['build database'],
#    refreshonly => true,
#}

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
}

package { $pypi_packages:
    ensure => present,
    provider => 'pip',
    require => Package['python-pip'],
}

class { 'postgresql::server': }

postgresql::server::db { 'beercatalog':
    #user => 'vagrant',
    #password => postgresql_password('vagrant', 'vagrant'),
    #grant => all,
    user     => 'connoisseur',
    #password => 'michaeljackson',
    password => postgresql_password('connoisseur', 'michaeljackson'),
    require => Package['postgresql'],
}

postgresql::server::pg_hba_rule { 'allow localhost to access beercatalog database':
    description => 'open up postgresql for local access',
    type => 'host',
    database => 'beercatalog',
    user => 'connoisseur',
    address => 'localhost',
    auth_method => 'trust',
}

postgresql::server::pg_hba_rule { 'allow vagrant to access beercatalog database':
    description => 'open up postgresql for local access',
    type => 'host',
    database => 'beercatalog',
    user => 'vagrant',
    address => 'localhost',
    auth_method => 'trust',
}

#postgresql::server::role { 'connoisseur':
#    password_hash => postgresql('connoisseur', 'michaeljackson'),
#}

postgresql::server::role { 'vagrant': }

exec { 'load fixtures':
    command => 'python database_init.py',
    cwd => '/vagrant/catalog/',
    logoutput => 'true',
    path => ['/usr/bin/'],
    user => 'vagrant',
    #onlyif => 'psql --list | grep beercatalog',
    unless => '',
    subscribe => [Postgresql::Server::Db['beercatalog'], Postgresql::Server::Pg_hba_rule['allow localhost to access beercatalog database']],
}

exec { 'start web application':
    command => 'python catalog.py &',
    cwd => '/vagrant/catalog/',
    logoutput => 'true',
    path => ['/usr/bin/'],
    user => 'vagrant',
    require => Exec['load fixtures'],
}
