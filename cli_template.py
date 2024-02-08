from jinja2 import Template
import yaml
import os

def generate_config (y, t):
    try:
        with open (y, 'r') as file:
            int = yaml.safe_load(file)
    except Exception as e:
        print ('yaml dosyasi okunurken hata oldu', e)
        return None
    
    try:
        with open (t,'r') as file:
            template = Template(file.read())
    except Exception as e:
        print ('template dosyasi okunurken hata oluştu', e)
        return None

    return template.render(router_interface = int['interfaces'])

if __name__ == '__main__':
    y = 'jinja_template/yaml_file.yaml'
    t = 'jinja_template/template_file.j2'

config_file = generate_config(y,t)

if config_file is not None:
    print(config_file)
else:
    print ('hata oldu')

