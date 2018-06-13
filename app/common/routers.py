import pkgutil


def init_routes(app):
    """Register routes."""
    from .. import views
    from flask.blueprints import Blueprint

    bp_names, modules = _import_submodules_from_package(views)
    for key, value in enumerate(bp_names):
        bp = getattr(modules[key], value)
        if bp and isinstance(bp, Blueprint):
            app.register_blueprint(bp)


def _import_submodules_from_package(package):
    modules = []
    bpnames = []
    # pkgutil.iter_modules,参数是一个包的路径和名字，然后获取包下所有模块
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__,
                                                         prefix=package.__name__ + "."):
        # print(importer, modname, ispkg)
        # FileFinder('/home/sange/PycharmProjects/bian/app/views')
        # app.views.reserve
        # False
        bpnames.append(modname.split('.')[-1])
        modules.append(__import__(modname, fromlist="dummy"))
    return bpnames, modules
