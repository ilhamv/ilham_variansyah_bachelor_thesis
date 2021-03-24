from PyQt4.QtGui import QMainWindow, QApplication, QWidget, QGraphicsScene, QColor, QBrush
from PyQt4.QtCore import QTimer, Qt
from LFIPRSimulator import Ui_LFIPRSimulator
from BeginningBurnup import Ui_Awal
from TrackedNuclide import Ui_TrackedNuclide
import math
from Functions import DependentKineticProperty, Nuclide
import sys

#############################global variable###################################
#text output and output array for graph
output_directory="C:\\Users\\Ilham\\Desktop\\Desktop_hide\\LFIPR Reactor Dynamics Simulator\\output.txt" #ubah direktori output
out=[] #text output
tArray=[] #time array
rhoArray=[] #reactivity array
TfArray=[] #fuel temperature array
TcArray=[] #coolant temperature array
PArray=[] #power array
critArray=[] #critical reactivity array
pcritArray=[] #prompt supercritical reactivity array
XeArray=[] #xenon-135 concentration array
SmArray=[] #samarium-149 concentration array
IArray=[] #iodine-135 concentration array
PmArray=[] #promethium-149 concentration array


#tracked nuclide and its properties
I=Nuclide()
I.FissionYield=6.29E-02 #I-135 fission yield
I.Lambda=2.87E-05 #I-135 decay constant [/s]
I.Siga=5.50E-04*10**-24,1.36E-02*10**-24 #I-135 absorption micros [cm2]

Xe=Nuclide()
Xe.FissionYield=2.41E-03 #Xe-135 fission yield
Xe.Lambda=2.09E-05 #Xe-135 decay constant [/s]
Xe.Siga=8.27E+00*10**-24,2.12E+06*10**-24 #Xe-135 absorption micros [cm2]

Pm=Nuclide()
Pm.FissionYield=1.07E-02 #Pm-149 fission yield
Pm.Lambda=3.56E-06 #Pm-149 decay constant [/s]
Pm.Siga=4.42E+01*10**-24,9.51E+02*10**-24 #Pm-149 micros [cm2]

Sm=Nuclide()
Sm.FissionYield=1.11E-10 #Sm-149 fission yield
Sm.Lambda=0 #Sm-149 decay constant [/s]
Sm.Siga=4.12E+01*10**-24,5.38E+04*10**-24 #Sm-149 absorption micros [cm2]


#initial time dimension
t=0.0 #initial time [s]
dt=10**-2 #initial time step [s]


#reactor dimension
N=340 #fuel cell number
D=0.0135 #average diameter of coolant canal [m]
L=0.6 #coolant canal length [m]
V=0.20441401 #core volume [m3]
Vf=V*0.846235002 #fuel volume [m3]
Vc=V*0.132583085 #coolant volume [m3]


#reactor parameters global declaration
fluks=[0,0] #fast and thermal flux [/cm2s]
c=[0,0,0,0,0,0] #6 delayed neutron precursor groups concentration [/cm3]
I.value=0 #I-135 concentration [/cm3]
Xe.value=0 #Xe-135 concentration [/cm3]
Pm.value=0 #Pm-149 concentration [/cm3]
Sm.value=0 #Sm-149 concentration [/cm3]
BU=0 #burnup level index

v=0 #void fraction
z1=0 #central control rod position [cm]
z2=0 #periferal control rod position [cm]

mdotf=0 #fuel flow rate [kg/s]
mdotc=0 #coolant flow rate [kg/s]
Tf=0 #fuel temperature [C]
Tc=0 #coolant temperature [C]
Tfin=0 #fuel inlet temperature [C]
Tcin=0 #coolant inlet temperature [C]


#reactor kinetic properties global declaration
rho=DependentKineticProperty() #reactivity
lp=DependentKineticProperty() #mean neutron lifetime [s]
beta=0 #delayed neutron fraction
lambdai=[0,0,0,0,0,0] #delayed neutron precursor group decay constant [/s]
betai=[0,0,0,0,0,0] #delayed neutron precursor group fraction
siga1=DependentKineticProperty() #fast group absorbtion macros [/cm]
sigf1=DependentKineticProperty() #fast fission macros [/cm]
sigf2=DependentKineticProperty() #thermal fission macros [/cm]
sigs12=DependentKineticProperty() #fast group down scattering macros [/cm]
nu=[0,0] #nusselt number
D1=DependentKineticProperty() #fast group diffusion coefficient [cm]

B=0 #buckling geometry [/cm]

P=0 #W


#thermal properties global declaration
U=1000 #assumed overal heat transfer coefficient [W/m2s]
def densf(Tf):return-0.0039871632*Tf**2 + 0.0477808554*Tf + 1040.7551550382 #fuel density [kg/m3]
cpf=0.74 *4.1868*1000 #fuel heat capacity [J/kgK]
def densc(Tc):return-0.0040893981*Tc**2 + 0.0490060056*Tc + 995.3899026033 #coolant density [kg/m3]
def cpc(Tc):return (0.0000081240*Tc**2 - 0.0008163912*Tc + 4.2249266749)*1000 #coolant heat capacity [J/kgK]


