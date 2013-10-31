#!/usr/bin/env python

import sys
from ConfigParser import SafeConfigParser

class SnmpManager:
    def __init__(self):
        self.systems = {}
        
    def add_system(self, id, descr, addr, port, comm_ro):
        self.systems[id] = {'description'   : descr,
                             'address'      : addr,
                             'port'         : int(port),
                             'communityro'  : comm_ro,
                             'checks'       : {}
                             }
                             
    def add_check(self , id, oid, descr, system):
        oid_tuple = tuple([int(i) for i in oid.split('.')])
        self.system[system]['checks'][id] = {'description': descr,
                                              'oid'       : oid_tuple,
                                          }
                                         
    def main(conf_file="snmpconfig"):
        if not conf_file:
            sys.exit(-1)
        config = SafeConfigParser()
        config.read(conf_file)
        snmp_manager = SnmpManager()
        for system in [s for s in config.section() if s.startswitch('system')]:
            snmp_manager.add_system(system,
                                    config.get(system, 'desctription'),
                                    config.get(system,  'address'),
                                    config.get(system,  'port'),
                                    config.get(system,  'communityro'))
        for check in [c for c in config.sections() if c.startswith('check')]:
            snmp_manager.add_check(check,
                                    config.get(check, 'oid'),
                                    config.get(check, 'description'),
                                    config.get(check, 'system'))
