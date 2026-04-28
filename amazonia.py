#amazonia.py
#Programa Sobre animales de la Amazonia

animales = [
    {"nombre": "Jaguar", "dato": " Es el felino mas grande de America."},
     { "nombre": "Parrot","dato":"I would like to have a parrot because they're realy beautiful"}
]
print("=== Animales de la Amazonia ===")
for animal in animales :
    print(f"- {animal["nombre"]}:{animal["dato"]}")