#kinetic property feedback and control constants, MOL's and EOL's aren't included yet
rho.a1Tf=-0.0000721,0,0
rho.a2Tf=-0.000001394,0,0
rho.a1v=-0.002749,0,0
rho.a2v=-0.00002382,0,0
rho.a1Xe=-2.566E-17,0,0
rho.a1Sm=-6.5E-19,0,0
rho.a51z10=-3E-13,0,0
rho.a50z10=1.18E-09,0,0
rho.a51z11=-2.044E-11,0,0
rho.a50z11=1.3814E-09,0,0
rho.a51z12=-9.78E-12,0,0
rho.a50z12=1.1682E-09,0,0
rho.a51z13=6.19E-12,0,0
rho.a50z13=6.891E-10,0,0
rho.a51z14=-5.02E-12,0,0
rho.a50z14=1.1375E-09,0,0
rho.a51z15=-2.96E-12,0,0
rho.a50z15=1.0345E-09,0,0
rho.a41z10=5E-11,0,0
rho.a40z10=-1.743E-07,0,0
rho.a41z11=3.6E-09,0,0
rho.a40z11=-2.098E-07,0,0
rho.a41z12=1.78E-09,0,0
rho.a40z12=-1.734E-07,0,0
rho.a41z13=-1.48E-09,0,0
rho.a40z13=-7.56E-08,0,0
rho.a41z14=3E-11,0,0
rho.a40z14=-0.000000136,0,0
rho.a41z15=2.9E-10,0,0
rho.a40z15=-0.000000149,0,0
rho.a31z10=-3.6E-09,0,0
rho.a30z10=0.000007135,0,0
rho.a31z11=-2.138E-07,0,0
rho.a30z11=0.000009237,0,0
rho.a31z12=-9.88E-08,0,0
rho.a30z12=0.000006937,0,0
rho.a31z13=1.265E-07,0,0
rho.a30z13=1.78E-07,0,0
rho.a31z14=5.65E-08,0,0
rho.a30z14=0.000002978,0,0
rho.a31z15=-1.7E-09,0,0
rho.a30z15=0.000005888,0,0
rho.a21z10=0.000000093,0,0
rho.a20z10=-0.00002109,0,0
rho.a21z11=0.000004609,0,0
rho.a20z11=-0.00006625,0,0
rho.a21z12=0.000001443,0,0
rho.a20z12=-0.00000293,0,0
rho.a21z13=-4.3213E-06,0,0
rho.a20z13=0.000169999,0,0
rho.a21z14=-2.9247E-06,0,0
rho.a20z14=0.000114135,0,0
rho.a21z15=-0.000000344,0,0
rho.a20z15=-0.0000149,0,0
rho.a11z10=-5.2E-07,0,0
rho.a10z10=-0.0001419,0,0
rho.a11z11=-0.00002468,0,0
rho.a10z11=0.0000997,0,0
rho.a11z12=-0.00000592,0,0
rho.a10z12=-0.0002755,0,0
rho.a11z13=0.00002767,0,0
rho.a10z13=-0.0012832,0,0
rho.a11z14=0.00001985,0,0
rho.a10z14=-0.0009704,0,0
rho.a11z15=0.00000261,0,0
rho.a10z15=-0.0001084,0,0
rho.a51z20=-3.2E-12,0,0
rho.a50z20=1.114E-09,0,0
rho.a51z21=-1.463E-11,0,0
rho.a50z21=1.2283E-09,0,0
rho.a51z22=-3.75E-12,0,0
rho.a50z22=1.0107E-09,0,0
rho.a51z23=-3.72E-12,0,0
rho.a50z23=1.0098E-09,0,0
rho.a51z24=-1.516E-11,0,0
rho.a50z24=1.4674E-09,0,0
rho.a51z25=-5.26E-12,0,0
rho.a50z25=9.724E-10,0,0
rho.a41z20=6.4E-10,0,0
rho.a40z20=-1.796E-07,0,0
rho.a41z21=0.000000003,0,0
rho.a40z21=-2.032E-07,0,0
rho.a41z22=8.9E-10,0,0
rho.a40z22=-0.000000161,0,0
rho.a41z23=5E-11,0,0
rho.a40z23=-1.358E-07,0,0
rho.a41z24=1.72E-09,0,0
rho.a40z24=-2.026E-07,0,0
rho.a41z25=6.6E-10,0,0
rho.a40z25=-1.496E-07,0,0
rho.a31z20=-4.37E-08,0,0
rho.a30z20=0.000008695,0,0
rho.a31z21=-2.013E-07,0,0
rho.a30z21=0.000010271,0,0
rho.a31z22=-5.27E-08,0,0
rho.a30z22=0.000007299,0,0
rho.a31z23=4.53E-08,0,0
rho.a30z23=0.000004359,0,0
rho.a31z24=-4.11E-08,0,0
rho.a30z24=0.000007815,0,0
rho.a31z25=-2.27E-08,0,0
rho.a30z25=0.000006895,0,0
rho.a21z20=0.000001094,0,0
rho.a20z20=-0.00009404,0,0
rho.a21z21=0.000004795,0,0
rho.a20z21=-0.00013105,0,0
rho.a21z22=0.000000472,0,0
rho.a20z22=-0.00004459,0,0
rho.a21z23=-0.000002686,0,0
rho.a20z23=0.00005015,0,0
rho.a21z24=-0.000000738,0,0
rho.a20z24=-0.00002777,0,0
rho.a21z25=9.5E-08,0,0
rho.a20z25=-0.00006942,0,0
rho.a11z20=-0.00000718,0,0
rho.a10z20=0.0002311,0,0
rho.a11z21=-0.00003063,0,0
rho.a10z21=0.0004656,0,0
rho.a11z22=0,0,0
rho.a10z22=-0.000147,0,0
rho.a11z23=0.000022907,0,0
rho.a10z23=-0.00083421,0,0
rho.a11z24=0.000010233,0,0
rho.a10z24=-0.00032725,0,0
rho.a11z25=7.3E-07,0,0
rho.a10z25=0.0001479,0,0

