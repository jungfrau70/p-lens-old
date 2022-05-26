cat <<EOF | tee /etc/hosts
127.0.0.1       localhost
127.0.1.1       ubuntu

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

172.18.0.80     kr1-zookeeper
172.18.0.81     kr1-kafka1
172.18.0.82     kr1-kafka2
172.18.0.83     kr1-kafka3
172.18.0.84     kr1-kafdrop

EOF