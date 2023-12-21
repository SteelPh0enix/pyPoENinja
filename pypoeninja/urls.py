"""This module contains URLs to PoE.Ninja API and helper functions for constructing them."""

from dataclasses import dataclass

BASE_URL = "https://poe.ninja/"
"""Base URL of PoE.Ninja."""

API_URL = BASE_URL + "api/data/"
"""URL to PoE.Ninja main API endpoint."""

ENDPOINT_NAMES = {
    "index": "getindexstate",
    "currency": "currencyoverview",
    "item": "itemoverview",
}
"""Map of API endpoints names and paths relative to API URL."""


@dataclass
class CategoryMetadata:
    """Structure containing category metadata."""

    id: str
    """Category ID in PoE.Ninja API."""
    endpoint_name: str
    """Endpoint name."""


CATEGORIES = {
    "Currency": CategoryMetadata("Currency", "currency"),
    "Fragments": CategoryMetadata("Fragment", "currency"),
    "Tattoos": CategoryMetadata("Tattoo", "item"),
    "Omens": CategoryMetadata("Omen", "item"),
    "Divination Cards": CategoryMetadata("DivinationCard", "item"),
    "Artifacts": CategoryMetadata("Artifact", "item"),
    "Oils": CategoryMetadata("Oil", "item"),
    "Incubators": CategoryMetadata("Incubator", "item"),
    "Unique Weapons": CategoryMetadata("UniqueWeapon", "item"),
    "Unique Armours": CategoryMetadata("UniqueArmour", "item"),
    "Unique Accessories": CategoryMetadata("UniqueAccessory", "item"),
    "Unique Flasks": CategoryMetadata("UniqueFlask", "item"),
    "Unique Jewels": CategoryMetadata("UniqueJewel", "item"),
    "Skill Gems": CategoryMetadata("SkillGem", "item"),
    "Cluster Jewels": CategoryMetadata("ClusterJewel", "item"),
    "Maps": CategoryMetadata("Map", "item"),
    "Blighted Maps": CategoryMetadata("BlightedMap", "item"),
    "Blight-ravaged Maps": CategoryMetadata("BlightRavagedMap", "item"),
    "Scourged Maps": CategoryMetadata("ScourgedMap", "item"),
    "Unique Maps": CategoryMetadata("UniqueMap", "item"),
    "DeliriumOrbs": CategoryMetadata("DeliriumOrb", "item"),
    "Invitations": CategoryMetadata("Invitation", "item"),
    "Scarabs": CategoryMetadata("Scarab", "item"),
    "Memories": CategoryMetadata("Memory", "item"),
    "Base Types": CategoryMetadata("BaseType", "item"),
    "Fossils": CategoryMetadata("Fossil", "item"),
    "Resonators": CategoryMetadata("Resonator", "item"),
    "Helmet Enchants": CategoryMetadata("HelmetEnchant", "item"),
    "Beasts": CategoryMetadata("Beast", "item"),
    "Essences": CategoryMetadata("Essence", "item"),
    "Vials": CategoryMetadata("Vial", "item"),
}
"""Map of names and API IDs of categories."""

LANGUAGES = {
    "English": "en",
    "Brazilian": "pt",
    "Russian": "ru",
    "Thai": "th",
    "German": "qe",
    "French": "fr",
    "Spanish": "es",
    "Korean": "ko",
}
"""Map of available API languages, and their ID's"""

DEFAULT_LANGUAGE = "English"
"""Default language used for fetching."""


class UrlException(Exception):
    """Stub class for URL-related exception"""

    pass


def api_index_url() -> str:
    """Returns a full URL to API with general metadata"""
    return f"{API_URL}{ENDPOINT_NAMES['index']}"


def api_category_url(
    league_name: str, category: str, language: str = DEFAULT_LANGUAGE
) -> str:
    """Returns a full URL to a specific category in PoE.Ninja API.

    Args:
        league_name (str): League name.
        category (str): Category name.
        language (str, optional): Language to fetch data in. Defaults to :const:`DEFAULT_LANGUAGE`.
                                  Valid languages are stored in :const:`LANGUAGES` map.
    """
    if category not in CATEGORIES:
        raise UrlException(f"Category '{category}' is not available!")

    if language not in LANGUAGES:
        raise UrlException(f"Language '{language}' is not available!")

    category_metadata = CATEGORIES[category]
    language_id = LANGUAGES[language]
    endpoint = API_URL + ENDPOINT_NAMES[category_metadata.endpoint_name]
    return f"{endpoint}?league={league_name}&type={category_metadata.id}&language={language_id}"