siga1.a1Tf=0.000001062,0,0
siga1.a2Tf=-1.296E-08,0,0
siga1.a1v=-3.09614E-05,0,0

sigs12.a1Tf=3.949E-07,0,0
sigs12.a2Tf=-9.927E-08,0,0
sigs12.a1v=-0.000264384,0,0

D1.a1Tf=-0.0002206,0,0
D1.a2Tf=0.000005909,0,0
D1.a1v=0.01316,0,0
D1.a2v=0.00007695,0,0

sigf1.a1Tf=3.206E-08,0,0
sigf1.a2Tf=-3.007E-09,0,0
sigf1.a1v=-7.9449E-06,0,0

sigf2.a1Tf=-0.00004613,0,0
sigf2.a2Tf=-5.664E-08,0,0
sigf2.a1v=-0.000345653,0,0

lp.a1Tf=2.729E-09,0,0
lp.a2Tf=3.213E-10,0,0
lp.a1v=7.302E-07,0,0
lp.a2v=3.867E-09,0,0
lp.a51z10=-4E-16,0,0
lp.a50z10=2.78E-13,0,0
lp.a51z11=-8.89E-15,0,0
lp.a50z11=3.629E-13,0,0
lp.a51z12=-2.67E-15,0,0
lp.a50z12=2.385E-13,0,0
lp.a51z13=2.77E-15,0,0
lp.a50z13=7.53E-14,0,0
lp.a51z14=-3.82E-15,0,0
lp.a50z14=3.389E-13,0,0
lp.a51z15=-6.5E-16,0,0
lp.a50z15=1.804E-13,0,0
lp.a41z10=7.1E-14,0,0
lp.a40z10=-4.4E-11,0,0
lp.a41z11=1.529E-12,0,0
lp.a40z11=-5.858E-11,0,0
lp.a41z12=4.74E-13,0,0
lp.a40z12=-3.748E-11,0,0
lp.a41z13=-6.6E-13,0,0
lp.a40z13=-3.46E-12,0,0
lp.a41z14=3.1E-13,0,0
lp.a40z14=-4.226E-11,0,0
lp.a41z15=1.06E-13,0,0
lp.a40z15=-3.206E-11,0,0
lp.a31z10=-4.4E-12,0,0
lp.a30z10=1.985E-09,0,0
lp.a31z11=-8.87E-11,0,0
lp.a30z11=2.828E-09,0,0
lp.a31z12=-2.215E-11,0,0
lp.a30z12=1.497E-09,0,0
lp.a31z13=5.595E-11,0,0
lp.a30z13=-8.46E-10,0,0
lp.a31z14=5.3E-12,0,0
lp.a30z14=1.18E-09,0,0
lp.a31z15=-6.6E-12,0,0
lp.a30z15=1.775E-09,0,0
lp.a21z10=9.8E-11,0,0
lp.a20z10=-1.432E-08,0,0
lp.a21z11=1.8598E-09,0,0
lp.a20z11=-3.1938E-08,0,0
lp.a21z12=6.9E-11,0,0
lp.a20z12=3.878E-09,0,0
lp.a21z13=-1.8828E-09,0,0
lp.a20z13=6.2432E-08,0,0
lp.a21z14=-7.68E-10,0,0
lp.a20z14=1.784E-08,0,0
lp.a21z15=1.82E-10,0,0
lp.a20z15=-2.966E-08,0,0
lp.a11z10=-5.5E-10,0,0
lp.a10z10=-1.36E-08,0,0
lp.a11z11=-1.015E-08,0,0
lp.a10z11=8.24E-08,0,0
lp.a11z12=9.3E-10,0,0
lp.a10z12=-1.392E-07,0,0
lp.a11z13=1.2662E-08,0,0
lp.a10z13=-4.9116E-07,0,0
lp.a11z14=6.185E-09,0,0
lp.a10z14=-2.3208E-07,0,0
lp.a11z15=-1.046E-09,0,0
lp.a10z15=1.2947E-07,0,0
lp.a51z20=-1.47E-15,0,0
lp.a50z20=3.147E-13,0,0
lp.a51z21=-8.53E-15,0,0
lp.a50z21=3.853E-13,0,0
lp.a51z22=-1.9E-15,0,0
lp.a50z22=2.527E-13,0,0
lp.a51z23=-1E-16,0,0
lp.a50z23=1.987E-13,0,0
lp.a51z24=-5.98E-15,0,0
lp.a50z24=4.339E-13,0,0
lp.a51z25=-7.2E-16,0,0
lp.a50z25=1.709E-13,0,0
lp.a41z20=2.67E-13,0,0
lp.a40z20=-5.227E-11,0,0
lp.a41z21=1.56E-12,0,0
lp.a40z21=-6.52E-11,0,0
lp.a41z22=3.96E-13,0,0
lp.a40z22=-4.192E-11,0,0
lp.a41z23=-1.9E-13,0,0
lp.a40z23=-2.434E-11,0,0
lp.a41z24=6.75E-13,0,0
lp.a40z24=-5.894E-11,0,0
lp.a41z25=9.3E-14,0,0
lp.a40z25=-2.984E-11,0,0
lp.a31z20=-1.63E-11,0,0
lp.a30z20=2.565E-09,0,0
lp.a31z21=-9.52E-11,0,0
lp.a30z21=3.354E-09,0,0
lp.a31z22=-2.01E-11,0,0
lp.a30z22=1.852E-09,0,0
lp.a31z23=2.88E-11,0,0
lp.a30z23=3.85E-10,0,0
lp.a31z24=-1.66E-11,0,0
lp.a30z24=2.201E-09,0,0
lp.a31z25=-3.9E-12,0,0
lp.a30z25=1.566E-09,0,0
lp.a21z20=3.73E-10,0,0
lp.a20z20=-2.861E-08,0,0
lp.a21z21=2.0814E-09,0,0
lp.a20z21=-4.5694E-08,0,0
lp.a21z22=4.82E-11,0,0
lp.a20z22=-5.03E-09,0,0
lp.a21z23=-1.2666E-09,0,0
lp.a20z23=3.4414E-08,0,0
lp.a21z24=-2.46E-10,0,0
lp.a20z24=-6.41E-09,0,0
lp.a21z25=7.2E-11,0,0
lp.a20z25=-2.231E-08,0,0
lp.a11z20=-2.297E-09,0,0
lp.a10z20=7.908E-08,0,0
lp.a11z21=-1.2502E-08,0,0
lp.a10z21=1.8113E-07,0,0
lp.a11z22=1.274E-09,0,0
lp.a10z22=-9.439E-08,0,0
lp.a11z23=0.00000001,0,0
lp.a10z23=-3.5617E-07,0,0
lp.a11z24=3.475E-09,3.475E-090,0
lp.a10z24=-9.517E-08,0,0
lp.a11z25=-4.63E-10,-4.63E-100,0
lp.a10z25=1.0173E-07,0,0

