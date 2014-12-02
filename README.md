
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

1. Scan all possible google's IPs.
2. Auto sort IP with connection speed, fast ahead.
3. Print output in your terminal and write to out.txt file.
4. Add random mechanism to scan.
5. Analyze webpage content and use SSL to improve IPs' quality.
6. Show scanning progress!
7. Fastly lookup.

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

#TEST:

Linux, RAM: 512MB, Single Core, IPs: 250, 50 Parallelly, Python3.4

Elapse time(seconds): 
1823, 1513, 1581, 1015, 1010, 833, 782, 844, 484, 961, 1330, 860, 1391, 1157, 515 , 1238, 848, 1703, 1969
```
       Linux, RAM: 512MB, Single Core, IPs: 250, 50 Parallelly, Python3.4
       
time(s) 
  2000 ++------+------+-------+------+-------+------+-------+------+------+A
       +       +      +       +      +       +      +       +      +       +
  1800 A+.................................................................++
       |       :      :       :      :       :      :       :      :   A   |
  1600 ++......A..........................................................++
       |   A   :      :       :      :       :      :       :      :       |
  1400 ++...........................................A.....................++
       |       :      :       :      :       A      :       :      :       |
  1200 ++.......................................................A.........++
       |       :      :       :      :       :      :   A   :      :       |
       |       :  A   :       :      :       :      :       :      :       |
  1000 ++.............A..................A................................++
       |       :      :   A   :  A   :       :   A  :       :      A       |
   800 ++.....................A...........................................++
       |       :      :       :      :       :      :       :      :       |
   600 ++.................................................................++
       +       +      +       +      A       +      +       A      +       +
   400 ++------+------+-------+------+-------+------+-------+------+------++
       0       2      4       6      8       10     12      14     16      18
                                     Count(n)

```

#FAQ
1. Many IPs good, but slow speed?

    First,

        Free Google App Engine, has it's own limits:

            1. Outgoing/Incoming Bandwidth：1GB/day、56MB/minute

            2. UrlFetch Data Sent/Received：22MB/minute

                Please see: https://cloud.google.com/appengine/docs/quotas
        
        Goagent canceled pagespeed due to Google withdrew pagespeed servers from China.
    
    Second,
    
        Too many IPs in proxy.ini, will slow down your average speed. I personally thank 
            250 is well.
    
    However you also can try to find faster IPs by modifying findip.py file:
    
        begin with 40 line:
    
            # python3 will use http.client.HTTPSConnection
            if sys.version_info >= (3, 0):
                conn=http.client.HTTPSConnection(ip,timeout=3)
            else:
                conn=httplib.HTTPSConnection(ip,timeout=3)
        
        to smaller timeout value, example here is: 2
    
            # python3 will use http.client.HTTPSConnection
            if sys.version_info >= (3, 0):
                conn=http.client.HTTPSConnection(ip,timeout=2)
            else:
                conn=httplib.HTTPSConnection(ip,timeout=2)
    
    
        and modify join time at line 151, example here is 4:
    
            p.join(6)
        to 
            p.join(4)
    
    
        This will filter slow IPs, but fewer IPs can be found, 
            and need wait for more time.
    
    Enjoy!

2. Windows hangs or freezes when run this program?

    I am sorry, neither do I have solutions, but you can modify 
        thread_number(at line 32) to a smaller value, for example, 50, 
        and try again.
