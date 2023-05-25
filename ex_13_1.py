def main():
    import json

    data ='''
    { "name" : "Chuck",
    "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
    }, "email" : { "hide" : "yes"}
    }'''
    info = json.loads(data)
    print('Nombre:', info["name"])
    print('Telefono:', info["phone"])
    print('Hide:', info["email"]["hide"]) 
    
if __name__ == "__main__":
    main()