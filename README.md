# Notification scripts for [Zabbix](http://www.zabbix.com/)

## Description
Notify users about errors by Zabbix via various channels.

## Platforms
### [Hipchat](https://www.hipchat.com/)
- Requires hipchat rubygem
- Provide proper token.
- Usage: hipchat.rb channel/user subject message

### [Slack](https://slack.com/)
- Provide proper company url and token in the connection.
- Usage: slack.py @user/#channel subject message

### [Pushover](https://pushover.net/)
- Provide proper token.
- Usage: push.py usertoken subject message

### [Alerts-activity-stream](https://github.com/szelcsanyi/alerts-activity-stream)
- Provide proper server url.
- Usage: alert-activity-stream.py group subject message

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

* Freely distributable and licensed under the [MIT license](http://szelcsanyi.mit-license.org/2014/license.html).
* Copyright (c) 2014 Gabor Szelcsanyi

