from __future__ import (
    print_function, division, absolute_import, unicode_literals)
from fontTools.misc.py23 import *

from fontTools import unicodedata

import pytest


def test_script():
    assert unicodedata.script("a") == "Latn"
    assert unicodedata.script(unichr(0)) == "Zyyy"
    assert unicodedata.script(unichr(0x0378)) == "Zzzz"
    assert unicodedata.script(unichr(0x10FFFF)) == "Zzzz"

    # these were randomly sampled, one character per script
    assert unicodedata.script(unichr(0x1E918)) == 'Adlm'
    assert unicodedata.script(unichr(0x1170D)) == 'Ahom'
    assert unicodedata.script(unichr(0x145A0)) == 'Hluw'
    assert unicodedata.script(unichr(0x0607)) == 'Arab'
    assert unicodedata.script(unichr(0x056C)) == 'Armn'
    assert unicodedata.script(unichr(0x10B27)) == 'Avst'
    assert unicodedata.script(unichr(0x1B41)) == 'Bali'
    assert unicodedata.script(unichr(0x168AD)) == 'Bamu'
    assert unicodedata.script(unichr(0x16ADD)) == 'Bass'
    assert unicodedata.script(unichr(0x1BE5)) == 'Batk'
    assert unicodedata.script(unichr(0x09F3)) == 'Beng'
    assert unicodedata.script(unichr(0x11C5B)) == 'Bhks'
    assert unicodedata.script(unichr(0x3126)) == 'Bopo'
    assert unicodedata.script(unichr(0x1103B)) == 'Brah'
    assert unicodedata.script(unichr(0x2849)) == 'Brai'
    assert unicodedata.script(unichr(0x1A0A)) == 'Bugi'
    assert unicodedata.script(unichr(0x174E)) == 'Buhd'
    assert unicodedata.script(unichr(0x18EE)) == 'Cans'
    assert unicodedata.script(unichr(0x102B7)) == 'Cari'
    assert unicodedata.script(unichr(0x1053D)) == 'Aghb'
    assert unicodedata.script(unichr(0x11123)) == 'Cakm'
    assert unicodedata.script(unichr(0xAA1F)) == 'Cham'
    assert unicodedata.script(unichr(0xAB95)) == 'Cher'
    assert unicodedata.script(unichr(0x1F0C7)) == 'Zyyy'
    assert unicodedata.script(unichr(0x2C85)) == 'Copt'
    assert unicodedata.script(unichr(0x12014)) == 'Xsux'
    assert unicodedata.script(unichr(0x1082E)) == 'Cprt'
    assert unicodedata.script(unichr(0xA686)) == 'Cyrl'
    assert unicodedata.script(unichr(0x10417)) == 'Dsrt'
    assert unicodedata.script(unichr(0x093E)) == 'Deva'
    assert unicodedata.script(unichr(0x1BC4B)) == 'Dupl'
    assert unicodedata.script(unichr(0x1310C)) == 'Egyp'
    assert unicodedata.script(unichr(0x1051C)) == 'Elba'
    assert unicodedata.script(unichr(0x2DA6)) == 'Ethi'
    assert unicodedata.script(unichr(0x10AD)) == 'Geor'
    assert unicodedata.script(unichr(0x2C52)) == 'Glag'
    assert unicodedata.script(unichr(0x10343)) == 'Goth'
    assert unicodedata.script(unichr(0x11371)) == 'Gran'
    assert unicodedata.script(unichr(0x03D0)) == 'Grek'
    assert unicodedata.script(unichr(0x0AAA)) == 'Gujr'
    assert unicodedata.script(unichr(0x0A4C)) == 'Guru'
    assert unicodedata.script(unichr(0x23C9F)) == 'Hani'
    assert unicodedata.script(unichr(0xC259)) == 'Hang'
    assert unicodedata.script(unichr(0x1722)) == 'Hano'
    assert unicodedata.script(unichr(0x108F5)) == 'Hatr'
    assert unicodedata.script(unichr(0x05C2)) == 'Hebr'
    assert unicodedata.script(unichr(0x1B072)) == 'Hira'
    assert unicodedata.script(unichr(0x10847)) == 'Armi'
    assert unicodedata.script(unichr(0x033A)) == 'Zinh'
    assert unicodedata.script(unichr(0x10B66)) == 'Phli'
    assert unicodedata.script(unichr(0x10B4B)) == 'Prti'
    assert unicodedata.script(unichr(0xA98A)) == 'Java'
    assert unicodedata.script(unichr(0x110B2)) == 'Kthi'
    assert unicodedata.script(unichr(0x0CC6)) == 'Knda'
    assert unicodedata.script(unichr(0x3337)) == 'Kana'
    assert unicodedata.script(unichr(0xA915)) == 'Kali'
    assert unicodedata.script(unichr(0x10A2E)) == 'Khar'
    assert unicodedata.script(unichr(0x17AA)) == 'Khmr'
    assert unicodedata.script(unichr(0x11225)) == 'Khoj'
    assert unicodedata.script(unichr(0x112B6)) == 'Sind'
    assert unicodedata.script(unichr(0x0ED7)) == 'Laoo'
    assert unicodedata.script(unichr(0xAB3C)) == 'Latn'
    assert unicodedata.script(unichr(0x1C48)) == 'Lepc'
    assert unicodedata.script(unichr(0x1923)) == 'Limb'
    assert unicodedata.script(unichr(0x1071D)) == 'Lina'
    assert unicodedata.script(unichr(0x100EC)) == 'Linb'
    assert unicodedata.script(unichr(0xA4E9)) == 'Lisu'
    assert unicodedata.script(unichr(0x10284)) == 'Lyci'
    assert unicodedata.script(unichr(0x10926)) == 'Lydi'
    assert unicodedata.script(unichr(0x11161)) == 'Mahj'
    assert unicodedata.script(unichr(0x0D56)) == 'Mlym'
    assert unicodedata.script(unichr(0x0856)) == 'Mand'
    assert unicodedata.script(unichr(0x10AF0)) == 'Mani'
    assert unicodedata.script(unichr(0x11CB0)) == 'Marc'
    assert unicodedata.script(unichr(0x11D28)) == 'Gonm'
    assert unicodedata.script(unichr(0xABDD)) == 'Mtei'
    assert unicodedata.script(unichr(0x1E897)) == 'Mend'
    assert unicodedata.script(unichr(0x109B0)) == 'Merc'
    assert unicodedata.script(unichr(0x10993)) == 'Mero'
    assert unicodedata.script(unichr(0x16F5D)) == 'Plrd'
    assert unicodedata.script(unichr(0x1160B)) == 'Modi'
    assert unicodedata.script(unichr(0x18A8)) == 'Mong'
    assert unicodedata.script(unichr(0x16A48)) == 'Mroo'
    assert unicodedata.script(unichr(0x1128C)) == 'Mult'
    assert unicodedata.script(unichr(0x105B)) == 'Mymr'
    assert unicodedata.script(unichr(0x108AF)) == 'Nbat'
    assert unicodedata.script(unichr(0x19B3)) == 'Talu'
    assert unicodedata.script(unichr(0x1143D)) == 'Newa'
    assert unicodedata.script(unichr(0x07F4)) == 'Nkoo'
    assert unicodedata.script(unichr(0x1B192)) == 'Nshu'
    assert unicodedata.script(unichr(0x169C)) == 'Ogam'
    assert unicodedata.script(unichr(0x1C56)) == 'Olck'
    assert unicodedata.script(unichr(0x10CE9)) == 'Hung'
    assert unicodedata.script(unichr(0x10316)) == 'Ital'
    assert unicodedata.script(unichr(0x10A93)) == 'Narb'
    assert unicodedata.script(unichr(0x1035A)) == 'Perm'
    assert unicodedata.script(unichr(0x103D5)) == 'Xpeo'
    assert unicodedata.script(unichr(0x10A65)) == 'Sarb'
    assert unicodedata.script(unichr(0x10C09)) == 'Orkh'
    assert unicodedata.script(unichr(0x0B60)) == 'Orya'
    assert unicodedata.script(unichr(0x104CF)) == 'Osge'
    assert unicodedata.script(unichr(0x104A8)) == 'Osma'
    assert unicodedata.script(unichr(0x16B12)) == 'Hmng'
    assert unicodedata.script(unichr(0x10879)) == 'Palm'
    assert unicodedata.script(unichr(0x11AF1)) == 'Pauc'
    assert unicodedata.script(unichr(0xA869)) == 'Phag'
    assert unicodedata.script(unichr(0x10909)) == 'Phnx'
    assert unicodedata.script(unichr(0x10B81)) == 'Phlp'
    assert unicodedata.script(unichr(0xA941)) == 'Rjng'
    assert unicodedata.script(unichr(0x16C3)) == 'Runr'
    assert unicodedata.script(unichr(0x0814)) == 'Samr'
    assert unicodedata.script(unichr(0xA88C)) == 'Saur'
    assert unicodedata.script(unichr(0x111C8)) == 'Shrd'
    assert unicodedata.script(unichr(0x1045F)) == 'Shaw'
    assert unicodedata.script(unichr(0x115AD)) == 'Sidd'
    assert unicodedata.script(unichr(0x1D8C0)) == 'Sgnw'
    assert unicodedata.script(unichr(0x0DB9)) == 'Sinh'
    assert unicodedata.script(unichr(0x110F9)) == 'Sora'
    assert unicodedata.script(unichr(0x11A60)) == 'Soyo'
    assert unicodedata.script(unichr(0x1B94)) == 'Sund'
    assert unicodedata.script(unichr(0xA81F)) == 'Sylo'
    assert unicodedata.script(unichr(0x0740)) == 'Syrc'
    assert unicodedata.script(unichr(0x1714)) == 'Tglg'
    assert unicodedata.script(unichr(0x1761)) == 'Tagb'
    assert unicodedata.script(unichr(0x1965)) == 'Tale'
    assert unicodedata.script(unichr(0x1A32)) == 'Lana'
    assert unicodedata.script(unichr(0xAA86)) == 'Tavt'
    assert unicodedata.script(unichr(0x116A5)) == 'Takr'
    assert unicodedata.script(unichr(0x0B8E)) == 'Taml'
    assert unicodedata.script(unichr(0x1754D)) == 'Tang'
    assert unicodedata.script(unichr(0x0C40)) == 'Telu'
    assert unicodedata.script(unichr(0x07A4)) == 'Thaa'
    assert unicodedata.script(unichr(0x0E42)) == 'Thai'
    assert unicodedata.script(unichr(0x0F09)) == 'Tibt'
    assert unicodedata.script(unichr(0x2D3A)) == 'Tfng'
    assert unicodedata.script(unichr(0x114B0)) == 'Tirh'
    assert unicodedata.script(unichr(0x1038B)) == 'Ugar'
    assert unicodedata.script(unichr(0xA585)) == 'Vaii'
    assert unicodedata.script(unichr(0x118CF)) == 'Wara'
    assert unicodedata.script(unichr(0xA066)) == 'Yiii'
    assert unicodedata.script(unichr(0x11A31)) == 'Zanb'


