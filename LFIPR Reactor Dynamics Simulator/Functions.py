class DependentKineticProperty():  
    def __init__(self):
        self.value=0
        self.a1Tf=0,0,0
        self.a2Tf=0,0,0
        self.a1v=0,0,0
        self.a2v=0,0,0
        self.a1Xe=0,0,0
        self.a1Sm=0,0,0
        self.a51z10=0,0,0
        self.a50z10=0,0,0
        self.a51z11=0,0,0
        self.a50z11=0,0,0
        self.a51z12=0,0,0
        self.a50z12=0,0,0
        self.a51z13=0,0,0
        self.a50z13=0,0,0
        self.a51z14=0,0,0
        self.a50z14=0,0,0
        self.a51z15=0,0,0
        self.a50z15=0,0,0
        self.a41z10=0,0,0
        self.a40z10=0,0,0
        self.a41z11=0,0,0
        self.a40z11=0,0,0
        self.a41z12=0,0,0
        self.a40z12=0,0,0
        self.a41z13=0,0,0
        self.a40z13=0,0,0
        self.a41z14=0,0,0
        self.a40z14=0,0,0
        self.a41z15=0,0,0
        self.a40z15=0,0,0
        self.a31z10=0,0,0
        self.a30z10=0,0,0
        self.a31z11=0,0,0
        self.a30z11=0,0,0
        self.a31z12=0,0,0
        self.a30z12=0,0,0
        self.a31z13=0,0,0
        self.a30z13=0,0,0
        self.a31z14=0,0,0
        self.a30z14=0,0,0
        self.a31z15=0,0,0
        self.a30z15=0,0,0
        self.a21z10=0,0,0
        self.a20z10=0,0,0
        self.a21z11=0,0,0
        self.a20z11=0,0,0
        self.a21z12=0,0,0
        self.a20z12=0,0,0
        self.a21z13=0,0,0
        self.a20z13=0,0,0
        self.a21z14=0,0,0
        self.a20z14=0,0,0
        self.a21z15=0,0,0
        self.a20z15=0,0,0
        self.a11z10=0,0,0
        self.a10z10=0,0,0
        self.a11z11=0,0,0
        self.a10z11=0,0,0
        self.a11z12=0,0,0
        self.a10z12=0,0,0
        self.a11z13=0,0,0
        self.a10z13=0,0,0
        self.a11z14=0,0,0
        self.a10z14=0,0,0
        self.a11z15=0,0,0
        self.a10z15=0,0,0

        self.a51z20=0,0,0
        self.a50z20=0,0,0
        self.a51z21=0,0,0
        self.a50z21=0,0,0
        self.a51z22=0,0,0
        self.a50z22=0,0,0
        self.a51z23=0,0,0
        self.a50z23=0,0,0
        self.a51z24=0,0,0
        self.a50z24=0,0,0
        self.a51z25=0,0,0
        self.a50z25=0,0,0
        self.a41z20=0,0,0
        self.a40z20=0,0,0
        self.a41z21=0,0,0
        self.a40z21=0,0,0
        self.a41z22=0,0,0
        self.a40z22=0,0,0
        self.a41z23=0,0,0
        self.a40z23=0,0,0
        self.a41z24=0,0,0
        self.a40z24=0,0,0
        self.a41z25=0,0,0
        self.a40z25=0,0,0
        self.a31z20=0,0,0
        self.a30z20=0,0,0
        self.a31z21=0,0,0
        self.a30z21=0,0,0
        self.a31z22=0,0,0
        self.a30z22=0,0,0
        self.a31z23=0,0,0
        self.a30z23=0,0,0
        self.a31z24=0,0,0
        self.a30z24=0,0,0
        self.a31z25=0,0,0
        self.a30z25=0,0,0
        self.a21z20=0,0,0
        self.a20z20=0,0,0
        self.a21z21=0,0,0
        self.a20z21=0,0,0
        self.a21z22=0,0,0
        self.a20z22=0,0,0
        self.a21z23=0,0,0
        self.a20z23=0,0,0
        self.a21z24=0,0,0
        self.a20z24=0,0,0
        self.a21z25=0,0,0
        self.a20z25=0,0,0
        self.a11z20=0,0,0
        self.a10z20=0,0,0
        self.a11z21=0,0,0
        self.a10z21=0,0,0
        self.a11z22=0,0,0
        self.a10z22=0,0,0
        self.a11z23=0,0,0
        self.a10z23=0,0,0
        self.a11z24=0,0,0
        self.a10z24=0,0,0
        self.a11z25=0,0,0
        self.a10z25=0,0,0

    def feedback(self,Tf,dTf,v,dv,Xe,dXe,Sm,dSm,z1,dz1,z2,dz2,BU):
        return self.value+self.aTf(Tf,BU)*dTf+self.av(v,BU)*dv+self.aXe(BU)*dXe+self.aSm(BU)*dSm+self.wz1(z1,z2,BU)*dz1+self.wz2(z1,z2,BU)*dz2
    def aTf(self,Tf,BU):
        return 2*self.a2Tf[BU]*Tf + self.a1Tf[BU]
    def av(self,v,BU):
        return 2*self.a2v[BU]*v + self.a1v[BU]
    def aXe(self,BU):
        return self.a1Xe[BU]
    def aSm(self,BU):
        return self.a1Sm[BU]
    def wz1(self,z1,z2,BU):
        return 5*self.a5z1(z2,BU)*z1**4+4*self.a4z1(z2,BU)*z1**3+3*self.a3z1(z2,BU)*z1**2+2*self.a2z1(z2,BU)*z1+self.a1z1(z2,BU)
    def wz2(self,z1,z2,BU):
        return 5*self.a5z2(z1,BU)*z2**4+4*self.a4z2(z1,BU)*z2**3+3*self.a3z2(z1,BU)*z2**2+2*self.a2z2(z1,BU)*z2+self.a1z2(z1,BU)
    def a5z1(self,z2,BU):
        if 0<=z2<10: return self.a51z10[BU]*z2+self.a50z10[BU]
        if 10<=z2<20: return self.a51z11[BU]*z2+self.a50z11[BU]
        if 20<=z2<30: return self.a51z12[BU]*z2+self.a50z12[BU]
        if 30<=z2<40: return self.a51z13[BU]*z2+self.a50z13[BU]
        if 40<=z2<50: return self.a51z14[BU]*z2+self.a50z14[BU]
        if 50<=z2<=60: return self.a51z15[BU]*z2+self.a50z15[BU]          
    def a4z1(self,z2,BU):
        if 0<=z2<10: return self.a41z10[BU]*z2+self.a40z10[BU]
        if 10<=z2<20: return self.a41z11[BU]*z2+self.a40z11[BU]
        if 20<=z2<30: return self.a41z12[BU]*z2+self.a40z12[BU]
        if 30<=z2<40: return self.a41z13[BU]*z2+self.a40z13[BU]
        if 40<=z2<50: return self.a41z14[BU]*z2+self.a40z14[BU]
        if 50<=z2<=60: return self.a41z15[BU]*z2+self.a40z15[BU]          
    def a3z1(self,z2,BU):
        if 0<=z2<10: return self.a31z10[BU]*z2+self.a30z10[BU]
        if 10<=z2<20: return self.a31z11[BU]*z2+self.a30z11[BU]
        if 20<=z2<30: return self.a31z12[BU]*z2+self.a30z12[BU]
        if 30<=z2<40: return self.a31z13[BU]*z2+self.a30z13[BU]
        if 40<=z2<50: return self.a31z14[BU]*z2+self.a30z14[BU]
        if 50<=z2<=60: return self.a31z15[BU]*z2+self.a30z15[BU]          
    def a2z1(self,z2,BU):
        if 0<=z2<10: return self.a21z10[BU]*z2+self.a20z10[BU]
        if 10<=z2<20: return self.a21z11[BU]*z2+self.a20z11[BU]
        if 20<=z2<30: return self.a21z12[BU]*z2+self.a20z12[BU]
        if 30<=z2<40: return self.a21z13[BU]*z2+self.a20z13[BU]
        if 40<=z2<50: return self.a21z14[BU]*z2+self.a20z14[BU]
        if 50<=z2<=60: return self.a21z15[BU]*z2+self.a20z15[BU]          
    def a1z1(self,z2,BU):
        if 0<=z2<10: return self.a11z10[BU]*z2+self.a10z10[BU]
        if 10<=z2<20: return self.a11z11[BU]*z2+self.a10z11[BU]
        if 20<=z2<30: return self.a11z12[BU]*z2+self.a10z12[BU]
        if 30<=z2<40: return self.a11z13[BU]*z2+self.a10z13[BU]
        if 40<=z2<50: return self.a11z14[BU]*z2+self.a10z14[BU]
        if 50<=z2<=60: return self.a11z15[BU]*z2+self.a10z15[BU]          
    def a5z2(self,z1,BU):
        if 0<=z1<10: return self.a51z20[BU]*z1+self.a50z20[BU]
        if 10<=z1<20: return self.a51z21[BU]*z1+self.a50z21[BU]
        if 20<=z1<30: return self.a51z22[BU]*z1+self.a50z22[BU]
        if 30<=z1<40: return self.a51z23[BU]*z1+self.a50z23[BU]
        if 40<=z1<50: return self.a51z24[BU]*z1+self.a50z24[BU]
        if 50<=z1<=60: return self.a51z25[BU]*z1+self.a50z25[BU]          
    def a4z2(self,z1,BU):
        if 0<=z1<10: return self.a41z20[BU]*z1+self.a40z20[BU]
        if 10<=z1<20: return self.a41z21[BU]*z1+self.a40z21[BU]
        if 20<=z1<30: return self.a41z22[BU]*z1+self.a40z22[BU]
        if 30<=z1<40: return self.a41z23[BU]*z1+self.a40z23[BU]
        if 40<=z1<50: return self.a41z24[BU]*z1+self.a40z24[BU]
        if 50<=z1<=60: return self.a41z25[BU]*z1+self.a40z25[BU]          
    def a3z2(self,z1,BU):
        if 0<=z1<10: return self.a31z20[BU]*z1+self.a30z20[BU]
        if 10<=z1<20: return self.a31z21[BU]*z1+self.a30z21[BU]
        if 20<=z1<30: return self.a31z22[BU]*z1+self.a30z22[BU]
        if 30<=z1<40: return self.a31z23[BU]*z1+self.a30z23[BU]
        if 40<=z1<50: return self.a31z24[BU]*z1+self.a30z24[BU]
        if 50<=z1<=60: return self.a31z25[BU]*z1+self.a30z25[BU]          
    def a2z2(self,z1,BU):
        if 0<=z1<10: return self.a21z20[BU]*z1+self.a20z20[BU]
        if 10<=z1<20: return self.a21z21[BU]*z1+self.a20z21[BU]
        if 20<=z1<30: return self.a21z22[BU]*z1+self.a20z22[BU]
        if 30<=z1<40: return self.a21z23[BU]*z1+self.a20z23[BU]
        if 40<=z1<50: return self.a21z24[BU]*z1+self.a20z24[BU]
        if 50<=z1<=60: return self.a21z25[BU]*z1+self.a20z25[BU]          
    def a1z2(self,z1,BU):
        if 0<=z1<10: return self.a11z20[BU]*z1+self.a10z20[BU]
        if 10<=z1<20: return self.a11z21[BU]*z1+self.a10z21[BU]
        if 20<=z1<30: return self.a11z22[BU]*z1+self.a10z22[BU]
        if 30<=z1<40: return self.a11z23[BU]*z1+self.a10z23[BU]
        if 40<=z1<50: return self.a11z24[BU]*z1+self.a10z24[BU]
        if 50<=z1<=60: return self.a11z25[BU]*z1+self.a10z25[BU]          

class Nuclide():
    def __init__(self):
        self.value=0
        self.Lambda=0
        self.FissionYield=0,0
        self.Siga=0,0