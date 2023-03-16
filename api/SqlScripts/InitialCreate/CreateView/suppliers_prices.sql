CREATE VIEW IF NOT EXISTS suppliers_prices AS
SELECT
suppliers.name AS supplier_name,
suppliers.currency,
auto_partner_gdansk.manufacturer,
auto_partner_gdansk.supplier_part_number,
auto_partner_gdansk.part_number,
auto_partner_gdansk.price,
auto_partner_gdansk.quantity
FROM suppliers
INNER JOIN auto_partner_gdansk
ON suppliers.id = auto_partner_gdansk.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
emoto.manufacturer,
emoto.supplier_part_number,
emoto.part_number,
emoto.price,
emoto.quantity
FROM suppliers
INNER JOIN emoto
ON suppliers.id = emoto.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
gordon.manufacturer,
gordon.supplier_part_number,
gordon.part_number,
gordon.price,
gordon.quantity
FROM suppliers
INNER JOIN gordon
ON suppliers.id = gordon.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
motorol.manufacturer,
motorol.supplier_part_number,
motorol.part_number,
motorol.price,
motorol.quantity
FROM suppliers
INNER JOIN motorol
ON suppliers.id = motorol.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
paketo.manufacturer,
paketo.supplier_part_number,
paketo.part_number,
paketo.price,
paketo.quantity
FROM suppliers
INNER JOIN paketo
ON suppliers.id = paketo.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
hart.manufacturer,
hart.supplier_part_number,
hart.part_number,
hart.price,
hart.quantity
FROM suppliers
INNER JOIN hart
ON suppliers.id = hart.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
rodon.manufacturer,
rodon.supplier_part_number,
rodon.part_number,
rodon.price,
rodon.quantity
FROM suppliers
INNER JOIN rodon
ON suppliers.id = rodon.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
motogama.manufacturer,
motogama.supplier_part_number,
motogama.part_number,
motogama.price,
motogama.quantity
FROM suppliers
INNER JOIN motogama
ON suppliers.id = motogama.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
autoland.manufacturer,
autoland.supplier_part_number,
autoland.part_number,
autoland.price,
autoland.quantity
FROM suppliers
INNER JOIN autoland
ON suppliers.id = autoland.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
elit.manufacturer,
elit.supplier_part_number,
elit.part_number,
elit.price,
elit.quantity
FROM suppliers
INNER JOIN elit
ON suppliers.id = elit.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
motoprofil.manufacturer,
motoprofil.supplier_part_number,
motoprofil.part_number,
motoprofil.price,
motoprofil.quantity
FROM suppliers
INNER JOIN motoprofil
ON suppliers.id = motoprofil.supplier_id

UNION

SELECT
suppliers.name AS supplier_name,
suppliers.currency,
inter_team.manufacturer,
inter_team.supplier_part_number,
inter_team.part_number,
inter_team.price,
inter_team.quantity
FROM suppliers
INNER JOIN inter_team
ON suppliers.id = inter_team.supplier_id
