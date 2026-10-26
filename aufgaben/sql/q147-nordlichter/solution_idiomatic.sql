UPDATE fuetterungen
SET menge = menge + 1
WHERE pinguin_id IN (SELECT id FROM pinguine WHERE kolonie = 'Nord');
