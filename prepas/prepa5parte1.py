db = {
    "profesores":{
        "11666123":{
            "name": "Antonio", 
            "lastname": "Guerra", 
            "materias":{
                "FBTS05": {
                    "name": "algoritmos", 
                    "credits": 3
                }
            }
        }
    },
    "students":{
                "28765432":{
                        "name":"Rommel", 
                        "lastname":"Sanzonetti", 
                        "materias":[
                            "algoritmos", 
                            "matematica",
                            "ingles"
                            ]
                }
    }
}

print(db["profesores"]["11666123"]["lastname"])
for materia in db["students"]["28765432"]["materias"]:
    print(materia)
