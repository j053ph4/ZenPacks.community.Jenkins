from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "Jenkins"
VERSION = Version(1, 0, 0)
ZPROPS = []

def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'UNKNOWN'

def getBuildStatus(ob): return ob.getMapValue('check_build_status', ob.buildStatusMap)

buildStatusMap = { 0: 'SUCCESS', 1: 'FAILURE', 2: 'ABORTED', 3: 'UNSTABLE', 4: 'NOT_BUILD', 5: 'STILL_UNSTABLE'}
zenossStatusMap = { 'SUCCESS' : 0, 'FAILURE' : 5, 'ABORTED' : 3, 'UNSTABLE' : 3, 'NOT_BUILD' : 3, 'UNKNOWN': 1}

def getStatus(ob):
    msg = ob.getBuildStatus()
    return ob.zenossStatusMap[msg]
    
    
JenkinsBuildDefinition = type('JenkinsBuildDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'JenkinsBuild',
        'componentData' : {
                          'singular': 'Jenkins Build',
                          'plural': 'Jenkins Builds',
                          'properties': {
                                        'buildid' : addProperty('Build ID'),
                                        'description' : addProperty('Description', optional=False),
                                        'getBuildStatus' : getReferredMethod('Build Status', 'getBuildStatus'),
                                        },
                          },
        
        'packZProperties' : [ 
                             ('zJenkinsPort', '8080', 'string'),
                             ('zJenkinsURL', '/jenkins', 'string'),
                             ('zJenkinsUser', '', 'string'),
                             ('zJenkinsPassword', '', 'password'),
                            ],
        'componentAttributes' : {'buildStatusMap': buildStatusMap, 'zenossStatusMap': zenossStatusMap},
        'componentMethods' : [getMapValue, getBuildStatus, getStatus]
        }
)
