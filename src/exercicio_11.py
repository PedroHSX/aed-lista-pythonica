def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    """
    Substitui um convidado indisponível por outro.
    """
    index = guests.index(unavailable)
    guests[index] = new_guest
    return guests