from atumm.core.types import Command, CommandUseCase


class CreateRestResourceCommand(Command):
    service_name: str
    resource_name: str


class CreateRestResourceUseCase(CommandUseCase[CreateRestResourceCommand]):

    async def execute(self, command: CreateRestResourceCommand):
        """
        Create a new REST resource with the given service and resource names.
        """
        base_path = f"thisapp/services/{command.service_name}/entrypoints/rest/{command.resource_name}"
    
        modules = [
            (
                "",
                [
                    "controllers.py",
                    "presenters.py",
                    "responses.py",
                    "routers.py",
                ],
            ),
        ]
    
        for module, files in modules:
            create_module(f"{base_path}/{module}", files)

