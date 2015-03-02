from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.ZenUtils.Utils import zenPath,prepId
from ZenPacks.community.Jenkins.Definition import *
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

__doc__ = """JenkinsBuildMap

JenkinsBuildMap detects Jenkins Builds

"""

class JenkinsBuildMap(PythonPlugin):
    """
    """
    compname = "os"
    constr = Construct(JenkinsBuildDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    deviceProperties = PythonPlugin.deviceProperties + (
                    'zJenkinsPort',
                    'zJenkinsURL',
                    )

    def collect(self, device, log):
        url = 'http://%s:%s%s' % (device.id, device.zJenkinsPort, device.zJenkinsURL)
        log.debug("checking Jenkins at %s" % url) 
        J = Jenkins(url)
        output = []
        for j in J.get_jobs_list():
            job = J.get_job(j)
            info = {}
            id = job.name.replace('-','_')
            info['id'] = prepId(id)
            info['buildid'] = job.name
            info['description'] = job.get_description()
            info['monitor'] = job.is_enabled()
            output.append(info)
        return output
 
    def process(self, device, results, log):
        log.debug("processing device: %s results: %s" % (device, results))
        rm = self.relMap()
        for r in results:
            om = self.objectMap(r)
            rm.append(om)
        return rm
    
