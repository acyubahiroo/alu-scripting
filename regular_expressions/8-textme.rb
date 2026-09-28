#!/usr/bin/env ruby
ARGV[0].scan(/\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/) do |from, to, flags|
  puts "#{from},#{to},#{flags}"
end
