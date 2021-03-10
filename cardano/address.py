from .consts import Era

class Address(object):
    _address = ""
    era = None
    wallet = None

    def __init__(self, addr, wallet=None):
        self._address = addr
        self.wallet = wallet or self.wallet
        if addr.startswith("Ae2") or addr.startswith("DdzFF"):
            self.era = Era.BYRON
        elif addr.startswith("addr1"):
            self.era = Era.SHELLEY
        else:
            raise ValueError("String {} is not a valid Cardano address")

    def __repr__(self):
        return self._address

    def __eq__(self, other):
        if isinstance(other, Address):
            return str(self) == str(other)
        elif isinstance(other, str):
            return str(self) == other
        elif isinstance(other, bytes):
            return str(self).encode() == other
        return super(Address, self).__eq__(other)