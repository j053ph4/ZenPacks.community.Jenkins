from ZenPacks.community.ConstructionKit.ClassHelper import *

def JenkinsBuildgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class JenkinsBuildInfo(ClassHelper.JenkinsBuildInfo):
    ''''''