#others
ci=1 #for precursor calculation
RKok=[True] #for RKF45 method


#initials for each burnup level
def initial():
    global BU,fluks,c,I,Xe,Pm,Sm,v,z1,z2,Tf,Tc,mdotf,mdotc,Tfin,Tcin,rho,lp,beta,lambdai,betai,siga1,sigf1,sigf2,sigs12,nu,D1,B,P,V
    init_fluks=[0.0,0.0],[20253578.80156669,1022996513387.9971],[1177317.569,2900425581]
    init_c=[0.0,0.0,0.0,0.0,0.0,0.0],[1336239507.0632775, 3626284387.8480835, 887731224.6573828, 660734471.8876841, 51333102.5697835, 7073925.7259922],[3337086.611,9079066.791,2215317.337,1646377.728,127995.7892,17694.09935]
    init_I=0.0,7.04553E+13,1.77992E+11
    init_Xe=0.0,9.10207E+13,2.53722E+11
    init_Pm=0.0,9.64078E+13,2.43556E+11
    init_Sm=0.0,6.24145E+15,5.5614E+15
    init_v=0.0,0.0,0.0
    init_z1=30,40,60
    init_z2=20.83,32.36,53.3
    init_Tf=66.96932385,72.1203542,66.98220141
    init_Tc=56.11657737,56.59708293,56.1177786
    init_mdotf=5.0,5.0,5.0
    init_mdotc=10.0,10.0,10.0
    init_Tfin=70.0,70.0,70.0
    init_Tcin=55.0,55.0,55.0

    init_rho=0.0,0.0,0.0#-6.20004E-06,-4E-07
    init_lp=6.76473E-05,8.25562E-05,9.69618E-05
    init_beta=0.00652813,0.00643633,0.00633841
    init_lambdai=[0.012442,0.0305454,0.111516,0.301682,1.13868,3.02199],[0.0124451,0.0305425,0.111637,0.301893,1.13937,3.02117],[0.0124481,0.0305384,0.111746,0.302083,1.13974,3.01922]
    init_betai=[0.000214698,0.00142628,0.00127854,0.00257798,0.000755217,0.000275412],[0.000211605,0.00140932,0.00126105,0.00253818,0.000744226,0.000271944],[0.000208378,0.00139153,0.00124236,0.00249593,0.000732111,0.000268101]
    init_siga1=0.00329824,0.0032499,0.00318951
    init_sigf1=0.000796059,0.000711341,0.000626731
    init_sigf2=0.0351263,0.0314197,0.0279961
    init_sigs12=0.0329776,0.0330006,0.0330341
    init_nu=[2.473535253,2.436334029],[2.482100708,2.445010614],[2.491898438,2.453945371]
    init_D1=1.69204,1.69209,1.69216

    init_B=10,10,10 ##

    init_P=(init_sigf1[0]*init_fluks[0][0]+init_sigf2[0]*init_fluks[0][1])*1000**2*190.0*1.6021*10.0**-13.0*V,(init_sigf1[1]*init_fluks[1][0]+init_sigf2[1]*init_fluks[1][1])*1000**2*190.0*1.6021*10.0**-13.0*V,(init_sigf1[2]*init_fluks[2][0]+init_sigf2[2]*init_fluks[2][1])*1000**2*190.0*1.6021*10.0**-13.0*V

    fluks=init_fluks[BU]
    c=init_c[BU]
    I.value=init_I[BU]
    Xe.value=init_Xe[BU]
    Pm.value=init_Pm[BU]
    Sm.value=init_Sm[BU]
    v=init_v[BU]
    z1=init_z1[BU]
    z2=init_z2[BU]
    Tf=init_Tf[BU]
    Tc=init_Tc[BU]
    mdotf=init_mdotf[BU]
    mdotc=init_mdotc[BU]
    Tfin=init_Tfin[BU]
    Tcin=init_Tcin[BU]
    sigf1.value=init_sigf1[BU]
    sigf2.value=init_sigf2[BU]
    B=init_B[BU]    
    P=init_P[BU]
    rho.value=init_rho[BU]
    lp.value=init_lp[BU]
    siga1.value=init_siga1[BU]
    sigs12.value=init_sigs12[BU]
    beta=init_beta[BU]
    lambdai=init_lambdai[BU]
    betai=init_betai[BU]
    nu=init_nu[BU]
    D1.value=init_D1[BU]
    
    BU=0  #kinetic property feedback and control constants are assumed constant for each burnup level
    
    mw.doubleSpinBoxZ1.setValue(z1)
    mw.doubleSpinBoxZ2.setValue(z2)
            
