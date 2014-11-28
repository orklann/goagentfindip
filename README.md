
#Introduction

A tiny tool to find google ip for goagent

#License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Features:

1. Scan all possible google's IP.
2. Auto sort IP with connectoin speed, fast ahead.
3. Print output in your terminal and write to out.txt file.
4. Add random mechanism to scan.
5. Ping test to improve IPs' quality.

#How to run?
    Linux and MAC OS:
        python findip.py
    Windows:
        after install python, double click findip.py.
    
(You may need Ctrl+C to stop when you feel IPs enough.)

#NOTICE:

1. If you don't want to scan all IPs, please delete some unwanted files in ippool folder, it will scan remain IPs. 
2. You may need modify "thread_number" value, depending on your hardware, to control the ip number parallelly check, default: 100.
3. You may need to modify "ip_max_need" value to get numbers of IPs as you want.
4. If you can get IPs, you can ignore errors when you PRESS Ctrl+C
5. Enjoy!
    
