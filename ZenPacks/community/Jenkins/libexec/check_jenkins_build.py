#!/usr/bin/env python
from ZenPacks.community.ConstructionKit.libexec.CustomCheckCommand import *
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

class CheckJenkinsBuild(CustomCheckCommand):
    """
    """
    def __init__(self):
        CustomCheckCommand.__init__(self)
        self.statusMap = {'SUCCESS': {'val': 0, 'exit': 0 , 'msg': 'OK'}, 
                          'FAILURE': {'val': 1, 'exit': 2 , 'msg': 'CRITICAL'}, 
                          'ABORTED': {'val': 2, 'exit': 1 , 'msg': 'WARNING'}, 
                          'UNSTABLE': {'val': 3, 'exit': 1 , 'msg': 'WARNING'}, 
                          'NOT_BUILD': {'val': 4, 'exit': 1 , 'msg': 'WARNING'},
                          'UNKNOWN': {'val': 1, 'exit': 1 , 'msg': 'WARNING'}, 
                          }

    def buildOptions(self):
        """
        """
        ZenScriptBase.buildOptions(self)
        self.parser.add_option('--server', dest='server',
            help='Jenkins Server')
        self.parser.add_option('--port', dest='port',
            help='Jenkins Port')
        self.parser.add_option('--url', dest='url',
            help='Jenkins URL')
        self.parser.add_option('--user', dest='user',
            help='Jenkins User', default=None)
        self.parser.add_option('--password', dest='password',
            help='Jenkins Password', default=None)
        self.parser.add_option('--build', dest='build',
            help='Jenkins Build ID', default=None)

    def initialize(self):
        """
        """
        self.output = {'status': 'UNKNOWN', 'number': 0, 'duration': 0}
        serverurl = 'http://%s:%s%s' % (self.options.server, self.options.port, self.options.url)
        if self.options.user == None or self.options.password == None:
            self.session = Jenkins(serverurl)
        else:
            self.session = Jenkins(serverurl, self.options.user, self.options.password)
            
        job = self.session.get_job(self.options.build)
        build = job.get_last_build()
        self.output['status'] = build.get_status()
        if self.output['status'] is None: self.output['status'] = 'UNKONWN'
        self.output['number'] = build.get_number()
        self.output['duration'] = build.get_duration().total_seconds()#/1000

    def evalStatus(self):
        """
        """
        msg = "%s: %s status for build number: %s|status=%s;  duration=%ss"
        entry = self.statusMap[self.output['status']]
        self.status = entry['exit']
        self.message = msg % (entry['msg'], self.output['status'], self.output['number'], entry['val'], self.output['duration'])
 
if __name__ == "__main__":
    u = CheckJenkinsBuild()
    u.run()