#text output file template
out.append ('t\tfluks1\tfluks2\tP\tTf\tTc\tv\tI\tXe\tPm\tSm\tz1\tz2\trho\tpcrit\tTfin\tTcin\tmdotf\tmdotc\tc1\tc2\tc3\tc4\tc5\tc6\n')
with open(output_directory, "w+") as fl: #ubah direktori output di sini
    fl.writelines(out)

    
#######################Reactor Dynamic Functions###############################
def ff1(): #fast flux equation
    global beta,nu,sigf1,sigf2,fluks,lambdai,ci,siga1,B,D1,sigs12
    clsum=0
    for i in range (0,6):
        clsum=clsum+lambdai[i]*c[i]
    return ((1-beta)*nu[1]*sigf2.value*fluks[1]+clsum)/((siga1.value+B**2*D1.value)+sigs12.value-(1-beta)*nu[0]*sigf1.value)

def ff2(t,y): #thermal flux equation
    global lp,rho,beta,fluks,c,lambdai,sigf2,nu
    clsum=0
    for i in range (0,6):
        clsum=clsum+lambdai[i]*c[i]
    return y/lp.value*(rho.value-beta)/(1-rho.value) + 1/(lp.value*sigf2.value*nu[1]*(1-rho.value))*clsum

def fc(t,y): #delayed neutron precursor group equation
    global lambdai,c,ci,betai,fluks,sigf1,sigf2,nu
    return -lambdai[ci]*y+betai[ci]*(nu[0]*sigf1.value*fluks[0]+nu[1]*sigf2.value*fluks[1])

def fI(t,y): #iodine equation
    global I,fluks,sigf1,sigf2
    return -I.Lambda*y-(I.Siga[0]*fluks[0]+I.Siga[1]*fluks[1])*y+I.FissionYield*(sigf1.value*fluks[0]+sigf2.value*fluks[1])
    
def fXe(t,y): #xenon equation
    global Xe,fluks,sigf1,sigf2,I
    return -Xe.Lambda*y-(Xe.Siga[0]*fluks[0]+Xe.Siga[1]*fluks[1])*y+Xe.FissionYield*(sigf1.value*fluks[0]+sigf2.value*fluks[1])+I.Lambda*I.value
    
def fPm(t,y): #promethium equation
    global Pm,fluks,sigf1,sigf2
    return -Pm.Lambda*y-(Pm.Siga[0]*fluks[0]+Pm.Siga[1]*fluks[1])*y+Pm.FissionYield*(sigf1.value*fluks[0]+sigf2.value*fluks[1])
    
def fSm(t,y): #samarium equation
    global Sm,fluks,sigf1,sigf2,Pm
    return -Sm.Lambda*y-(Sm.Siga[0]*fluks[0]+Sm.Siga[1]*fluks[1])*y+Sm.FissionYield*(sigf1.value*fluks[0]+sigf2.value*fluks[1])+Pm.Lambda*Pm.value

def fTf(t,y): #fuel temperature equation
    global Vf,densf,cpf,mdotf,Tfin,Tf,U,N,D,L,Tc,P
    return (2*mdotf*cpf*(Tfin-y)+P-U*D*N*math.pi*L*(y-Tc))/(Vf*densf(Tf)*cpf)

def fTc(t,y): #coolant temperature equation
    global Vc,densc,cpc,mdotc,Tcin,Tc,U,N,D,L,Tf
    return (U*D*N*math.pi*L*(Tf-y)+2*mdotc*cpc(Tc)*(Tcin-y))/(Vc*densc(Tc)*cpc(Tc))

def output(): #adding output graph array and text
    global t,rho,fluks,P,Tf,v,z1,z2,Tc,I,Pm,Xe,Sm,tArray,fluks2Array,rhoArray,TfArray,TcArray, PArray, critArray, pcritArray,XeArray,SmArray,IArray,PmArray
    pcritArray.append(beta)
    critArray.append(0)
    PArray.append(P)
    tArray.append(t)
    rhoArray.append(rho.value)
    TfArray.append(Tf)
    TcArray.append(Tc)
    XeArray.append(Xe.value)
    IArray.append(I.value)
    SmArray.append(Sm.value)
    PmArray.append(Pm.value)
    out.append( str(t)+'\t'+str(fluks[0])+'\t'+str(fluks[1])+'\t'+str(P)+'\t'+str(Tf)+'\t'+str(Tc)+'\t'+str(v)+'\t'+str(I.value)+'\t'+str(Xe.value)+'\t'+str(Pm.value)+'\t'+str(Sm.value)+'\t'+str(z1)+'\t'+str(z2)+'\t'+str(rho.value)+'\t'+str(beta)+'\t'+str(Tfin)+'\t'+str(Tcin)+'\t'+str(mdotf)+'\t'+str(mdotc)+'\t'+str(c[0])+'\t'+str(c[1])+'\t'+str(c[2])+'\t'+str(c[3])+'\t'+str(c[4])+'\t'+str(c[5])+'\n')
    with open(output_directory, "w+") as fl: #ubah direktori output di sini
        fl.writelines(out)

