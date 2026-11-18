import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from supplier import Supplier
from inventory import Inventory
from product_loader import load_products

CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


def run_loader(path: str) -> tuple[Inventory, list[str]]:
    inventory = Inventory()
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    output = io.StringIO()
    with redirect_stdout(output):
        load_products(path, inventory, supplier)
    return inventory, output.getvalue().strip().splitlines()


class TestLoadProducts(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.folder.name, "products.csv")
        with open(self.path, "w", newline="") as file:
            file.write(CSV_TEXT)

    def tearDown(self) -> None:
        self.folder.cleanup()

    def test_valid_rows_load_and_bad_rows_are_skipped(self) -> None:
        inventory, lines = run_loader(self.path)
        ids = [p.get_product_id() for p in inventory.get_products()]
        self.assertEqual(ids, ["P001", "D001", "P003"])

    def test_unknown_type_and_bad_price_are_reported(self) -> None:
        inventory, lines = run_loader(self.path)
        self.assertEqual(lines[0], "Row 4 skipped: Unknown product type: service")
        self.assertTrue(lines[1].startswith("Row 5 skipped:"))

    def test_messages_print_in_the_expected_order(self) -> None:
        inventory, lines = run_loader(self.path)
        self.assertEqual(lines[-2], "3 products loaded.")
        self.assertEqual(lines[-1], "Load attempt finished.")

    def test_missing_file_is_handled_without_crashing(self) -> None:
        missing = os.path.join(self.folder.name, "nothing.csv")
        inventory, lines = run_loader(missing)
        self.assertEqual(lines, [f"Products file not found: {missing}", "Load attempt finished."])
        self.assertEqual(inventory.get_products(), [])

    def test_row_with_wrong_number_of_columns_is_skipped(self) -> None:
        with open(self.path, "w", newline="") as file:
            file.write("product_type,product_id,name,price,stock_quantity\nphysical,P009,Short\n")
        inventory, lines = run_loader(self.path)
        self.assertEqual(inventory.get_products(), [])
        self.assertTrue(lines[0].startswith("Row 2 skipped:"))


if __name__ == "__main__":
    unittest.main()
