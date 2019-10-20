# SubroutineTest

SubroutineTest is Abaqus 6.14 plugin intended for user-defined constitutive model assessment automation. As such, its planned purpose is to allow to pre-configure and autogenerate simple dynamic/explicit models for user-defined UHARD/VUHARD subroutines.

## Formalities

The plugin is part of my Master's Thesis "Evaluation of capabilities of rheological models for high strain rate loading conditions". ~As such, no third-party contributions to this project may be accepted until the day of my thesis' defence. However, feel free to fork and/or use the plugin, as long as you find it worth using.~ Since the thesis defence took place on 19th September 2019, I believe contributions made after that date are safe and welcome. 

## Prerequisities

* Python 2.7 - required to pre-compile plugin sources to *\*.pyc* files
* Abaqus FEA 6.14 - other versions may, or may not work with the plugin due to possible API incompatibility
* Intel Parallel Studio with Intel Fortran Compiler (ifort)
* Microsoft Visual Studio

## Setup

To install SubroutineTest plugin, copy entire project tree to *<Abaqus installation directory>/SIMULIA/6.14-3/code/python2.7/lib/abaqus_plugins*. 
Then, enter *SubroutineTest* folder and run *setup.py* script to compile project sources. To be able to use the plugin, you need to restart Abaqus CAE if one is running.

In order to run Abaqus jobs with user subroutines, you need to install Intel Fortran Compiler (ifort) first, which is bundled with Intel Parallel Studio, which in turn you have to integrate with MS Visual Studio. Then you need to configure Abaqus Command and Abaqus CAE to start with Intel Parallel Studio running in background with proper arguments. To accomplish this, refer to manuals and documentation provided by 3DS and Intel. You may also find various tips shared at ResearchGate useful. Installation process may differ depending on exact versions of software.

## Usage

After successful setup *SubroutineTest* plugin should be accessible from Plug-ins tab as shown below:
![plugin_run.png](./resources/plugin_run.PNG)