def calcYZ(f,h,t,y): #calculating RKF45 constants and solutions
    k1=h*f(t,y)
    k2=h*f(t+1.0/4*h,y+1.0/4*k1)
    k3=h*f(t+3.0/8*h,y+3.0/32*k1+9.0/32*k2)
    k4=h*f(t+12.0/13*h,y+1932.0/2197*k1-7200.0/2197*k2+7296.0/2197*k3)
    k5=h*f(t+h,y+439.0/216*k1-8.0*k2+3680.0/513*k3-845.0/4104*k4)
    k6=h*f(t+1.0/2*h,y-8.0/27*k1+2.0*k2-3544.0/2565*k3+1859.0/4104*k4-11.0/40*k5)
    yk=y+25.0/216*k1+1408.0/2565*k3+2197.0/4101*k4-1.0/5*k5
    zk=y+16.0/135*k1+6656.0/12825*k3+28561.0/56430*k4-9.0/50*k5+2.0/55*k6
    return yk, zk

def RKF45(f,h,t,y): #performing RKF45
    global RKok
    tol=0.001

    yk,zk = calcYZ(f,h,t,y)
    if yk!=zk:
        e=abs((yk-zk)/yk)
        s=(tol*h/2/e)**0.25
        h=s*h
    else:
        e=abs(yk-zk)
        h=1
    if h>1: h=1    
    if e>=0.001:
        RKok.append(False)
    else:
        RKok.append(True)
    return h, zk

def Jump(): #execution for each tick
    global t, dt, fluks, P, Tf, Tc, U, v, z1, z2, Tfin, Tcin, mdotf, mdotc, out, ci, rho, N, D, L, V, lp, beta, betai, siga1, sigf1,sigf2, nu, sigs12, c, lambdai, betai, Xe,Sm,I,Pm,RKok,BU,B

    tin=0.0
    tj=1.0
    mshow=2.0
    awal1=True
    kali=1.0
    
    while tin<=tj:
  
        RKok=[False]
        while False in RKok:
            cnew=[0,0,0,0,0,0]            
            RKok=[]
            dtnew=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
            for i in range (0,6):
                ci=i
                dtnew[ci],cnew[ci]=RKF45(fc,dt,t,c[ci])

            dtnew[6],fluks2new=RKF45(ff2,dt,t,fluks[1])

            dtnew[7], Tfnew=RKF45(fTf,dt,t,Tf)
            dtnew[8], Tcnew=RKF45(fTc,dt,t,Tc)

            dtnew[9], Inew=RKF45(fI,dt,t,I.value)
            dtnew[10], Xenew=RKF45(fXe,dt,t,Xe.value)
            dtnew[11], Pmnew=RKF45(fPm,dt,t,Pm.value)
            dtnew[12], Smnew=RKF45(fSm,dt,t,Sm.value)
            
            if False in RKok or (not False in RKok and min(dtnew) > dt):
                dt=min(dtnew)
                RKok.append(False)

        for i in range (0,6): 
            ci=i
            c[ci]=cnew[ci]               
        fluks[1]=fluks2new
        dTf=Tfnew-Tf
        Tf=Tfnew
        dXe=Xenew-Xe.value
        Xe.value=Xenew
        dSm=Smnew-Sm.value
        Sm.value=Smnew
        Pm.value=Pmnew
        I.value=Inew
        Tc=Tcnew
        fluks[0]=ff1()   
        P=(sigf1.value*fluks[0]+sigf2.value*fluks[1])*1000**2*190.0*1.6021*10.0**-13.0*V #W   

        
        
        if awal1:
            #control in
            vnew=float(mw.labelV.text())
            dv=vnew-v
            v=vnew
            z1new=mw.doubleSpinBoxZ1.value()
            dz1=z1new-z1
            z1=z1new
            z2new=mw.doubleSpinBoxZ2.value()
            dz2=z2new-z2
            z2=z2new
            Tfin=float(mw.labelTfin.text())
            mdotf=float(mw.labelMdotf.text())
            Tcin=float(mw.labelTcin.text())
            mdotc=float(mw.labelMdotc.text())
            awal1=False

        rho.value=rho.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)
        siga1.value=siga1.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)        
        sigs12.value=sigs12.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)        
        D1.value=D1.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)        
        sigf1.value=sigf1.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)        
        sigf2.value=sigf2.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)        
        lp.value=lp.feedback((Tf-dTf/2),dTf,(v-dv/2),dv,(Xe.value-dXe/2),dXe,(Sm.value-dSm/2),dSm,(z1-dz1/2),dz1,(z2-dz2/2),dz2,BU)                
        dTf=0
        dv=0
        dXe=0
        dSm=0
        dz1=0
        dz2=0

        t=t+dt
        tin=tin+dt

        if tin>=(kali*tj/mshow):
            output()
            kali=kali+1

##############################Inheriting Window################################
class BeginningBurnup(QWidget, Ui_Awal):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)        

