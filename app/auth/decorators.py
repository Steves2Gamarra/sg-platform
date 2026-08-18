from functools import wraps

from flask import session, redirect, url_for


def login_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if "usuario_id" not in session:
            return redirect(url_for("auth.login"))

        return view(*args, **kwargs)

    return wrapped_view


def role_required(*perfis):

    def decorator(view):

        @wraps(view)
        def wrapped_view(*args, **kwargs):

            if "usuario_id" not in session:
                return redirect(url_for("auth.login"))

            perfil = session.get("usuario_perfil")

            if perfil not in perfis:
                return "Acesso não autorizado", 403

            return view(*args, **kwargs)

        return wrapped_view

    return decorator


