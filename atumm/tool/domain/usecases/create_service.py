from atumm.core.types import CommandUseCaseSync, Command
from atumm.tool.domain.utils import create_module

class CreateServiceCommand(Command):
    service_name: str


class CreateServiceUseCase(CommandUseCaseSync[CreateServiceCommand]):

    def execute(self, command: CreateServiceCommand):
        """
        Create a new service with the given service name.
        """
        base_path = f"thisapp/services/{command.service_name}"
    
        modules = [
            ("dataproviders/beanie", ["models.py", "repositories.py"]),
            ("dataproviders/alchemy", ["models.py", "repositories.py"]),
            ("domain", ["models.py", "repositories.py", "exceptions.py"]),
            ("domain/usecases", []),
            ("entrypoints", []),
            ("infra/di", []),
            ("infra/tests/domain/usecases", []),
        ]
    
        for module, files in modules:
            create_module(f"{base_path}/{module}", files)
