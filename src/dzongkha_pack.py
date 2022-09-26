"""
Create custom language pack for transliteration.
"""
from src import utils
from transliterate import get_available_language_codes
from transliterate.base import TranslitLanguagePack, registry


class DzongkhaLanguagePack(TranslitLanguagePack):
    """
    Custom Dzongkha Language pack.
    For more information please visit this link
    https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/693691/ROMANIZATION_OF_DZONGKHA.pdf
    """

    # Set the language code
    language_code = 'dz'
    
    # Set the language name
    language_name = 'Dzongkha'

    # Set simple representation of character mapping (source -> target)
    mapping =utils.mapping

    # Set dictionary mapping from source to target
    pre_processor_mapping = utils.pre_processor_mapping
    
    # Set character ranges
    character_ranges = ((0X0F00, 0X0FFF))


registry.register(DzongkhaLanguagePack)

print(get_available_language_codes())
