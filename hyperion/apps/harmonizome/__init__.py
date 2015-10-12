import hyperion.registrar as reg


from hyperion.apps.harmonizome.checkmain import CheckMain


reg.register_health_check(CheckMain('foo', 10))
reg.register_health_check(CheckMain('bar', 5))
reg.start()