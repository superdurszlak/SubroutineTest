from abaqusGui import getAFXApp
from config import VERSION

# Root function for the plugin
def init():
    # Abaqus 'Plugins' toolset
    toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
    # Attach 'ImpactTest' plugin to the toolset
    toolset.registerKernelMenuButton(
        buttonText='Subroutine Test',
        # Plugin's main module
        moduleName="plugin_runner",
        # Module's function to be invoked
        functionName="run()",
        author='Szymon Durak',
        description='Ballistic impact model designer',
        version=VERSION,
        helpUrl='https://github.com/superdurszlak/ImpactTest/blob/master/README.md'
    )


init()