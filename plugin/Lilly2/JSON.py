import os, sys, glob, random, time, copy, string, re, numbers
from pathlib import Path,PurePosixPath
#sys.path.append(os.getcwd())
from ConsoleColor import print, console

#required  = {'json5'}
#installed = {pkg.key for pkg in pkg_resources.working_set}
#missing   = required - installed
#if missing:
#    python = sys.executable
#    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
#import json5 as json
import json


def jsonFileW(path,data):
    with open(path, 'w') as json_file:
        #json.dump(data, json_file, indent=4)
        d=json.dumps(data, indent=4)
        json_file.write(d)

def jsonFileRead(path,text=None):
    with open(path, 'r', encoding='utf-8') as file:
        text=file.read()
        text=json.loads(text)
        return text
        
        
def getFileList(path,filelist=[]):
    filelist=list(Path().rglob(path))
    return filelist
    


"""
"""
tt=True

js=getFileList("Content/**/*_MDA.json")
#print(js)
for f in js:
    try:
        p=f.parents[0]
        n=f.name.replace("_MDA.json","_MDA_Lilly.json")
        #print(p,n)
        a=Path(p,n)
        
        t=os.path.exists(a)           
        if t and not tt :
            continue
            
        j=jsonFileRead(f)
        #print(j["mechStats"]["table"])
        j["mechStats"]["table"]="DataTable'/Lilly2/Stats/MechStats_Lilly.MechStats_Lilly'"
        j["healthStats"]["table"]="DataTable'/Lilly2/Stats/MechHealthStats_Lilly.MechHealthStats_Lilly'"
        if j["mechDataStats"] is not None:
            j["mechDataStats"]["baseStats"]["baseTons"]=-2000
        j["variantName"]+="_Lilly"
        j["defaultMech"]["id"]+="_Lilly_2"
        j["equipmentAllocation"]["totalTraitSlots"]=100
        j["bIsHeroMech"]=True
        j["bIsDefaultVariant"]=False
        #print(j)
        #print(f)
        print(a)
        jsonFileW(a,j)
    except Exception:
        console.print_exception()
        print(j)
        print(f)
        
js=getFileList("Content/**/*_Loadout.json")
#print(js)
for f in js:
    try:
        p=f.parents[0]
        n=f.name.replace("_Loadout.json","_Loadout_Lilly.json")
        a1=Path(p,n)        
        
        n=f.name.replace("_Loadout.json","_Loadout_Lilly_2.json")
        a2=Path(p,n)
        
        t1=os.path.exists(a1)        
        t2=os.path.exists(a2)              
        if not tt and t1 and t2:
            continue
            
        j=jsonFileRead(f)
        
        j["mechDataAssetId"]["id"]+="_Lilly"
        
        if tt or not t1:
            print(a1)
            jsonFileW(a1,j)
        
        j["installedArmor"]=j["currentArmor"]=j["currentStructure"]={
            "head": 20000,
            "centerTorso": 20000,
            "leftTorso": 20000,
            "rightTorso": 20000,
            "leftArm": 20000,
            "rightArm": 20000,
            "leftLeg": 20000,
            "rightLeg": 20000
        }
        j["installedRearArmor"]=j["currentRearArmor"]={
            "centerTorsoRear": 20000,
            "leftTorsoRear": 20000,
            "rightTorsoRear": 20000
        }   

        if tt or not t2:
            print(a2)
            jsonFileW(a2,j)
            
    except Exception:
        console.print_exception()
        print(j)
        print(f)