#!/usr/bin/env python

import os,time,httplib,sys,multiprocessing

# good google's ip [elapse time, ip]
ip_queue=multiprocessing.Queue()

# how many ip parallelly check?
thread_number=500

# store threads' id
thread_id=[]

def iplookup(ip,q):
    """ Check google's ip is suitable for goagent. """
    try:
        c=httplib.HTTPSConnection(ip,timeout=3)
        c.request("GET", "/")
        st=time.time()
        response=c.getresponse()
        en=time.time()
        result=str(response.status)+' '+response.reason
        if '200 OK' in result:
            q.put([en-st, ip])
            print ip, 'is Good'
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
        print "\r\nOutput:\r\n"
        print format_ip[:-1]
        print "\r\nPlease wait about 3 minutes to use goagent!!!\r\n"+\
            "I don't know why, but the scanning does affect it.\r\n"+\
            "You may have a cup of coffee, ^_^\r\n"+\
            "Enjoy!"
        file=open('out.txt', 'w')
        file.write(format_ip[:-1]+'\r\n')
        file.close()
    else:
        print "\r\nI am sorry, nothing found out"
        print "You may need to rerun it, and wait for it more time."

if __name__ == '__main__':

    # get all files in ./ippool
    ippool_files=["./ippool/"+s for s in os.listdir("./ippool")]

    try:
        for file in ippool_files:
            with open(file, 'r') as infile:
                lines=infile.readlines()
                lines=[x.rstrip('\n') for x in lines]
                # split ip to 2d array
                ip_all=[lines[i:i+thread_number] for i in xrange(0,len(lines),
                            thread_number)]
                
                for ips in ip_all:
                    format_str="scan from "
                    format_str+="{:>15}    to    {:>15} ++please be patient"
                    print format_str.format(ips[0],ips[-1])
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
        infile.close()

        sys.exit(0)

    except KeyboardInterrupt:

        # deal with ip
        deal_ip()   
        infile.close()

        sys.exit(0)
