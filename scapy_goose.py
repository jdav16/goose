from scapy.all import *


ethernet = Ether(src='00:00:00:00:00:01', dst='00:00:00:00:00:02')

vlan2=[2 for i in range(30)]

prio = Dot1Q(vlan=vlan2,id=2,prio=2,type=0x88b8)


class Goose(Packet):
   name = "Goose"
   fields_desc=[ByteField("APPID", 3), ShortField("len", 0), XByteField("reserved1", None), XByteField("reserved2", None),]


class GoosePdu(Packet):
   name = "GoosePdu"
   fields_desc= [
   ByteField("TimeAllowedToLive", 0),
   ByteField("stNum", 0),
   ByteField("sqNum", 0),
   ShortField("ConfRev", 0),
   ByteField("NumDatSetEntries", 0),]



goose=Goose()
goosePdu=GoosePdu()

sendp(ethernet/prio/goose/goosePdu)
