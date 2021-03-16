def prepare_signature_str(ordered_signature):
    """Build signature string from OrderedDict with metadata

    :param ordered_signature: OrderedDict with metadata
    :return: string signature
    """
    return "{}_{}_{}_{}".format(ordered_signature.get('name'),
                                ordered_signature.get('create_date'),
                                ordered_signature.get('size'),
                                ordered_signature.get('content'))