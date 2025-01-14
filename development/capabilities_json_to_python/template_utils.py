from dataclasses import dataclass


def get_capabilities(capabilities_json_path: str | None):
    """
    Returns capabilities from capabilities.json

    Note: path to capabilities.json is grabbed from paths.py
    """
    import json

    from .paths import capabilities_json_path as default_capabilities_json_path

    capabilities_json_path = capabilities_json_path or default_capabilities_json_path

    capabilities = {}

    with open(capabilities_json_path, "r") as f:
        capabilities: dict = json.load(f)

    return capabilities["capabilities"]


@dataclass
class TemplateArgs:
    template_path: str
    output_folder_path: str
    suffix: str
    generate_interface_only_capabilities_in_a_separate_file: bool
    generate_init_file_imports: bool
    generate_registration_methods: bool
    use_supported_decorator: bool


def get_templates_to_generate() -> list[TemplateArgs]:
    """
    Returns a list of templates to generate

    Note: path to templates is grabbed from paths.py
    """
    from .paths import (
        capabilities_to_py_interface,
        capabilities_to_py_interface_out,
        capabilities_to_py_provider,
        capabilities_to_py_provider_out,
        capabilities_to_py_test_interface,
        capabilities_to_py_test_interface_out,
        capabilities_to_py_test,
        capabilities_to_py_test_out,
        capabilities_to_py_factory,
        capabilities_to_py_factory_out,
        capabilities_to_py_proxy,
        capabilities_to_py_proxy_out,
    )

    return [
        TemplateArgs(
            template_path=capabilities_to_py_interface,
            output_folder_path=capabilities_to_py_interface_out,
            suffix="Interface",
            generate_interface_only_capabilities_in_a_separate_file=True,
            generate_init_file_imports=False,
            generate_registration_methods=False,
            use_supported_decorator=False,
        ),
        TemplateArgs(
            template_path=capabilities_to_py_factory,
            output_folder_path=capabilities_to_py_factory_out,
            suffix="",
            generate_interface_only_capabilities_in_a_separate_file=False,
            generate_init_file_imports=False,
            generate_registration_methods=False,
            use_supported_decorator=False,
        ),
        TemplateArgs(
            template_path=capabilities_to_py_proxy,
            output_folder_path=capabilities_to_py_proxy_out,
            suffix="",
            generate_interface_only_capabilities_in_a_separate_file=False,
            generate_init_file_imports=True,
            generate_registration_methods=False,
            use_supported_decorator=False,
        ),
        TemplateArgs(
            template_path=capabilities_to_py_provider,
            output_folder_path=capabilities_to_py_provider_out,
            suffix="",
            generate_interface_only_capabilities_in_a_separate_file=False,
            generate_init_file_imports=False,
            generate_registration_methods=True,
            use_supported_decorator=True,
        ),
        TemplateArgs(
            template_path=capabilities_to_py_test_interface,
            output_folder_path=capabilities_to_py_test_interface_out,
            suffix="TestInterface",
            generate_interface_only_capabilities_in_a_separate_file=True,
            generate_init_file_imports=False,
            generate_registration_methods=False,
            use_supported_decorator=False,
        ),
        TemplateArgs(
            template_path=capabilities_to_py_test,
            output_folder_path=capabilities_to_py_test_out,
            suffix="Test",
            generate_interface_only_capabilities_in_a_separate_file=False,
            generate_init_file_imports=True,
            generate_registration_methods=False,
            use_supported_decorator=False,
        ),
    ]


def get_jinja_environment():
    """
    Returns a JINJA2 environment instance

    Note: path to the templates folder is grabbed from paths.py
    """
    import jinja2

    from .paths import templates_dir

    template_loader = jinja2.FileSystemLoader(searchpath=templates_dir)
    return jinja2.Environment(loader=template_loader)