class TrackedNuclide(QWidget, Ui_TrackedNuclide):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        
class Simulator(QMainWindow, Ui_LFIPRSimulator):
    def __init__(self):
        QMainWindow.__init__(self)
        self.beginningburnup=BeginningBurnup()
        self.beginningburnup.show()
        self.beginningburnup.comboBoxBU.currentIndexChanged.connect(self.BUchanged)
        self.beginningburnup.pushButtonMulai.clicked.connect(self.started)
        
    def BUchanged(self):
        global BU
        if self.beginningburnup.comboBoxBU.currentIndex()==0:
            BU=0
        if self.beginningburnup.comboBoxBU.currentIndex()==1:
            BU=1
        if self.beginningburnup.comboBoxBU.currentIndex()==2:
            BU=2
                
    def started(self):
        self.setupUi(self)
        initial()
        output()
        self.beginningburnup.close()
        self.trackedXenon=TrackedNuclide()
        self.trackedSamarium=TrackedNuclide()
        self.graphIodine=self.trackedXenon.mplwidgetI.figure.add_subplot(111)
        self.graphXenon=self.trackedXenon.mplwidgetXe.figure.add_subplot(111)
        self.graphPromethium=self.trackedSamarium.mplwidgetI.figure.add_subplot(111)
        self.graphSamarium=self.trackedSamarium.mplwidgetXe.figure.add_subplot(111)        
        self.myTimer = QTimer()
        self.myTimer.start()
        self.showMaximized()
        self.graphPower=self.mplwidgetPower.figure.add_subplot(111)
        self.graphReactivity=self.mplwidgetReactivity.figure.add_subplot(111)
        self.graphTemperature=self.mplwidgetTemperature.figure.add_subplot(111)
        self.dialV.valueChanged.connect(self.changeV)
        self.horizontalSliderTfin.valueChanged.connect(self.changeTfin)
        self.horizontalSliderMdotf.valueChanged.connect(self.changeMdotf)
        self.horizontalSliderTcin.valueChanged.connect(self.changeTcin)
        self.horizontalSliderMdotc.valueChanged.connect(self.changeMdotc)
        self.horizontalSliderPlot.valueChanged.connect(self.changeArray)
        self.checkBoxPrecision.clicked.connect(self.changePrecision)
        self.pushButtonInitiate.clicked.connect(self.addNeutron)
        self.actionXenon_135.triggered.connect(self.showXenon)        
        self.actionSamarium_149_dan_Promethium_149.triggered.connect(self.showSamarium)
        self.myTimer.setInterval(100)
        self.myTimer.timeout.connect(self.aksi)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 521, 377)
        self.graphicsView.setScene(self.scene)
        orange = QBrush(QColor(255, 170, 0))
        darkGreen = QBrush(QColor(0, 150, 0))
        green = QBrush(QColor(0, 200, 0))
        blue = QBrush(QColor(0, 85, 255))
        self.scene.addRect(self.scene.sceneRect(), Qt.gray, blue)
        self.scene.addRect(0, 0, 100, 377, Qt.black, Qt.gray)
        self.scene.addRect(421, 0, 100, 377, Qt.black, Qt.gray)
        self.scene.addRect(198, 126, 125, 125, Qt.black, orange)
        self.scene.addRect(207, 126, 3, 125, Qt.black, blue)        
        self.scene.addRect(217, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(227, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(237, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(314, 126, 3, 125, Qt.black, blue)        
        self.scene.addRect(304, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(294, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(284, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(246, (126-z1*125/60), 29, 125, Qt.black, darkGreen)
        self.scene.addRect(323, (126-z2*125/60), 20, 125, Qt.black, darkGreen)
        self.scene.addRect(178, (126-z2*125/60), 20, 125, Qt.black, darkGreen)
        self.scene.addRect(246, (251-z1*125/60), 29, 125, Qt.black, green)
        self.scene.addRect(323, (251-z2*125/60), 20, 125, Qt.black, green)
        self.scene.addRect(178, (251-z2*125/60), 20, 125, Qt.black, green)
        self.doubleSpinBoxZ1.valueChanged.connect(self.changeAnimation)
        self.doubleSpinBoxZ2.valueChanged.connect(self.changeAnimation)      

    def showXenon(self):
        self.trackedXenon.show()        
    def showSamarium(self):
        self.trackedSamarium.show()
    def changeAnimation(self):
        global z1,z2
        orange = QBrush(QColor(255, 170, 0))
        darkGreen = QBrush(QColor(0, 150, 0))
        green = QBrush(QColor(0, 200, 0))
        blue = QBrush(QColor(0, 85, 255))
        self.scene.clear()
        self.scene.addRect(self.scene.sceneRect(), Qt.gray, blue)
        self.scene.addRect(0, 0, 100, 377, Qt.black, Qt.gray)
        self.scene.addRect(421, 0, 100, 377, Qt.black, Qt.gray)
        self.scene.addRect(198, 126, 125, 125, Qt.black, orange)
        self.scene.addRect(246, (126-z1*125/60), 29, 125, Qt.black, darkGreen)
        self.scene.addRect(323, (126-z2*125/60), 20, 125, Qt.black, darkGreen)
        self.scene.addRect(178, (126-z2*125/60), 20, 125, Qt.black, darkGreen)
        self.scene.addRect(246, (251-z1*125/60), 29, 125, Qt.black, green)
        self.scene.addRect(323, (251-z2*125/60), 20, 125, Qt.black, green)
        self.scene.addRect(178, (251-z2*125/60), 20, 125, Qt.black, green)
        self.scene.addRect(207, 126, 3, 125, Qt.black, blue)        
        self.scene.addRect(217, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(227, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(237, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(314, 126, 3, 125, Qt.black, blue)        
        self.scene.addRect(304, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(294, 126, 3, 125, Qt.black, blue)                
        self.scene.addRect(284, 126, 3, 125, Qt.black, blue)                        
    
    def addNeutron(self):
        global fluks
        fluks[1]=fluks[1]+self.doubleSpinBoxNeutron.value()        
    def changePrecision(self):
        if self.doubleSpinBoxZ1.singleStep()==0.1:   
            self.doubleSpinBoxZ1.setSingleStep(0.01)
            self.doubleSpinBoxZ2.setSingleStep(0.01)
        else:
            self.doubleSpinBoxZ1.setSingleStep(0.1)
            self.doubleSpinBoxZ2.setSingleStep(0.1) 
    def aksi(self):
        Jump()
        self.changeMinPlot()
        self.changePlot()
    def changeMinPlot(self):
        self.horizontalSliderPlot.setMaximum(len(tArray))        
    def changeArray(self):
        global PArray,TfArray,TcArray,rhoArray,tArray,critArray,pcritArray,XeArray,SmArray,IArray,PmArray
        ubah=PArray[self.horizontalSliderPlot.value():]
        PArray=ubah
        ubah=critArray[self.horizontalSliderPlot.value():]
        critArray=ubah
        ubah=pcritArray[self.horizontalSliderPlot.value():]
        pcritArray=ubah
        ubah=tArray[self.horizontalSliderPlot.value():]
        tArray=ubah
        ubah=rhoArray[self.horizontalSliderPlot.value():]
        rhoArray=ubah
        ubah=TfArray[self.horizontalSliderPlot.value():]
        TfArray=ubah
        ubah=TcArray[self.horizontalSliderPlot.value():]
        TcArray=ubah
        ubah=IArray[self.horizontalSliderPlot.value():]
        IArray=ubah        
        ubah=XeArray[self.horizontalSliderPlot.value():]
        XeArray=ubah        
        ubah=PmArray[self.horizontalSliderPlot.value():]
        PmArray=ubah        
        ubah=SmArray[self.horizontalSliderPlot.value():]
        SmArray=ubah                
        self.horizontalSliderPlot.setValue(0)        
    def changePlot(self):
        global PArray,TfArray,TcArray,rhoArray,tArray,critArray,pcritArray,XeArray,SmArray,IArray,PmArray
        self.graphPower.plot(tArray,PArray)
        self.graphPower.set_title('Daya')
        self.graphPower.set_ylabel('Watt')
        self.graphPower.set_xlabel('sekon')
        self.graphPower.grid()
        self.graphPower.figure.canvas.draw()        
        self.graphReactivity.plot(tArray,rhoArray,'-g',tArray,critArray,'--b',tArray,pcritArray,'--r')
        self.graphReactivity.set_title('Reaktifitas')
        self.graphReactivity.set_xlabel('sekon')
        self.graphReactivity.grid()
        self.graphReactivity.figure.canvas.draw()        
        self.graphTemperature.plot(tArray,TfArray,'-r',tArray,TcArray,'-b')
        self.graphTemperature.set_title('Temperatur')
        self.graphTemperature.set_ylabel('Celcius')
        self.graphTemperature.set_xlabel('sekon')
        self.graphTemperature.grid()
        self.graphTemperature.figure.canvas.draw() 
        if self.trackedXenon.isActiveWindow():
            self.graphXenon.plot(tArray,XeArray)
            self.graphXenon.set_title('Konsentrasi Xenon')
            self.graphXenon.set_ylabel('/cm3')
            self.graphXenon.set_xlabel('sekon')
            self.graphXenon.grid()
            self.graphXenon.figure.canvas.draw()        
            self.graphIodine.plot(tArray,IArray)
            self.graphIodine.set_title('Konsentrasi Iodine')
            self.graphIodine.set_ylabel('/cm3')
            self.graphIodine.set_xlabel('sekon')
            self.graphIodine.grid()
            self.graphIodine.figure.canvas.draw()        
        if self.trackedSamarium.isActiveWindow():
            self.graphSamarium.plot(tArray,SmArray)
            self.graphSamarium.set_title('Konsentrasi Samarium')
            self.graphSamarium.set_ylabel('/cm3')
            self.graphSamarium.set_xlabel('sekon')
            self.graphSamarium.grid()
            self.graphSamarium.figure.canvas.draw()        
            self.graphPromethium.plot(tArray,PmArray)
            self.graphPromethium.set_title('Konsentrasi Promethium')
            self.graphPromethium.set_ylabel('/cm3')
            self.graphPromethium.set_xlabel('sekon')
            self.graphPromethium.grid()
            self.graphPromethium.figure.canvas.draw()        
        
       
    def changeV(self):
        self.labelV.setNum(self.dialV.value()*1.0/100)
    def changeTfin(self):
        self.labelTfin.setNum(self.horizontalSliderTfin.value()*1.0/10)
    def changeMdotf(self):
        self.labelMdotf.setNum(self.horizontalSliderMdotf.value()*1.0/10)
    def changeTcin(self):
        self.labelTcin.setNum(self.horizontalSliderTcin.value()*1.0/10)
    def changeMdotc(self):
        self.labelMdotc.setNum(self.horizontalSliderMdotc.value()*1.0/10)

#Initial Output and Starting Application
app = QApplication(sys.argv)
mw=Simulator()
sys.exit(app.exec_())