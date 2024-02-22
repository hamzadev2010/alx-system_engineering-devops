#testing how well our web server setup featuring Nginx is doing under
#pressure and it turns out it’s not doing well: we are getting
#a huge amount of failed requests.
exec { 'my limit 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}
exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart'
}
