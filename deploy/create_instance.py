import time
import boto
from boto.ec2.regioninfo import RegionInfo
import json

def get_real_instance_info(inst):
    all_res = conn.get_all_reservations()
    for res in all_res:
        if res.id == inst.id:
            return res

def create(size):
    print "Creating instance of",size,"GB"
    vol_req = conn.create_volume(
        size, region, volume_type=volumn_type)
    inst=conn.run_instances(
        image_name,
        key_name=key_pair,
        instance_type=instance_type,
        security_groups=sec_group,
        placement=region)

    print "Created a", size ,"GB instance"
    return vol_req

def print_instances(res):
    for ins in res:
        print "---------------------"
        print "IP: ", ins.instances[0].private_ip_address
        print "Placement: ", ins.instances[0].placement
        print "ID: ", ins.instances[0].id
        print "Key: ", ins.instances[0].key_name



config=json.load(open("config.json"))
access_key=config["access_key"]
secret_key=config["secret_key"]
instance_type=config["instance_type"]
instances_config=config["instances"]
region=config["region"]
sec_group=config["sec_group"]
key_pair=config["key_pair"]
image_name=config["image"]
volumn_type=config["volumn_type"]
output_header=config["output_header"]
conn = boto.connect_ec2(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        is_secure=True,
        region=RegionInfo(name=region, endpoint="nova.rc.nectar.org.au"),
        port=8773,
        path='/services/Cloud',
        validate_certs=False)

f=open("hosts","w+")
f.write(output_header+"\n\n")

vols=dict()
types=dict()

for sz in instances_config:
    vol=create(sz["size"])
    if sz["type"] not in vols:
        vols[sz["type"]]=[vol]
    else:
        vols[sz["type"]].append(vol)

print "Create Done, waiting for the instances..."
time.sleep(65)
print "Getting instance info..."
all_inst=conn.get_all_reservations()
print_instances(all_inst)
count=0
for ty in vols:
    types[ty]=[]
    for vol in vols[ty]:
        print "Attach volume of",ty
        if conn.attach_volume(vol.id, all_inst[count].instances[0].id, "/dev/vdb"):
            print("Volume attached OK!")
        else:
            print("Volume attached Failed!")
        types[ty].append(all_inst[count].instances[0].private_ip_address)
        count+=1

for ty in types:
    f.write("[%s]\n" % ty)
    for ip in types[ty]:
        f.write(ip+"\n")
    f.write("\n")
f.close()


