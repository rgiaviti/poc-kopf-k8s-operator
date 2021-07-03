import kopf


@kopf.on.create('ephemeralvolumeclaims')
def create_fn(body, **kwargs):
    print(f"A handler is called with body: {body}")


@kopf.on.delete('ephemeralvolumeclaims')
def delete_fn(body, **kwargs):
    print(f"Delete: {body}")
