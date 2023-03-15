




#systemctl restart docker;
# echo  'bash /home/appbox/.sh'  >>  /etc/rc.d/rc.local
#docker restart $(docker ps -a -q);


cd /home/appbox;
export PATH=$PATH:/usr/local/python3/bin;

gunicorn -w 4 -b 127.0.0.1:8003 --access-logfile access8003.log --error-logfile error8003.log appbox:app -D;




/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf;


