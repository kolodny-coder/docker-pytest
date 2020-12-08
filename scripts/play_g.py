import requests


def attren_human_skin(resistance):
    if resistance < 300 or resistance > 1000:
        raise ValueError('please set a valid ohms input')
    return resistance

def arduino(power, applicator_input):
    assert applicator_input*0.9 < power < applicator_input * 1.1




def applicator_mesaurment(pigmantion_level):
    pigmantion_level_to_volt = pigmantion_level * 1000
    return pigmantion_level_to_volt



def power_meter(resistance, pigmantion_level_to_volt):
    power = (pigmantion_level_to_volt * pigmantion_level_to_volt)/resistance
    return power

def automative(self):
    url = 'htttps://dummy.automative'
    power = self.power_meter()
    result = requests.post(url, data=power)
    return result





def applicator_power_output():
    url = ('htttps://dummy.automative')
    response = requests.get(url, params=desierd_power)
    json_response = response.json()
    return json_response.get('desired_power')



