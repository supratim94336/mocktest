from unittest.mock import Mock, call
from src.backend import Order


def test_order_is_filled():
    # setup - data
    order = Order('Talisker', 50)
    warehouse = Mock()
    # setup - expectations
    warehouse.has_inventory.return_value = True
    warehouse.remove.return_value = None
    # exercise
    order.fill(warehouse)

    # verify
    assert order.is_filled()
    warehouse.has_inventory.assert_called_with('Talisker', 50)
    warehouse.assert_has_calls(
        [
            call.has_inventory('Talisker', 50),
            call.remove('Talisker', 50)
        ]
    )


def test_order_is_not_filled():
    # setup - data
    order = Order('Talisker', 50)
    warehouse = Mock()

    # setup - expectations
    warehouse.has_inventory.return_value = False

    # exercise
    order.fill(warehouse)

    # verify
    assert not order.is_filled()
    warehouse.has_inventory.assert_called_with('Talisker', 50)
    warehouse.remove.assert_not_called()
