#!/usr/bin/env ruby

require 'rubygems'
require 'hipchat'

to = ARGV[0]
subject = ARGV[1]
message = ARGV[2]

client = HipChat::Client.new('yourtoken')
if subject[/PROBLEM/]
	client[to].send('Alert', message, :color => 'red', :message_format => 'text', :notify => true)
else
	client[to].send('Alert', message, :color => 'green', :message_format => 'text', :notify => true)
end
