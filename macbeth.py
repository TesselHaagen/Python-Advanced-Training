import xml.etree.ElementTree as ET

tree = ET.parse('macbeth.xml')
root = tree.getroot()

# Find the name of the play
print(f"The title of the play is: {root.find('TITLE').text}")

print("\n".join([x.text for x in root.iter('PERSONA')]))
# Find names of all Persons
person_tree = root.find('PERSONAE')

personen = [person.text for person in person_tree.findall('PERSONA')]

# for pgroup_tree in person_tree.findall('PGROUP'):
#     for person in pgroup_tree.findall('PERSONA'):
#         print(person.text)

personen_pgroup = [person.text for pgroup_tree in person_tree.findall('PGROUP')
                   for person in pgroup_tree.findall('PERSONA') ]

#print("\n".join(personen + personen_pgroup))

# Find names of all the scenes

scenes = [scene_tree.find('TITLE').text 
          for act_tree in root.findall('ACT') 
          for scene_tree in act_tree.findall('SCENE')]

print('\n'.join(scenes))