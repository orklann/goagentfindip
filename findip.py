#!/usr/bin/env python

import os,time,sys,multiprocessing

# python3 support, httplib renamed to http.client in python3
if sys.version_info >= (3, 0):
    import http.client
else:
    import httplib

# good google's ip [elapse time, ip]
ip_queue=multiprocessing.Queue()

# how many ip parallelly check?, one ip one threadper.
thread_number=100

# store threads' id
thread_id=[]

def iplookup(ip,q):
    """ Check google's ip is suitable for goagent. """
    try:
        # python3 will use http.client.HTTPSConnection
        if sys.version_info >= (3, 0):
            conn=http.client.HTTPSConnection(ip,timeout=3)
        else:
            conn=httplib.HTTPSConnection(ip,timeout=3)

        conn.request("GET", "/")
        st=time.time()
        response=conn.getresponse()
        en=time.time()
        result=str(response.status)+' '+response.reason
        if '200 OK' in result:
            q.put([en-st, ip])
            print(ip+' is Good')
            conn.close()
    except:
        pass

def deal_ip():
    """ Get, arrange and format ipfor goagent. """
    # get all suitable ip in ip_queue
    google_ip=[]
    while not ip_queue.empty():
        try:
            google_ip.append(ip_queue.get())
        except:
            pass

    # sort [elapse_time, ip] with eclapse_time
    arranged_ip=sorted(google_ip,key=lambda l:l[0])

    # format ip for goagent
    format_ip=''
    for ip in arranged_ip:
        format_ip+=ip[1]+'|'

    # print arranged good ip, fast ahead
    if format_ip:
        print("\r\nOutput:\r\n")
        print(format_ip[:-1])
        print("\r\nPlease wait about 3 minutes to use goagent!!!\r\n"+\
            "I don't know why, but the scanning does affect it.\r\n"+\
            "You may have a cup of coffee, ^_^\r\n"+\
            "Enjoy!")
        write_file=open('out.txt', 'w')
        write_file.write(format_ip[:-1]+'\r\n')
        write_file.close()
    else:
        print("\r\nI am sorry, nothing found out")
        print("You may need to rerun it, and wait for it more time.")

if __name__ == '__main__':

    # get all files in ./ippool
    ippool_files=["./ippool/"+s for s in os.listdir("./ippool")]

    try:
        for ip_file in ippool_files:
            with open(ip_file, 'r') as infile:
                lines=infile.readlines()
                # close opened file
                infile.close()
                # split text to list with '\n' end
                lines=[x.rstrip('\n') for x in lines]
                # split ip to 2d array every read_number
                ip_all=[lines[i:i+thread_number] for i in range(0,len(lines),
                            thread_number)]
                
                for ips in ip_all:
                    format_str="scan from "
                    format_str+="{:>15}    to    {:>15} ++please be patient"
                    print(format_str.format(ips[0],ips[-1]))
                    for ip in ips:
                        p = multiprocessing.Process(target=iplookup,
                                                    args=(ip,ip_queue,))
                        thread_id.append(p)
                        thread_id[-1].daemon=True
                        thread_id[-1].start()
            
                    # wait for finish
                    time.sleep(4)
    
                    # killall remain thread
                    for x in thread_id:
                        if x.is_alive():
                            x.terminate()
        
                    # clean thread_id
                    thread_id=[]
                    
        # deal with ip
        deal_ip()
        # quit
        sys.exit(0)

    except KeyboardInterrupt:

        # deal with ip
        deal_ip()
        # quit   
        sys.exit(0)
