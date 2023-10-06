from typer import Typer,  echo
from atumm.tool.domain.usecases.create_service import CreateServiceCommand,\
    CreateServiceUseCase
from atumm.tool.domain.usecases.add_rest_resource import AddRestResourceCommand,\
    AddRestResourceUseCase

app = Typer()

@app.command()
def create_service(service_name: str):
    """
    Create a new service with the given service name.
    """
    command = CreateServiceCommand(service_name=service_name)
    use_case = CreateServiceUseCase()
    use_case.execute(command)
    echo(f"✅ Service '{service_name}' created successfully!")

@app.command()
def create_rest_resource(service_name: str, resource_name: str):
    """
    Create a new REST resource with the given service and resource name.
    """
    command = AddRestResourceCommand(service_name=service_name, resource_name=resource_name)
    use_case = AddRestResourceUseCase()
    use_case.execute(command)
    echo(f"✅ REST resource '{resource_name}' for service '{service_name}' created successfully!")

if __name__ == "__main__":
    app()