def test_script_extension():
    assert unicodedata.script_extension("a") == {"Latn"}
    assert unicodedata.script_extension(unichr(0)) == {"Zyyy"}
    assert unicodedata.script_extension(unichr(0x0378)) == {"Zzzz"}
    assert unicodedata.script_extension(unichr(0x10FFFF)) == {"Zzzz"}

    assert unicodedata.script_extension("\u0660") == {'Arab', 'Thaa'}
    assert unicodedata.script_extension("\u0964") == {
        'Beng', 'Deva', 'Gran', 'Gujr', 'Guru', 'Knda', 'Mahj', 'Mlym',
        'Orya', 'Sind', 'Sinh', 'Sylo', 'Takr', 'Taml', 'Telu', 'Tirh'}


def test_script_name():
    assert unicodedata.script_name("Latn") == "Latin"
    assert unicodedata.script_name("Zyyy") == "Common"
    assert unicodedata.script_name("Zzzz") == "Unknown"
    # underscores in long names are replaced by spaces
    assert unicodedata.script_name("Egyp") == "Egyptian Hieroglyphs"

    with pytest.raises(KeyError):
        unicodedata.script_name("QQQQ")
    assert unicodedata.script_name("QQQQ", default="Unknown")


def test_script_code():
    assert unicodedata.script_code("Latin") == "Latn"
    assert unicodedata.script_code("Common") == "Zyyy"
    assert unicodedata.script_code("Unknown") == "Zzzz"
    # case, whitespace, underscores and hyphens are ignored
    assert unicodedata.script_code("Egyptian Hieroglyphs") == "Egyp"
    assert unicodedata.script_code("Egyptian_Hieroglyphs") == "Egyp"
    assert unicodedata.script_code("egyptianhieroglyphs") == "Egyp"
    assert unicodedata.script_code("Egyptian-Hieroglyphs") == "Egyp"

    with pytest.raises(KeyError):
        unicodedata.script_code("Does not exist")
    assert unicodedata.script_code("Does not exist", default="Zzzz") == "Zzzz"


def test_block():
    assert unicodedata.block("\x00") == "Basic Latin"
    assert unicodedata.block("\x7F") == "Basic Latin"
    assert unicodedata.block("\x80") == "Latin-1 Supplement"
    assert unicodedata.block("\u1c90") == "No_Block"


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main(sys.argv))