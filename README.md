
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

calc = STSRiskCalc({"age": 50, "heightcm": 180, ...payload...})
calc.calc_risks() # {'predmort': 0.01729, 'predmm': ...}

calc.set_payload({...new payload...})
calc.calc_risks() # {'predmort': 0.02469, 'predmm': ...}

calc.calc_risk({}) # Will raise HTTP error...
```

## Example
See [find_optional_fields.py](https://github.com/b0kch01/STSRiskCalc.py/blob/main/find_optional_fields.py) for an example of this library being used.

# Payload (light) Documentation

**NOT OFFICIAL!** These notes are based off of observation.

If you'd like to learn more about these fields,
[refer to this file](https://github.com/b0kch01/STS-Risk-Calculator-Source-Dump/blob/618b9635a3140a61302cb7aab7d8f6a9b3596530/fields.ts).

## Required Fields
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

## Optional Fields
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

## Example Formatting
```json
{
  "age": 50,
  "gender": "Male",
  "raceasian": "Yes",
  "raceblack": "Yes",
  "racenativeam": "Yes",
  "racnativepacific": "Yes",
  "ethnicity": "Yes",
  "payorprim": "Medicare (includes commercially managed options)",
  "payorsecond": "Non-U.S. Plan",
  "surgdt": "12/2/2014",
  "weightkg": 244,
  "heightcm": 123,
  "hct": 23,
  "wbc": 40,
  "platelets": 1234,
  "creatlst": 10,
  "dialysis": "Yes",
  "hypertn": "Yes",
  "immsupp": "Yes",
  "pvd": "Yes",
  "cvd": "Yes",
  "cvdtia": "Yes",
  "cvdpcarsurg": "Yes",
  "mediastrad": "Yes",
  "cancer": "Yes",
  "fhcad": "Yes",
  "slpapn": "Yes",
  "liverdis": "Yes",
  "unrespstat": "Yes",
  "syncope": "Yes",
  "diabetes": "Yes",
  "diabctrl": "Unknown",
  "infendo": "Yes",
  "infendty": "Active",
  "cva": "Yes",
  "cvawhen": "> 30 days",
  "chrlungd": "Lung disease documented, severity unknown",
  "cvdstenrt": "80% to 99%",
  "cvdstenlft": "Not documented",
  "ivdrugab": "Yes",
  "alcohol": ">= 8 drinks/week",
  "pneumonia": "Remote",
  "tobaccouse": "Current every day smoker",
  "hmo2": "Yes, PRN",
  "prcvint": "Yes",
  "prcab": "Yes",
  "prvalve": "Yes",
  "prvalveproc1": "Aortic valve repair, surgical",
  "prvalveproc2": "Aortic valve replacement, transcatheter",
  "prvalveproc3": "Aortic valve repair, surgical",
  "prvalveproc4": "Aortic valve balloon valvotomy/valvuloplasty",
  "prvalveproc5": "",
  "poc": "Yes",
  "pocint1": "Ablation, surgical, atrial arrhythmia",
  "pocint2": "Ablation, surgical, atrial arrhythmia",
  "pocint3": "",
  "pocint4": "",
  "pocint5": "",
  "pocint6": "",
  "pocint7": "",
  "pocpci": "Yes",
  "pocpciwhen": "Yes, at this facility",
  "pocpciin": "<= 6 Hours",
  "miwhen": "<=6 Hrs",
  "heartfailtmg": "Chronic",
  "classnyh": "Class II",
  "cardsymptimeofadm": "No Coronary Symptoms",
  "carshock": "Yes, not at the time of the procedure but within prior 24 hours",
  "arrhythatrfib": "Recent (<= 30 days preop)",
  "arrhythafib": "Persistent",
  "arrhythaflutter": "Recent (<= 30 days preop)",
  "arrhyththird": "Recent (<= 30 days preop)",
  "arrhythsecond": "Recent (<= 30 days preop)",
  "arrhythsss": "Recent (<= 30 days preop)",
  "arrhythvv": "None",
  "medinotr": "Yes",
  "medadp5days": "Contraindicated",
  "medadpidis": "",
  "medacei48": "Yes",
  "medbeta": "No",
  "medster": "Yes",
  "medgp": "Yes",
  "resusc": "No",
  "numdisv": "One",
  "stenleftmain": "No",
  "laddiststenpercent": "50 - 69%",
  "hdef": 32,
  "vdstena": "Yes",
  "vdstenm": "Yes",
  "vdinsufa": "Moderate",
  "vdinsufm": "Severe",
  "vdinsuft": "Severe",
  "vdaoprimet": "Congenital (other than Bicuspid, Unicuspid, or Quadricuspid)",
  "incidenc": "First cardiovascular surgery",
  "status": "Elective",
  "iabpwhen": "Intraop",
  "cathbasassistwhen": "Intraop",
  "ecmowhen": "Preop",
  "calculatedbmi": 161.27966157710358,
  "procid": "1"
}
```
