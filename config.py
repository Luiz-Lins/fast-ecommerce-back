from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='DYNACONF',
    settings_files=['settings.toml', '.secrets.toml'],
    # includes=['src/*.toml'],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
