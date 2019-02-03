from abaqusGui import getAFXApp

from config import VERSION


# Root function for the plugin
def init():
    # Abaqus 'Plugins' toolset
    toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
    # Attach 'SubroutineTest' plugin to the toolset
    toolset.registerKernelMenuButton(
        buttonText='Subroutine Test',
        # Plugin's main module
        moduleName='plugin_runner',
        # Module's function to be invoked
        functionName='run()',
        author='Szymon Durak',
        description='User-defined constitutive models testing tool',
        version=VERSION,
        helpUrl='https://github.com/superdurszlak/SubroutineTest/blob/master/README.md'
    )


init()
