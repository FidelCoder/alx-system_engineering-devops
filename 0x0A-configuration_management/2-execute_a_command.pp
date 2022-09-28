#executes a pkill command on killmenow
exec {'pkill':
command  => 'pkill killmenow',
provider => shell,
}
