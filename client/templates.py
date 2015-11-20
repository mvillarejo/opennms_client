# -*- coding: utf-8 -*-
from string import Template


template_services = Template("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><service source="P" status="A"><applications/><notify>Y</notify><serviceType id="$id"><name>$name</name></serviceType></service>""")
# TODO: remove end of lines for a proper representation
# template_services = Template("""
# <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <service source="P" status="A">
#   <applications/>
#   <notify>Y</notify>
#   <serviceType id="$id">
#     <name>$name</name>
#   </serviceType>
# </service>""")


templates = {
    'services': template_services
}