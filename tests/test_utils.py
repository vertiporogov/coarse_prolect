import pytest

from src import utils

def test_date_processing():
    assert utils.date_processing("2019-06-30T15:11:53.136004") == '30.06.2019'
    with pytest.raises(ValueError):
        utils.date_processing("test")

@pytest.mark.parametrize('operations, expected', [
    ([], ''),
    ([{"date": "2019-06-30T15:11:53.136004",
    "operationAmount": {
      "amount": "95860.47",
      "currency": {
        "name": "руб."
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 59956820797131895975",
    "to": "Счет 43475624104328495820"
  }], '30.06.2019 Перевод со счета на счет\n'
 'Счет 5995 68** **** 9597 -> Счет **9582\n'
 '95860.47 руб.\n'
 '\n')
])
def test_output_information(operations, expected):
    assert utils.output_information(operations) == expected
    with pytest.raises(TypeError):
        utils.output_information("test")
        utils.output_information(([1, 2]))
        utils.output_information((['1', '2']))
