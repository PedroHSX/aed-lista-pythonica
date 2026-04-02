def add_guests(
    guests: list[str],
    new_guests: list[str]
) -> list[str]:
    """
    Adiciona múltiplos convidados à lista.
    """
    guests.extend(new_guests)
    return guests