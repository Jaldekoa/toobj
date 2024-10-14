class ToObj:
    """
    Transform a dictionary into an object.
    """

    def __init__(self, d: dict):
        """
        Transform a dictionary into an object.

        Args:
            d (dict): Dictionary to be converted.
        """
        for k, v in d.items():
            if isinstance(v, dict):
                setattr(self, k, ToObj(v))
            elif isinstance(v, list):
                setattr(self, k, [self.__convert_list(el) for el in v])
            else:
                setattr(self, k, v)

    def __convert_list(self, el):
        """
        Recursively transform a list of dictionaries into an object.

        Args:
            el (dict or list): List of dictionaries to be converted.

        Returns:
            object or list[object]: Converted object or list of objects.
        """
        if isinstance(el, dict):
            return ToObj(el)
        elif isinstance(el, list):
            return [self.__convert_list(e) for e in el]
        return el