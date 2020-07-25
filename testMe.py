
import FlaskApp
import FlaskApp.vampireGen as vG
import json

if __name__ == '__main__':
    nsc = {'vorname': 'Eldana', 'nachname': 'Rozell', 'treeSeed':'Alrik Alrikson#0#Tremere', 'Clan':'Tremere','Powerlevel':0}
    nsc['RelationTree'] = vG.MakeRelationTree(nsc)
    print(json.dumps(vG.MakeRelationTree(nsc),indent=2))
    #print(vG.FindCreator(nsc,vG.MakeRelationTree(nsc)))
    #print(vG.FindChildren(nsc,vG.MakeRelationTree(nsc)))
    #print(vG.GetLevelInTree({'vorname': 'Moritz', 'nachname': 'Siedel', 'treeSeed':'Alrik Alrikson#0#Tremere', 'Clan':'Tremere','Powerlevel':0},vG.MakeRelationTree(nsc)))
    #print(vG.GetLevelInTree(nsc,vG.MakeRelationTree(nsc)))
    print(vG.PrintLineageTree(nsc))