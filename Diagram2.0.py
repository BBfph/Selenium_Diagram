import json
import matplotlib.pyplot as plt


# store class objests
array_class_json = []

class class_json_data:
    def __init__(self, Time, Beoltottak, Aktivfertozottek_videk, Aktivfertozottek_budapest, Gyogyultak_videk, Gyogyultak_budapest, Elhunytak_videk, Elhunytak_budapest, Hatosagi_hazikaranten, Mintavetel):
        self.Time = Time
        self.Beoltottak = Beoltottak
        self.Aktivfertozottek_videk = Aktivfertozottek_videk
        self.Aktivfertozottek_budapest = Aktivfertozottek_budapest
        self.Gyogyultak_videk = Gyogyultak_videk
        self.Gyogyultak_budapest = Gyogyultak_budapest
        self.Elhunytak_videk = Elhunytak_videk
        self.Elhunytak_budapest = Elhunytak_budapest
        self.Hatosagi_hazikaranten = Hatosagi_hazikaranten
        self.Mintavetel = Mintavetel


def load_json_to_class():
    with open ("Info.json") as f:
        data = json.load(f)
    
    json_lenght = len(data['Data']) 
    
    for count in range(0 , json_lenght):
        array_class_json.append(class_json_data
            (data['Data'][count]['Time'],
            data['Data'][count]["Beoltottak"],
            data['Data'][count]["Aktivfertozottek videk"],
            data['Data'][count]["Aktivfertozottek budapest"],
            data['Data'][count]["Gyogyultak videk"],
            data['Data'][count]["Gyogyultak budapest"],
            data['Data'][count]["Elhunytak videk"],
            data['Data'][count]["Elhunytak budapest"],
            data['Data'][count]["Hatosagi hazikaranten"],
            data['Data'][count]["Mintavetel"]
        )
    )


def draw_diagram(name_to_get):
    json_lenght = len(array_class_json)

    time_arr = []
    for i in range(0, json_lenght):
        time_arr.append(array_class_json[i].Time)

    current_arr = []
    for i in range(0, json_lenght):
        append_data = array_class_json[i].__dict__[name_to_get]
        current_arr.append(append_data)
    plt.plot(time_arr, current_arr, label = "line 1", marker='o')


    # giving a title to my graph
    plt.title(name_to_get)
    # --- #
    plt.xlabel("Dátom")
    plt.ylabel("Ember")
    plt.show()
    

def options():
    chouse_array = [
        "Beoltottak",
        "Aktivfertozottek_videk",
        "Aktivfertozottek_budapest",
        "Gyogyultak_videk",
        "Gyogyultak_budapest",
        "Elhunytak_videk",
        "Elhunytak_budapest",
        "Hatosagi_hazikaranten",
        "Mintavetel"
    ]
    for i in range(1, len(chouse_array) + 0):
        print("({1}) {0}".format(chouse_array[i],i))

    id_name = input('Kérem adja meg a kategóriát kategoriat: ')
    send = chouse_array[int(id_name) - 1]
    
    return send

def main():
    load_json_to_class()
    
    id = options()

    draw_diagram(id)
##
#
##
if __name__ == '__main__':
    main()    