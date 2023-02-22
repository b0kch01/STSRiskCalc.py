
<div align=center>

# STSRiskCalc.py
```
A python library for handling the STS Short-Term Risk Calculator
```

</div>

# Installation & Usage
```console
pip install -r requirements.txt
```

```python
from stsriskcalc import STSRiskCalc

calc = STSRiskCalc({...payload...})
calc.calc_risks() # {'predmort': 0.01729, 'predmm': ...}

calc.set_payload({...new payload...})
calc.calc_risks() # {'predmort': 0.02469, 'predmm': ...}

calc.calc_risk({}) # Will raise HTTP error...
```

# Required Fields
```
age
weightkg
heightcm
hct
wbc
platelets
creatlst
medadpidis
hdef
calculatedbmi
procid
```

# Optional Fields
```
alcohol
arrhythafib
arrhythaflutter
arrhythatrfib
arrhythsecond
arrhythsss
arrhyththird
arrhythvv
cancer
cardsymptimeofadm
carshock
cathbasassistwhen
chrlungd
classnyh
cva
cvawhen
cvd
cvdpcarsurg
cvdstenlft
cvdstenrt
cvdtia
diabctrl
diabetes
dialysis
ecmowhen
ethnicity
fhcad
gender
heartfailtmg
hmo2
hypertn
iabpwhen
immsupp
incidenc
infendo
infendty
ivdrugab
laddiststenpercent
liverdis
medacei48
medadp5days
medbeta
medgp
mediastrad
medinotr
medster
miwhen
numdisv
payorprim
payorsecond
pneumonia
poc
pocint1
pocint2
pocint3
pocint4
pocint5
pocint6
pocint7
pocpci
pocpciin
pocpciwhen
prcab
prcvint
prvalve
prvalveproc1
prvalveproc2
prvalveproc3
prvalveproc4
prvalveproc5
pvd
raceasian
raceblack
racenativeam
racnativepacific
resusc
slpapn
status
stenleftmain
surgdt
syncope
tobaccouse
unrespstat
vdaoprimet
vdinsufa
vdinsufm
vdinsuft
vdstena
vdstenm
```